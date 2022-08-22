# bot.py
import os
import requests

URL = ""
page = request.get(URL)

import discord
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='!')
@bot.command (name='help', help='list of helpful stuff')

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

   # if 'games this month' in message.content.lower():
    #    await message.channel.send(requests)

@client.event
async def on_message

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hello! {member.name}, welcome to the Discord server'
    )

   # handling exceptions with the bot
   #  elif message.content == 'raise-exception':
       #raise discord.DiscordException


client.run(TOKEN)

