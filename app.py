# TO-DO:
# Get the rest of the useful data, put it all in a dictonary to put return from this api
# write tests for each of the sub functions:
#   potentially put the helper functions in a different file
# write a function to get the city name or airport name
# maybe write in different returns for different status codes

'''
Brian Macomber - U25993688
References:
https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
https://www.dataquest.io/blog/python-api-tutorial/
'''

import json
import flask
from flask import jsonify
import requests
from secret import api_key
from getGeoCoords import getGeoCoords

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# using the latitude and longitude, the current weather of that airport is returned
def getAirportWeather(lat, lon):
    if (lat == "") or (lon == ""):
        return ""
    else:
        params = {"lat": lat, "lon": lon, "appid": api_key}
        url = "http://api.openweathermap.org/data/2.5/weather"
        Data = requests.get(url, params=params)

        # If it was not a successful api request, returns an empty string
        if (Data.status_code == 200):
            usefulData = Data.__dict__
            weatherDataBytes = usefulData.get('_content')
            weatherDataDict = json.loads(weatherDataBytes.decode('utf-8'))
            return weatherDataDict
        else:
            return ""


# returns the usefule data to display for the api
def parseData(weatherData):
    if weatherData == "":
        return ""
    else:
        # things i want: temp, feels like, min temp, max temp, wind speed
        temp = weatherData['main']['temp']
        feels_like = weatherData['main']['feels_like']
        temp_min = weatherData['main']['temp_min']
        temp_max = weatherData['main']['temp_max']
        humidity = weatherData['main']['humidity']
        pressure = weatherData['main']['pressure']
        windSpeed = weatherData['wind']['speed']
        description = weatherData['weather'][0]['description']

        # create the dictionary to return
        myData = {'description': description, 'temp': temp,
                "feels_like": feels_like, 'temp_min': temp_min,
                'temp_max': temp_max, 'humidity': humidity,
                'pressure': pressure, 'wind_speed': windSpeed}

        # Description
        return myData


@app.route('/api/current_weather', methods=['GET'])
def user_api():

    ident_name = "KJFK"

    lat, lon = getGeoCoords(ident_name)

    if lat == "" or lon == "":
        return "<h1>Error: Please enter a valid ident code.</h1>"

    weatherData = getAirportWeather(lat, lon)

    if weatherData == "":
        return "<h1>Error: API request invalid."

    myData = parseData(weatherData)

    return jsonify(myData)


app.run()
