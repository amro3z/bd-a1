import sys
import pandas as pd
import subprocess

file_path = sys.argv[1]

df = pd.read_csv(file_path, encoding='utf-8')
df.drop(columns=['Ticket', 'Cabin', 'Name' , 'PassengerId'], errors='ignore', inplace=True)
df.columns = df.columns.str.strip().str.lower()
df.fillna(df.median(numeric_only=True), inplace=True)
df.drop_duplicates(inplace=True)
duplicates_count = df.duplicated().sum()
print(f"Num of Duplicates Columns {duplicates_count}")

for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].str.lower()

print(f" Num of Columns after lowercase: {df.shape[0]}")

df.to_csv("res_dpre.csv", index=False)

print("Preprocess Done")

subprocess.run(["python3", "/home/doc-bd-a1/eda.py", "/home/doc-bd-a1/res_dpre.csv"])

