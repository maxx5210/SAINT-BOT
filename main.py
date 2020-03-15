import os


try:
    import pip
except ImportError as ee:
    os.system('python get-pip.py')


try:
    import discord
except ImportError as e:
    os.system('pip install -U discord')

TOKEN = "Njg4NDk0NzkzNDg3NDE3MzQ0.Xm1z-Q.CAIzuoBGB5ZkGwYogLuesIdVVmE"

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

