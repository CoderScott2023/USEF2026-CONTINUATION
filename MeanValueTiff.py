import os
import rasterio
import numpy as np
import pandas as pd
from google.colab import drive

drive.mount('/content/drive', force_remount=True)

dataDir = "/content/drive/My Drive/USEF2026/SIF MAPS"

output_csv = "/content/drive/My Drive/USEF2026/sif_mean_values.csv"

mean_values = []

for filename in sorted(os.listdir(dataDir)):
    if filename.lower().endswith(".tif"):
        file_path = os.path.join(dataDir, filename)

        try:
            with rasterio.open(file_path) as src:
                arr = src.read(1).astype(np.float32)

                # Replace nodata with nan
                if src.nodata is not None:
                    arr[arr == src.nodata] = np.nan

            mean_val = float(np.nanmean(arr))
            mean_values.append(mean_val)

            print(f"{filename} → mean = {mean_val}")

        except Exception as e:
            print(f"ERROR reading {filename}: {e}")

df = pd.DataFrame({"mean_pixel_value": mean_values})
df.to_csv(output_csv, index=False)

print("\nSaved mean values to:", output_csv)
df.head()
