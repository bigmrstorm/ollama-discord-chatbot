import discord
from discord import Intents
import os
import subprocess
import threading
import asyncio

intents = Intents.default()
client = discord.Client(intents=intents)

def run_ollama():
    subprocess.run(["start", "cmd", "/k", "ollama run modelname"], shell=True)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    threading.Thread(target=run_ollama).start()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user in message.mentions: 
        user_message = f"{message.author.name}: {message.content}"
        print(user_message)
        process = subprocess.Popen(["ollama", "run", "modelname"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        stdout, stderr = process.communicate(input=user_message.encode())
        response = stdout.decode()
        async with message.channel.typing():
            await asyncio.sleep(3) 
            bot_message = await message.reply(response, mention_author=True) 
            await bot_message.add_reaction('🔄') 

@client.event
async def on_reaction_add(reaction, user):
    if user == client.user:
        return

    if reaction.emoji == '🔄' and reaction.message.author == client.user:
        original_message = reaction.message.reference.resolved
        if original_message.author != client.user:
            user_message = f"{original_message.author.name}: {original_message.content}"
            print(user_message) 
            process = subprocess.Popen(["ollama", "run", "modelname"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            stdout, stderr = process.communicate(input=user_message.encode())
            response = stdout.decode()
            async with reaction.message.channel.typing():
                await asyncio.sleep(2) 
                await reaction.message.edit(content=response)


client.run('YOUR_BOT_TOKEN')
