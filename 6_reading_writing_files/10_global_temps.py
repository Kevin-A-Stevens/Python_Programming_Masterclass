"""
https://www.ncdc.noaa.gov/cag/global/time-series

https://www.ncei.noaa.gov/cag/global/time-series/globe/land_ocean/1/6/1880-2022/data.json

code > reformat to put temperature_anomaly.json
in a more readable format
"""
import json

json_data_source = "temperature_anomaly.json"

with open(json_data_source, encoding='utf-8') as data:
    anomalies = json.load(data)

print(anomalies['description'])

for year, value in anomalies['data'].items():
    year, value = int(year), float(value)
    print(f'{year} ...{value:6.2f}')
print('*' * 80)

print(anomalies['citation'])

