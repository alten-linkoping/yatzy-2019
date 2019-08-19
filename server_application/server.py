from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def root():
    return json.dumps({
        "dice":[4,2,6,4,9]
    })