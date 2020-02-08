# TO-DO:
# Get the rest of the useful data, put it all in a dictonary to put return from this api
# write tests for each of the sub functions:
#   potentially put the helper functions in a different file
# write a function to get the city name or airport name

'''
Brian Macomber - U25993688
References:
https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
https://www.dataquest.io/blog/python-api-tutorial/
'''

import csv
import json
import flask
from flask import jsonify
import requests
from secret import api_key

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# using the ident code of an airport, get the geographical coordinates
def getGeoCoords(ident):
    with open('airports.csv', mode='r') as airports_csv:

        csv_reader = csv.reader(airports_csv, delimiter=',')

        for row in csv_reader:
            if ident == row[1]:
                return (row[4], row[5])

    return ("", "")


# using the latitude and longitude, the current weather of that airport is returned
def getAirportWeather(lat, lon):
    params = {"lat": lat, "lon": lon, "appid": api_key}
    url = "http://api.openweathermap.org/data/2.5/weather"
    Data = requests.get(url, params=params)

    if (Data.status_code == 200):
        usefulData = Data.__dict__
        weatherDataBytes = usefulData.get('_content')
        weatherDataDict = json.loads(weatherDataBytes.decode('utf-8'))
        return weatherDataDict
    else:
        return ""


# returns the usefule data to display for the api
def parseData(weatherData):
    # things i want: temp, feels like, min temp, max temp, wind speed
    weatherDataBytes = weatherData.get('_content')
    weatherDataDict = json.loads(weatherDataBytes.decode('utf-8'))

    temp = weatherDataDict['main']['temp']
    feels_like = weatherDataDict['main']['feels_like']
    temp_min = weatherDataDict['main']['temp_min']
    temp_max = weatherDataDict['main']['temp_max']

    # Description
    return (temp, feels_like, temp_min, temp_max)


ident_name = "00AA"

lat, lon = getGeoCoords(ident_name)
# if lat == "" || lon == "":


data = getAirportWeather(lat, lon)
# if data is "":

# (temp, feels_like, minTemp, maxTemp) = parseData(data)


@app.route('/api/current_weather', methods=['GET'])
def user_api():
    return jsonify(data)


app.run()
