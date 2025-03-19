import sys
import pandas as pd
import subprocess

file_path = sys.argv[1]

df = pd.read_csv(file_path)

insights = [
    f" num of data: {len(df)}",
    f" num of columns: {len(df.columns)}",
    f"Summary :\n{df.describe()}"
]

for i, insight in enumerate(insights, 1):
    with open(f"eda-in-{i}.txt", "w") as f:
        f.write(insight)

print("EDA Done")

subprocess.run(["python3", "/home/doc-bd-a1/vis.py", "/home/doc-bd-a1/res_dpre.csv"])

