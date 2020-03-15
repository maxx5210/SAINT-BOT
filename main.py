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
    import discord

tre = 1
TOKEN = "Njg4NDk0NzkzNDg3NDE3MzQ0.Xm5rtg.XhAjmGthtMLiGE_lkT2hooh9Qg4"

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
async def boucleTP1():
    while tre ==1:
        with open('coursTP1.json') as f:
            data = json.load(f)
        
        dateTimeObj = datetime.now()
        today = dateTimeObj.strftime("%Y-%m-%d-%H-%M")
        
        if today in data:
  
            groupeTP = data[today]['groupe']
            if groupeTP == "TP1":
                channel = client.get_channel(688688027912110088)
                await channel.send('Il est ' + data[today]['heure'] + '. Les ' + TP1 + ' ont ' + data[today]['nom'] +' avec ' + data[today]['prof'])
        await asyncio.sleep(60)

@client.event
async def boucleTP2():
    while tre ==1:
        with open('coursTP2.json') as f:
            data = json.load(f)
        
        dateTimeObj = datetime.now()
        today = dateTimeObj.strftime("%Y-%m-%d-%H-%M")
        
        if today in data:
                
            groupeTP = data[today]['groupe']
            if groupeTP == "TP2":
  
                channel = client.get_channel(688688027912110088)
                await channel.send('Il est ' + data[today]['heure'] + '. Les ' + TP2 + ' ont ' + data[today]['nom'] +' avec ' + data[today]['prof'])
        await asyncio.sleep(60)



@client.event
async def boucleTP3():
    while tre ==1:
        with open('coursTP3.json') as f:
            data = json.load(f)

        dateTimeObj = datetime.now()
        today = dateTimeObj.strftime("%Y-%m-%d-%H-%M")
        
        if today in data:
            groupeTP = data[today]['groupe']
            if groupeTP == "TP3":
                channel = client.get_channel(688688027912110088)
                await channel.send('Il est ' + data[today]['heure'] + '. Les ' + TP3 + ' ont ' + data[today]['nom'] +' avec ' + data[today]['prof'])
        await asyncio.sleep(60)



@client.event
async def boucleTP4():
    while tre == 1 :
        with open('coursTP4.json') as f:
            data = json.load(f)
        
        dateTimeObj = datetime.now()
        today = dateTimeObj.strftime("%Y-%m-%d-%H-%M")
        
        if today in data:
              
            groupeTP = data[today]['groupe']
            if groupeTP == "TP4":    
                channel = client.get_channel(688688027912110088)
                await channel.send('Il est ' + data[today]['heure'] + '. Les ' + TP4 + ' ont ' + data[today]['nom'] +' avec ' + data[today]['prof'])
        await asyncio.sleep(60)
    

client.loop.create_task(boucleTP1())

client.loop.create_task(boucleTP2())

client.loop.create_task(boucleTP3())

client.loop.create_task(boucleTP4())

client.run(TOKEN)


