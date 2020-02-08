'''
Brian Macomber - U25993688
References:
https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
https://www.dataquest.io/blog/python-api-tutorial/
'''

import csv
import json
import flask
# from flask import jsonify
import requests
from secret import api_key

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def getGeoCoords(ident):
    with open('airports.csv', mode='r') as airports_csv:
        csv_reader = csv.reader(airports_csv, delimiter=',')
        for row in csv_reader:
            if ident == row[1]:
                return (row[4], row[5])
    return ("", "")


def getAirportData(lat, lon):
    params = {"lat": lat, "lon": lon, "appid": api_key}
    url = "http://api.openweathermap.org/data/2.5/weather"
    Data = requests.get(url, params=params)

    if (Data.status_code == 200):
        return Data.__dict__
    else:
        return ""


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


data = getAirportData(lat, lon)
# if data is "":

(temp, feels_liek, minTemp, maxTemp) = parseData(data)


# @app.route('/', methods=['GET'])
# def home():
#     return "<h1>Yonk</h1><p>This site is a prototype API for giving weather data for a specific airport.</p>"


# @app.route('/data/all', methods=['GET'])
# def api_all():
#     return jsonify(data)


# app.run()
