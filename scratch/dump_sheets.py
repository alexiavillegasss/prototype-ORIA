import pandas as pd
import os

excel_path = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\config\rules\tableau_besoins_orientation_oria.xlsx"
out_dir = r"c:\Users\milac\Documents\Projet ORIA\prototype-ORIA\scratch"

xl = pd.ExcelFile(excel_path)

for sheet in xl.sheet_names:
    safe_name = sheet.replace(" ", "_").replace("(", "").replace(")", "")
    out_file = os.path.join(out_dir, f"sheet_{safe_name}.txt")
    try:
        df = pd.read_excel(excel_path, sheet_name=sheet)
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(f"Sheet: {sheet}\n\n")
            f.write(df.fillna("").to_string(index=False))
        print(f"Dumped {sheet} to {out_file}")
    except Exception as e:
        print(f"Error dumping {sheet}: {e}")
