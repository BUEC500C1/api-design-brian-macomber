import csv


# using the ident code of an airport, get the geographical coordinates
def getGeoCoords(ident):
    with open('airports.csv', mode='r') as airports_csv:

        csv_reader = csv.reader(airports_csv, delimiter=',')

        for row in csv_reader:
            if ident == row[1]:
                return (row[4], row[5])

    return ("", "")
