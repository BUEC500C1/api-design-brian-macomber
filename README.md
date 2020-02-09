# API Design

#### Brian Macomber 
#### EC500 - Building Software
#### Professor Osama Alshaykh


### Objectives:
- Develop an API and module that will get the current weather conditions from an airport
- Integrate Continuous Build Process to check if the software in each development stage passed the build process. 
- Integrate unit test and run the unit test in continuous integration process.

### Summary:
This API uses the ICAO code for each airport to return the current weather at the airport's location. Using the csv file in this repo, it searches for the geographic coordinates of the airport and uses these as parameters to call the OpenWeatherMapAPI to get the current weather. This API then returns a specific set of weather data as a JSON object.


### How to run:
- Clone the github repository to your computer
- Make sure the most recent version of python is installed
- On the command line run:
    `pip3 install -r requirements.txt`
- Enter your api key in th secret_.py file given
- To use the API:
    `python3 app.py`
- Got to the url `http://127.0.0.1:5000/api/current_weather` to get the default weather for Boston
- Go to the url `http://127.0.0.1:5000/api/current_weather?ident=IDENT` and add the desired ident code for an airport where it says IDENT


### References:
- https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
- https://www.dataquest.io/blog/python-api-tutorial/
- https://docs.python.org/3/library/csv.html
- https://openweathermap.org/current
