import json
import flask
from flask import jsonify
from flask import request
import requests
from secret_ import api_key
from getGeoCoords import getGeoCoords

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# using the latitude and longitude, the current weather of that airport is returned
def getAirportWeather(lat, lon):
    if (lat == "") or (lon == ""):
        return ""
    else:
        # api call
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


# returns the usefule data to display from the api response
def parseData(weatherData):
    if weatherData == "":
        return ""
    else:
        # Elements to parse from the data -
        temp = round(weatherData['main']['temp'] - 273.15) * (9 / 5) + 32  # converts from kelvin to fahernheit
        feels_like = round(weatherData['main']['feels_like'] - 273.15) * (9 / 5) + 32
        temp_min = round(weatherData['main']['temp_min'] - 273.15) * (9 / 5) + 32
        temp_max = round(weatherData['main']['temp_max'] - 273.15) * (9 / 5) + 32
        humidity = weatherData['main']['humidity']
        pressure = weatherData['main']['pressure']
        windSpeed = weatherData['wind']['speed'] * 2.237  # converts to miles per hour
        description = weatherData['weather'][0]['description']

        # known units of retutned data, so the user knows how to use the data
        units = {'temperature': 'F', 'pressure': 'hPa',
                'wind_speed': 'mph'}

        # create data structure of data to return to the user
        myData = {'weather': {'description': description, 'temp': temp,
                "feels_like": feels_like, 'temp_min': temp_min,
                'temp_max': temp_max, 'humidity': humidity,
                'pressure': pressure, 'wind_speed': windSpeed},
                'units': units}

        return myData


@app.route('/api/current_weather', methods=['GET'])
def user_api():

    if 'ident' in request.args:
        ident_name = request.args['ident']  # looks from ident in url after "?ident="
    else:
        ident_name = "KBOS"  # when the user has not specificed an ident, it defaults to Boston

    lat, lon = getGeoCoords(ident_name)

    if lat == "" or lon == "":
        return "<h1>Error: Please enter a valid ident code.</h1>"

    # calling the api and returning a dictionary of the reponse
    weatherData = getAirportWeather(lat, lon)

    if weatherData == "":
        return "<h1>Error: API request invalid."

    # getting the useful data and creating a data structure of my api's response data
    myData = parseData(weatherData)

    return jsonify(myData)


app.run()
