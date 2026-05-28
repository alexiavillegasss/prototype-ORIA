import os
import sys
import asyncio
import time
import re

# Global semaphore to limit parallel executions (prevent CPU/Ollama overload)
CONCURRENCY_LIMIT = 1
sem = asyncio.Semaphore(CONCURRENCY_LIMIT)

async def run_single_simulation(file_name, file_path):
    async with sem:
        start_time = time.time()
        
        # Execute the python script as an isolated subprocess
        # Using sys.executable ensures it uses the same virtual environment's python interpreter
        cmd = [sys.executable, file_path]
        
        try:
            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            # Wait for execution and capture outputs
            stdout, stderr = await process.communicate()
            
            success = (process.returncode == 0)
            stdout_content = stdout.decode('utf-8', errors='ignore')
            error_msg = stderr.decode('utf-8', errors='ignore') if not success else ""
        except Exception as e:
            success = False
            stdout_content = ""
            error_msg = f"Failed to launch subprocess: {e}"
            
        duration = time.time() - start_time
        
        # Parse score and orientation from output
        comid_score = "N/A"
        orientation = "N/A"
        
        # Attempt to parse COMID score
        score_matches = re.findall(r"Score Total\s*:\s*(\d+)", stdout_content)
        if score_matches:
            comid_score = score_matches[-1]
            
        # Attempt to parse primary orientation
        # Example 1: [ CEV - Cellule écoute et Vigilance ] - Priorite : 95
        # Example 2: VOTRE PRIORITÉ ABSOLUE : [ CEV ]
        ori_match = re.search(r"\[\s*([^\]]+?)\s*\]\s*-\s*Priorit[ée]\s*:\s*(\d+)", stdout_content)
        if ori_match:
            orientation = ori_match.group(1).strip()
        else:
            ori_match_2 = re.search(r"PRIORIT[ÉE]\s*ABSOLUE\s*:\s*\[\s*([^\]]+?)\s*\]", stdout_content, re.IGNORECASE)
            if ori_match_2:
                orientation = ori_match_2.group(1).strip()
            else:
                # Fallback to finding first bracket structure
                ori_match_3 = re.search(r"\[\s*([^\]]{3,100}?)\s*\]", stdout_content)
                if ori_match_3:
                    orientation = ori_match_3.group(1).strip()

        return {
            "file_name": file_name,
            "success": success,
            "error": error_msg,
            "duration": duration,
            "stdout": stdout_content,
            "comid_score": comid_score,
            "orientation": orientation
        }

async def main():
    print("=============================================================")
    print("   ORIA - LANCEUR ULTRA-RAPIDE DE TOUTES LES SIMULATIONS     ")
    print("=============================================================")
    
    test_dir = 'tests_simulation'
    # List all files starting with test_ and ending with .py, excluding run_all_simulations.py and test_anonymizer.py
    files = [f for f in os.listdir(test_dir) if f.startswith('test_') and f.endswith('.py') and f not in ['run_all_simulations.py', 'test_anonymizer.py']]
    files.sort()
    
    print(f"Détection de {len(files)} simulations cliniques.")
    print(f"Exécution en parallèle avec une limite de {CONCURRENCY_LIMIT} processus simultanés...\n")
    
    start_total = time.time()
    
    tasks = []
    for f in files:
        path = os.path.join(test_dir, f)
        tasks.append(run_single_simulation(f, path))
        
    results = []
    completed_count = 0
    for future in asyncio.as_completed(tasks):
        r = await future
        results.append(r)
        completed_count += 1
        name_clean = r["file_name"].replace("test_", "").replace(".py", "").replace("_", " ").title()
        status_str = "✅ SUCCESS" if r["success"] else "❌ FAILED"
        duration_str = f"{r['duration']:.1f}s"
        
        # Display instant status updates
        print(f"[{completed_count}/{len(files)}] {name_clean:<25} : {status_str:<8} | COMID: {r['comid_score']:<2} | {r['orientation'][:30]:<30} | {duration_str}")
        
    total_duration = time.time() - start_total
    
    # Generate gorgeous console output table
    print("\n" + "="*95)
    print(f" {'Nom de la Simulation':<30} | {'Status':<8} | {'Score COMID':<11} | {'Orientation Principale':<25} | {'Temps':<6}")
    print("="*95)
    
    success_count = 0
    for r in results:
        status_str = "SUCCESS" if r["success"] else "FAILED"
        name_clean = r["file_name"].replace("test_", "").replace(".py", "").replace("_", " ").title()
        duration_str = f"{r['duration']:.1f}s"
        
        print(f" {name_clean:<30} | {status_str:<8} | {r['comid_score']:^11} | {r['orientation'][:25]:<25} | {duration_str:<6}")
        if r["success"]:
            success_count += 1
            
    print("="*95)
    print(f"Rapport global : {success_count}/{len(results)} réussis.")
    print(f"Temps total d'exécution : {total_duration:.2f} secondes.")
    print("="*95)
    
    # Generate dynamic Markdown report
    report_path = os.path.join(test_dir, 'SIMULATION_REPORT.md')
    with open(report_path, 'w', encoding='utf-8') as rep:
        rep.write("# 📋 Rapport d'Évaluation Clinique ORIA\n\n")
        rep.write(f"Généré automatiquement le : `{time.strftime('%Y-%m-%d %H:%M:%S')}`  \n")
        rep.write(f"Nombre de cas exécutés : **{len(results)}**  \n")
        rep.write(f"Taux de succès : **{success_count}/{len(results)}**  \n")
        rep.write(f"Temps d'exécution total : **{total_duration:.2f} secondes**  \n\n")
        
        rep.write("## 📊 Tableau récapitulatif des Orientations\n\n")
        rep.write("| Patient | Status | Score COMID | Orientation Principale | Temps d'exécution |\n")
        rep.write("| :--- | :---: | :---: | :--- | :---: |\n")
        
        for r in results:
            name_clean = r["file_name"].replace("test_", "").replace(".py", "").replace("_", " ").title()
            status_icon = "✅ SUCCESS" if r["success"] else "❌ FAILED"
            rep.write(f"| **{name_clean}** | {status_icon} | {r['comid_score']} | `{r['orientation']}` | {r['duration']:.2f}s |\n")
            
        rep.write("\n---\n\n## 📝 Détail des extractions et raisonnements\n\n")
        for r in results:
            name_clean = r["file_name"].replace("test_", "").replace(".py", "").replace("_", " ").title()
            rep.write(f"<details>\n<summary>🔍 Cas {name_clean} (Détail des logs)</summary>\n\n")
            rep.write("```text\n")
            rep.write(r["stdout"] or r["error"])
            rep.write("\n```\n\n</details>\n\n")
            
    print(f"\n[INFO] Rapport détaillé généré dans : {report_path}")

if __name__ == "__main__":
    asyncio.run(main())
