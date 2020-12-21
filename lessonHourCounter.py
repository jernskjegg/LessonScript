#! python3

#HourCounter - A script to capture my lesson dates with the press of a button and export the amount of hours when needed.

import json, os, sys 
from datetime import datetime

date = datetime.now()
date = date.strftime("%d/%m/%Y %H:%M:%S")

addNew = [date]

def addStuff():
    if not os.path.isfile("counter.json"):
        with open("counter.json", mode="w") as json_file:
            json.dump([], json_file)
    with open("counter.json", mode="r") as json_file:
        existingList = json.load(json_file)
    with open("counter.json", mode="w+") as json_file:
        existingList.append(addNew)
        json.dump(existingList, json_file)
        return existingList

if len(sys.argv) == 2:
    arg = sys.argv[1]
    args = ["count", "hours", "time", "times", "multiply", "hour", "norsk"]
    if arg in args:
        with open("counter.json", mode="r") as json_file:
            cList = json.load(json_file)
        total = len(cList)*2
        print(f"You have had {total} hours of lessons. Check counter.json for dates." )
    else:
        print("Wrong arg passed.")
else:
    cList = addStuff()
