import pandas as pd
import json
import requests

station_status_json = requests.get('https://gbfs.lyft.com/gbfs/2.3/bkn/en/station_status.json').json()
station_list = station_status_json.get('data').get('stations')
station_list_map = {}

for station in station_list:
	if not station_list_map.get(station.get('station_id')):
		station_list_map[station.get('station_id')] = station

df = pd.DataFrame(station_list_map.values())
df.to_csv('station_status.csv')
