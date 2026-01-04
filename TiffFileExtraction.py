import ee
import datetime

ee.Authenticate()
ee.Initialize(project="boxwood-dynamo-419312")

modis = ee.ImageCollection("MODIS/061/MOD17A2HGF") \
    .select("Gpp")

wasatchFrontAreaBounding = ee.Geometry.Polygon([[
    [-113, 40], [-113, 42],
    [-111, 42], [-111, 40],
    [-113, 40]
]])

gpp_full = modis.filterDate('2013-03-01', '2025-01-01')

gpp_mean = gpp_full.mean()
gpp_std  = gpp_full.reduce(ee.Reducer.stdDev())

def getMonthlyGPP_Z(year, month):
    start = datetime.date(year, month, 1)
    end = datetime.date(year + (month == 12), (month % 12) + 1, 1)

    monthly = gpp_full.filterDate(str(start), str(end)).median()

    # z-score normalization per pixel:
    z = monthly.subtract(gpp_mean).divide(gpp_std)
    return z.rename("GPP_Z")

for year in range(2013, 2025):
    for month in range(1, 13):
        zmap = getMonthlyGPP_Z(year, month)

        task = ee.batch.Export.image.toDrive(
            image=zmap.clip(wasatchFrontAreaBounding),
            description=f'GPP_Z_Year_{year}_Month_{month:02d}',
            folder='GPP SCIENCE FAIR',
            scale=5550,
            region=wasatchFrontAreaBounding,
            maxPixels=1e13
        )
        task.start()

        print(f"Started export: {year}-{month:02d}")
