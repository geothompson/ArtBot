import os
import sys

import discord
import request_chat

TOKEN = os.getenv('DISCORD_TOKEN')
if TOKEN == None:
    print("invalid discord API token")
    sys.exit("1")
intents = discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("ready")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("/generate"):
        input = message.content.replace("/generate", "")
        image_prompt = request_chat.get_image_prompt(input)
        await message.channel.send("generating " + message.content.replace("/generate",""))
        if image_prompt == None:
            await message.channel.send("gpt-3.5 API Error")
        else:
            await message.channel.send(image_prompt)
            image_url = request_chat.get_image_url(image_prompt)
            if image_url == None:
                await message.channel.send("DALL-E API Error")
            else:
                await message.channel.send(image_url)

client.run(TOKEN)
