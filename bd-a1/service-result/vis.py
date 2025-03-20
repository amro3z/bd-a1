import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import subprocess

file_path = sys.argv[1]
df = pd.read_csv(file_path)

plt.figure(figsize=(8, 6))
sns.histplot(df, x="age", hue="survived", kde=True, bins=30)
plt.title("Age Distribution by Survival")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()
plt.tight_layout()
plt.savefig("vis.png")

print("VIS Done")

subprocess.run(["python3", "/home/doc-bd-a1/model.py", "/home/doc-bd-a1/res_dpre.csv"])

