#created by @Makusu5210, @glowning7 and @Maxence_Jung
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
TOKEN = "Njg4NDk0NzkzNDg3NDE3MzQ0.Xm4Y3w.kNmoLx08CCitZCmRk-84H82Fl7o"

GUILD = 'COMPUTING UNIVERSITY'

TP1 = '<@&647065897516924949>'
TP2 = '<@&647066080094847021>'
TP3 = '<@&647066128027222027>'
TP4 = '<@&647066184478490665>'


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
                
                print(data[today]['nom'])
                print(data[today]['prof'])
                print(data[today]['heure'])
                print(data[today]['groupe'])
                
                
                if data[today]['groupe'] == "TP1":
                    grp = TP1

                if data[today]['groupe'] == "TP2":
                    grp = TP2

                if data[today]['groupe'] == "TP3":
                    grp = TP3

                if data[today]['groupe'] == "TP4":
                    grp = TP4


                
                channel = client.get_channel(688688027912110088)
                await channel.send('Il est ' + data[today]['heure'] + '. Les ' + grp + ' ont ' + data[today]['nom'] +' avec ' + data[today]['prof'])
        await asyncio.sleep(60)
    


client.loop.create_task(boucle())
client.run(TOKEN)


