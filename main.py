import os

from time import sleep
from datetime  import datetime
import threading
import json

try:
    import pip
except ImportError as ee:
    os.system('python get-pip.py')


try:
    import discord
except ImportError as e:
    os.system('pip install -U discord')



with open('cours copy.json') as f:
  data = json.load(f)

TOKEN = "Njg4NDk0NzkzNDg3NDE3MzQ0.Xm372Q.W34bbzj9wux9jmNJ1tghpmqWo9Y"

GUILD = 'COMPUTING UNIVERSITY'

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break


    print(f'{client.user} has connected to' f' {guild.name} id: {guild.id}')

    
    
    boucle()


def boucle():
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

    
    threading.Timer(30, lambda : boucle()).start()


client.run(TOKEN)

