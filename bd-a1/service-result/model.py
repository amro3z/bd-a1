import sys
import pandas as pd
from sklearn.cluster import KMeans

file_path = sys.argv[1]
df = pd.read_csv(file_path)

df_numeric = df.select_dtypes(include=['float64', 'int64'])

kmeans = KMeans(n_clusters=3, random_state=0)
df['cluster'] = kmeans.fit_predict(df_numeric)

cluster_counts = df['cluster'].value_counts()
with open("k.txt", "w") as f:
    f.write(str(cluster_counts))

print("Done by K-Means!")

