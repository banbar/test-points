import csv
import geopandas as gpd
import pandas as pd

class point:
    def __init__(self, id, latitude, longitude, name):
        self.id = id
        self.lat = latitude
        self.lon = longitude
        self.name = name

def open_points(file):
    data_list = []

    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # Skip/save the header row if needed
        
        for row in csv_reader:
            data_list.append(row)  # Add each row to the list
    
    poi_list = []
    for i in range(len(data_list)):
        p = point(data_list[i][0], 
                  float(data_list[i][1]),
                  float(data_list[i][2]),
                  data_list[i][3])
        poi_list.append(p)
    return poi_list



def export_as_geojson(file_name):
    # Read CSV file
    df = pd.read_csv(file_name)

    # Convert to GeoDataFrame with Point geometry
    gdf = gpd.GeoDataFrame(
        df, 
        geometry=gpd.points_from_xy(df.longitude, df.latitude),
        crs="EPSG:4326"  # WGS84 coordinate reference system
    )

    # Save as GeoJSON
    gdf.to_file("points.geojson", driver="GeoJSON")
                    