from flask import Flask,request, jsonify
import json
import random
from collections import Counter
import rules
import example_dice
import struct

app = Flask(__name__)


@app.route("/")
def root():
    #dice = rules.roll_dice()
    #json = request.json
   # return json

    return example_dice.points()

@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    data = request.data
    my_dice = []
    for x in range (0,len(data)):
            my_dice.append(data[x])



    print(my_dice)
    

    return json.dumps({
        "dice": sorted(my_dice),
        "upper": [{
            "SmallStraight": rules.SmallStraight(my_dice),
            "BigStraight": rules.BigStraight(my_dice),
            "OnePair": rules.OnePair(my_dice),
            "TwoPairs": rules.TwoPairs(my_dice),
            "ThreeOf": rules.ThreeOf(my_dice),
            "four of": rules.FourOf(my_dice),
            "yatzy!": rules.yatzy(my_dice),
            "full house!": rules.FullHouse(my_dice),
            "chance": rules.chance(my_dice)
        }],
        "lower": [{
            "ones": rules.LowerSection(my_dice, 1),
            "twos": rules.LowerSection(my_dice, 2),
            "threes": rules.LowerSection(my_dice, 3),
            "fours": rules.LowerSection(my_dice, 4),
            "fives": rules.LowerSection(my_dice, 5),
            "sixes": rules.LowerSection(my_dice, 6)

        }]
    }
    )