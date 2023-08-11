import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

radius_km = 0.4
center_point = Point(40.7526134476784, -74.00134527272574)
buffer = center_point.buffer(radius_km / 111.32)  # Convert km to degrees approx.

station_information_df = pd.read_csv('station_information.csv')
station_status_df = pd.read_csv('station_status.csv')

geometry = [Point(xy) for xy in zip(station_information_df['lat'], station_information_df['lon'])]
station_information_df = gpd.GeoDataFrame(station_information_df, geometry=geometry, crs='EPSG:4326')
station_information_df = station_information_df[station_information_df.geometry.within(buffer)]

merged_df = station_information_df.merge(station_status_df, on='station_id')
merged_df.rename(columns={'num_bikes_available': 'total_num_bikes_available'}, inplace=True)
merged_df['num_regular_bikes_available'] = \
    merged_df['total_num_bikes_available'] - merged_df['num_ebikes_available']

print(merged_df[['station_id', 'name', 'total_num_bikes_available', 
                'num_regular_bikes_available', 'num_ebikes_available']])
