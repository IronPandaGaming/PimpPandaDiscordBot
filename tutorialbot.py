import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os
import time
import random
from discord import Game

client = commands.Bot(command_prefix = '.')
client = discord.Client()

chat_filter = ["NIGGER", "NIGGERS"]
bypass_list = []

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Loli Hunter..."))

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name="Pandamoniums")
    await client.add_roles(member, role)

@client.event
async def on_message(message):
    if message.content == '.sadpanda':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/523120827697463298/523120846097612810/sadpanda.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == '.nani':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/523120827697463298/523335385833799733/nanithefuck.JPG')
        await client.send_message(message.channel, embed=em)
        
@client.event
async def on_message(message):
    contents = message.content.split(" ")
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "Hey! You're not allowed to use that word here!")
                except discord.errors.NotFound:
                    return
        
    if message.content.startswith('.loli'):
       randomlist = ["Panda has a loli named Irma","Panda has a loli named Jenny","Panda has a loli named Rebecca","Panda has a loli named Emma","Panda has a loli named Sophia","Panda has a loli named Olivia"]
       await client.send_message(message.channel,(random.choice(randomlist)))
        
    if message.content == '.irma':
        await client.send_message(message.channel,"Oh... Panda's favorite loli?") 
        
@client.command (pass_context=True)
async def clear(ctx, amount=1):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) +1):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Messages Deleted.')
    
client.run(os.getenv('TOKEN'))
