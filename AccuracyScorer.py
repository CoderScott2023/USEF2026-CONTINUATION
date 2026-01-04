import pandas as pd
import numpy as np

csv1 = "/content/drive/My Drive/USEF2026/DROUGHT_ANOMALIES/spei3_monthly_mean_final.csv"
csv2 = "/content/drive/My Drive/USEF2026/DROUGHT_ANOMALIES/NDVI/ndvi_full.csv"

s1 = pd.read_csv(csv1, header=None)[0].astype(float)
s2 = pd.read_csv(csv2, header=None)[0].astype(float)

min_len = min(len(s1), len(s2))
s1 = s1[:min_len]
s2 = s2[:min_len]

distances = np.abs(s1 - s2)

mean_distance = distances.mean()

print(f"Mean distance between the two series: {mean_distance}")
