import sys
import pandas as pd
import subprocess

file_path = sys.argv[1]

df = pd.read_csv(file_path, encoding='utf-8')
df.drop(columns=['Ticket', 'Cabin', 'Name' , 'PassengerId'], errors='ignore', inplace=True)
duplicates = df[df.duplicated()]
duplicates_count = df.duplicated().sum()
print(f"Num of Columns after Drop {df.shape[0] - duplicates_count}")
df.drop_duplicates(inplace=True)
print("Preprocess Done")

df.to_csv("res_dpre.csv", index=False)
subprocess.run(["python3", "/home/doc-bd-a1/eda.py", "/home/doc-bd-a1/res_dpre.csv"])

