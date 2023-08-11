import pandas as pd
import json
import requests

station_json = requests.get('https://gbfs.lyft.com/gbfs/2.3/bkn/fr/station_information.json').json()
station_list = station_json.get('data').get('stations')

df = pd.DataFrame(station_list)
df.to_csv('station_list.csv')

