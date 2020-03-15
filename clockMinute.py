from time import sleep
from datetime  import datetime
import threading
import json

def boucle(message):
    
    with open('cours copy.json') as f:
    data = json.load(f)
    # today = date.today()
    dateTimeObj = datetime.now()
    today = dateTimeObj.strftime("%Y-%m-%d")
    
    hours = dateTimeObj.strftime("%H:%M")
    # print(today)
    # print (compteur)
    # print(data.get(today, "null"))
    # print(hours)
    if today in data:
        # print(data[today]['groupe'])

        heureCours = data[today]['heure']
        if hours == heureCours:
            # print("true")
            print(data[today]['nom'])
            print(data[today]['prof'])
            print(data[today]['heure'])
            print(data[today]['groupe'])
            await message.channel.send('Hi!')



    threading.Timer(30, lambda : boucle()).start()

boucle(message)