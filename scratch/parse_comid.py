import re
import json

def parse_report():
    with open('tests_simulation/SIMULATION_REPORT.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    details_blocks = re.findall(r'<details>\s*<summary>🔍 Cas (.*?)</summary>(.*?)</details>', content, re.DOTALL)
    
    output = []
    for title, detail in details_blocks:
        json_match = re.search(r'\{.*\}', detail, re.DOTALL)
        if json_match:
            try:
                data = json.loads(json_match.group(0))
                true_keys = []
                justifications = data.get("evaluation.comid.justifications", [])
                for k, v in data.items():
                    if k.startswith("evaluation.comid.") and k != "evaluation.comid.justifications" and v is True:
                        key_name = k.replace("evaluation.comid.", "")
                        true_keys.append(key_name)
                
                output.append(f"Patient: {title}")
                output.append(f"  Score: {len(true_keys)}")
                output.append(f"  True Flags: {true_keys}")
                output.append(f"  Justifications:")
                for j in justifications:
                    if isinstance(j, dict):
                        output.append(f"    - {j.get('code')}: {j.get('justification')}")
                output.append("-" * 50)
            except Exception as e:
                output.append(f"Error parsing {title}: {e}")
                
    with open('scratch/parsed_comid_results.txt', 'w', encoding='utf-8') as out_f:
        out_f.write("\n".join(output))

if __name__ == "__main__":
    parse_report()
