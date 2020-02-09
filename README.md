# API Design

#### Brian Macomber 
#### EC500 - Building Software
#### Professor Osama Alshaykh


### Objectives:
- Develop an API and module that will get the current weather conditions from an airport
- Integrate Continuous Build Process to check if the software in each development stage passed the build process. 
- Integrate unit test and run the unit test in continuous integration process.

### Summary:


### How to run:
- Clone the github repository to your computer
- Make sure te most recent version of python is installed
- On the command line run:
    `pip3 install -r requirements.txt`
- Enter your api key in th secret_.py file given
- To use the API:
    `python3 app.py`
- Got to the url `http://127.0.0.1:5000` to get the default weather for Boston
- Go to the url `http://127.0.0.1:5000?ident=IDENT` and add the desired ident code for an airport where it says IDENT:


### References:
- https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
- https://www.dataquest.io/blog/python-api-tutorial/