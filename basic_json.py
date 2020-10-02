import json, requests


start = '20130808 15:00'
end = '20130808 15:06'





start = '20130808 15:00'
end = '20130808 15:06'
# Stations that around Tampa Bay that have temperature data available.
station1 = '8726520' # St Petersburg
station2 = '8726384' # Port Manatee
station3 = '8726607' # Old Port Tampa Bay
station4 = '8726667' # Mckay Bay Entrance
station5 = '8726724' # Clearwater Beach

STATION = station2 # Pick one of the stations listed above

# Time Zones
zone1 = 'gmt' # Greenwich Mean Time.
zone2 = 'lst'  # Local Standard Time. The time local to the requested station.
zone3 =  'lst_ldt' # Local Standard/Local Daylight Time. The time local to the requested station.

part1 = f'https://tidesandcurrents.noaa.gov/api/datagetter?'
part2 = f'begin_date={start}&end_date={end}&station={STATION}'
part3 = f'&product=water_temperature&units=english&time_zone={zone2}'
part4 = f'&application=ports_screen&format=json'

# url = f'https://tidesandcurrents.noaa.gov/api/datagetter?begin_date={start3}&end_date={end3}&station={STATION}&product=water_temperature&units=english&time_zone={zone2}&application=ports_screen&format=json'

url = part1 + part2 + part3 + part4

response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
data = json.loads(response.text)
print(data)
