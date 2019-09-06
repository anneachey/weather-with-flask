from flask import Flask
app = Flask(__name__)

# Index method - entry point into the application
@app.route("/")
def hello():
    return "Hello world!"


# If the main route is requested and entered, run the app.
if __name__ == '__main__':
    app.run()
