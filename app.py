import os
from flask import Flask

app = Flask(__name__)
# Get the ennvironment we are currently on by loading the APP_SETTINGS environment variable
app.config.from_object(os.environ['APP_SETTINGS'])


# Index method - entry point into the application
@app.route("/")
def hello():
    return "Hello world!"


# If the main route is requested and entered, run the app.
if __name__ == '__main__':
    app.run()
