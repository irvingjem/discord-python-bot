# bot.py
import os
import requests

URL = ""
page = request.get(URL)

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'this bot sucks' in message.content.lower():   
        await message.channel.send('<:Smadge:1007789204664754227>') 

    if 'games this month' in message.content.lower():
        await message.channel.send(requests)



client.run(TOKEN)

