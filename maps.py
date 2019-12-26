import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import os


locations = ["Lahore", "Statue of Liberty", "Moscow", "Berlin", "London"]


# Loop over the locations
for location in locations:
    # Directory where the files are located
    fp = f"\Cities\{location}\shape\\"
    filesDir = os.getcwd() + fp

    # Look for shapefiles only
    files = []
    for i in os.listdir(filesDir):
        if i.endswith('.shp'):
            files.append(os.path.join(filesDir, i))

    # Merge all shapefiles
    data = []
    for filename in files:
        file = filename.split("\\")[-1]
        if file != "places.shp" and file != "points.shp" and file != "buildings.shp":
            data.append(gpd.read_file(filename))

    gdf = pd.concat(data, sort=True)

    # Plot the map
    gdf.plot(linewidth= 0.3, column = "type", cmap="viridis")
    plt.title(location)
    plt.show()