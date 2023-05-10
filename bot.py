import os

import discord
import request_chat

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("yep")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("/generate"):
        input = message.content.replace("/generate", "")
        output = request_chat.get_api_response(input)
        await message.channel.send("generating " + message.content.replace("/generate",""))
        await message.channel.send(output)

client.run(TOKEN)
