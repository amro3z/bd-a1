import sys
import pandas as pd
import subprocess

file_path = sys.argv[1]

df = pd.read_csv(file_path)

df.to_csv("loaded_data.csv", index=False)

print("Data Loaded")

subprocess.run(["python3", "/home/doc-bd-a1/dpre.py", "/home/doc-bd-a1/res_dpre.csv"])
