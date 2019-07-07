"""
quickWeather.py - Prints the weather for a location from the command line.
This program is similar to a program found in the online textbook "Automate the Boring Stuff."
It uses api from openweathermap.org.  Since the writing of the textbook the site now requires keys.
The keys for forecast data are free once you register with the website.  I rework the code for the url to
and the key I was given.  I also reworked it so that it finds the weather from the location assigned to the
location variable.   The code for running the program from the command line is
commented out but can be easily put back in.   
"""

import json, requests, sys

"""
Links to the documentation for these important libraries.
https://docs.python.org/3/library/json.html
https://docs.python.org/3/library/sys.html
https://2.python-requests.org/en/master/
"""

"""
Compute location from command line arguments.  To use the command line 
take the take the triple quotes out around the if statement below and 
comment out the location variable assignment.
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])
"""

location = 'Valrico, US'
key = 'appid=8d195f72c65049d55c801a702f095e96'

#http://api.openweathermap.org/data/2.5/forecast?q=Valrico,us&appid=8d195f72c65049d55c801a702f095e96

# Download the JSON data from OpenWeatherMap.org's API.
url ='http://api.openweathermap.org/data/2.5/forecast/?q=%s&%s' % (location,key)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Print weather descriptions.
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
print()
print('Day after the day after tomorrow:')
print(w[3]['weather'][0]['main'], '-', w[3]['weather'][0]['description'])
print()
print('Day after the day after tomorrow the day after:')
print(w[4]['weather'][0]['main'], '-', w[4]['weather'][0]['description'])
print()
print('Day after the day after tomorrow the day after the day after:')
print(w[5]['weather'][0]['main'], '-', w[5]['weather'][0]['description'])



print('\n\nweather data: \n', w)
print('\n\ntoday\'s weather data\n', w[0])
print('\n\ntoday\'s weather list\n', w[0]['weather'])
print()
print()
print(w[0]['weather'][0])
print()
print()
print(w[0]['weather'][0]['main'])
