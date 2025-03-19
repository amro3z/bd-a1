import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import subprocess

file_path = sys.argv[1]
df = pd.read_csv(file_path)

plt.figure(figsize=(8, 6))

sns.boxplot(data=df, x="survived", y="fare", palette="Set2")

plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Ticket Fare")
plt.title("Ticket Fare Distribution by Survival")

plt.tight_layout()
plt.savefig("vis.png")

print("VIS Done")

subprocess.run(["python3", "/home/doc-bd-a1/model.py", "/home/doc-bd-a1/res_dpre.csv"])

