from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return"<p>Hello, World!</p>"

# https://flask.palletsprojects.com/en/2.3.x/quickstart/