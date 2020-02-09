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
    pip3 install -r requirements.txt
- Enter your api key in th secret_.py file given
- To use the API:
    python3 app.py
- You will see this:
    * Serving Flask app "app" (lazy loading)
    * Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
    * Debug mode: on
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 173-747-444
- Go to the url shown and add the desired ident code where it says IDENT
    ?ident=IDENT



### References:
- https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
- https://www.dataquest.io/blog/python-api-tutorial/