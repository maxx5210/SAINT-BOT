#created by @Makusu5210, @glowning7 and @Maxence_Jung
import os

from time import sleep
from datetime  import datetime

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

try:
    import mysql.connector
except ImportError as e:
    os.system('pip install mysql-connector')
    import mysql.connector


mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="bot"
)

tre = 1
TOKEN = "Njg4NDk0NzkzNDg3NDE3MzQ0.Xm-EUg.13zkOO12TAj6uvoisZ1boBHsLhQ"

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

        dateCours=""
        cours=""
        prof=""
        heure=""
        groupe=""

        dateTimeObj = datetime.now()
        today = dateTimeObj.strftime("%Y-%m-%d-%H-%M")

        #BASE DE DONNEES
        mycursor = mydb.cursor()

        mycursor.execute(f"SELECT DISTINCT * FROM saintbot WHERE date='{today}' AND groupe='TP1'")

        print(today)
        myresult = mycursor.fetchall()
        for row in myresult:
            dateCours = row[0]
            cours = row[1]
            prof = row[2]
            heure = row[3]
            groupe = row[4]

        if today == dateCours:
  
            groupeTP = groupe
            if groupeTP == "TP1":
                channel = client.get_channel(688688027912110088)
                await channel.send('Il est ' + heure + '. Les ' + TP1 + ' ont ' + cours+' avec ' + prof)
        await asyncio.sleep(60)

@client.event
async def boucleTP2():
    while tre == 1:

        dateCours = ""
        cours = ""
        prof = ""
        heure = ""
        groupe = ""

        dateTimeObj = datetime.now()
        today = dateTimeObj.strftime("%Y-%m-%d-%H-%M")

        #BASE DE DONNEES
        mycursor = mydb.cursor()

        mycursor.execute(
            f"SELECT DISTINCT * FROM saintbot WHERE date='{today}' AND groupe='TP2'")

        print(today)
        myresult = mycursor.fetchall()
        for row in myresult:
            dateCours = row[0]
            cours = row[1]
            prof = row[2]
            heure = row[3]
            groupe = row[4]

        if today == dateCours:

            groupeTP = groupe
            if groupeTP == "TP2":
                channel = client.get_channel(688688027912110088)
                await channel.send('Il est ' + heure + '. Les ' + TP2 + ' ont ' + cours+' avec ' + prof)
        await asyncio.sleep(60)



@client.event
async def boucleTP3():
    while tre == 1:

        dateCours = ""
        cours = ""
        prof = ""
        heure = ""
        groupe = ""

        dateTimeObj = datetime.now()
        today = dateTimeObj.strftime("%Y-%m-%d-%H-%M")

        #BASE DE DONNEES
        mycursor = mydb.cursor()

        mycursor.execute(
            f"SELECT DISTINCT * FROM saintbot WHERE date='{today}' AND groupe='TP3'")

        print(today)
        myresult = mycursor.fetchall()
        for row in myresult:
            dateCours = row[0]
            cours = row[1]
            prof = row[2]
            heure = row[3]
            groupe = row[4]

        if today == dateCours:

            groupeTP = groupe
            if groupeTP == "TP3":
                channel = client.get_channel(688688027912110088)
                await channel.send('Il est ' + heure + '. Les ' + TP3 + ' ont ' + cours+' avec ' + prof)
        await asyncio.sleep(60)



@client.event
async def boucleTP4():
    while tre == 1:

        dateCours = ""
        cours = ""
        prof = ""
        heure = ""
        groupe = ""

        dateTimeObj = datetime.now()
        today = dateTimeObj.strftime("%Y-%m-%d-%H-%M")

        #BASE DE DONNEES
        mycursor = mydb.cursor()

        mycursor.execute(
            f"SELECT DISTINCT * FROM saintbot WHERE date='{today}' AND groupe='TP4'")

        print(today)
        myresult = mycursor.fetchall()
        for row in myresult:
            dateCours = row[0]
            cours = row[1]
            prof = row[2]
            heure = row[3]
            groupe = row[4]

        if today == dateCours:
            groupeTP = groupe
            if groupeTP == "TP4":
                channel = client.get_channel(688688027912110088)
                await channel.send('Il est ' + heure + '. Les ' + TP4 + ' ont ' + cours+' avec ' + prof)
        await asyncio.sleep(60)


client.loop.create_task(boucleTP1())

client.loop.create_task(boucleTP2())

client.loop.create_task(boucleTP3())

client.loop.create_task(boucleTP4())

client.run(TOKEN)


