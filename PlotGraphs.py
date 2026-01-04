import pandas as pd
import matplotlib.pyplot as plt
from google.colab import drive

drive.mount('/content/drive', force_remount=True)

csv1 = "/content/drive/My Drive/USEF2026/DROUGHT_ANOMALIES/NDVI/ndvi_full.csv"
csv2 = "/content/drive/My Drive/USEF2026/DROUGHT_ANOMALIES/SIF/sif_full.csv"
csv3 = "/content/drive/My Drive/USEF2026/DROUGHT_ANOMALIES/spei3_monthly_mean_final.csv"

s1 = pd.read_csv(csv1, header=None)[0].astype(float)
s2 = pd.read_csv(csv2, header=None)[0].astype(float)
s3 = pd.read_csv(csv3, header=None)[0].astype(float)

months = range(1, len(s1) + 1)

all_data = pd.concat([s1, s2, s3])
y_min = all_data.min() - 0.1 * abs(all_data.min())
y_max = all_data.max() + 0.1 * abs(all_data.max())

plt.figure(figsize=(14, 7))
plt.plot(months, s1, label="NDVI", linewidth=2)
plt.plot(months, s2, label="SIF", linewidth=2)
plt.plot(months, s3, label="SPEI3", linewidth=2)

plt.ylim(y_min, y_max)  # auto-scaled
plt.xlabel("Months")
plt.ylabel("Normalized / Z-score Value")
plt.title("Vegetation Index Trends & Drought Index (Z-score)")
plt.legend()
plt.grid(True, alpha=0.3)

plt.show()
