from flask import Flask
import json
import random
from collections import Counter
import rules
import example_dice

app = Flask(__name__)


@app.route("/")
def root():
    #dice = rules.roll_dice()

    return example_dice.points()