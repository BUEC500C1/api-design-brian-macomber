'''
Brian Macomber - U25993688
References:
https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
'''

import csv
import flask
from flask import jsonify
import requests


def getGeoCoords(ident):
    with open('airports.csv', mode='r') as airports_csv:
        csv_reader = csv.reader(airports_csv, delimiter=',')
        for row in csv_reader:
            if ident == row[1]:
                return (row[4], row[5])


def getAirportData(lat, lon):
    params = {"lat": lat, "lon": lon}
    jsonData = requests.get("http://api.openweathermap.org/data/2.5/weather}", params=params)
    print(jsonData.status_code)

# app = flask.Flask(__name__)
# app.config["DEBUG"] = True


ident_name = "00AA"

lat, lon = getGeoCoords(ident_name)
getAirportData(lat, lon)


'''
# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


app.run()
'''
