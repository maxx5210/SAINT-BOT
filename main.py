import os

from time import sleep
from datetime  import datetime
import threading
import json
import asyncio




try:
    import pip
except ImportError as ee:
    os.system('python get-pip.py')


try:
    import discord
except ImportError as e:
    os.system('pip install -U discord')

tre = 1
TOKEN = "Njg4NDk0NzkzNDg3NDE3MzQ0.Xm4BLA.XnDQDmckJVdl0ed-cGhCgPsekVo"

GUILD = 'COMPUTING UNIVERSITY'

client = discord.Client()



@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break


    print(f'{client.user} has connected to' f' {guild.name} id: {guild.id}')


@client.event
async def on_message(message) :
    id = client.get_guild(618803263558385671)

    if message.content.find("!hello") != -1:
        await message.channel.send("hi")


@client.event
async def boucle():
    

    while tre ==1:
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
                
                # channel = client.fetch_channel(688688027912110088)
                channel = client.get_channel(688688027912110088)
                await channel.send('hello')
        await asyncio.sleep(3)
    # threading.Timer(10, lambda : boucle()).start()


client.loop.create_task(boucle())
client.run(TOKEN)


