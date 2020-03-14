import os


try:
    import pip
except ImportError as ee:
    os.system('python get-pip.py')


try:
    import discord
except ImportError as e:
     pip.main(['install', 'discord'])

TOKEN = "Njg4NDk0NzkzNDg3NDE3MzQ0.Xm1JDg.OBLYPbcFA2SQMU8zr_p9amZ9Z58"

GUILD = 'COMPUTING UNIVERSITY'

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break


    print(f'{client.user} has connected to' f' {guild.name} id: {guild.id}')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

client.run(TOKEN)

