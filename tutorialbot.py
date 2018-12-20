import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os
import random
from discord import Game

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Powering... UP!'))
    print ('Bot is ready.')

@client.command(pass_context=True)
async def clear(ctx, amount = 5):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Messages Deleted.')

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name="Pandamoniums")
    await client.add_roles(member, role)

@client.event
async def on_message(message):
    if message.content == '.sadpanda':
        em = discord.Embed(description='')
        em.set_image(url='https://media.discordapp.net/attachments/523120827697463298/523120846097612810/sadpanda.jpg')
        await client.send_message(message.channel, embed=em)
    if message.content == '.nani':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/523120827697463298/523335385833799733/nanithefuck.JPG')
        await client.send_message(message.channel, embed=em)
    if message.content == '.reverse':
        em = discord.Embed(description='')
        em.set_image(url='https://cdn.discordapp.com/attachments/189078483865960448/523672198754467841/3WDcYbV.png')
        await client.send_message(message.channel, embed=em)
        
    if ('nigger') in message.content:
       await client.delete_message(message)
       await client.send_message(message.channel, "Hey! You're not allowed to use that word here!")
    if ('Nigger') in message.content:
       await client.delete_message(message)
       await client.send_message(message.channel, "Hey! You're not allowed to use that word here!")
    if ('niggers') in message.content:
       await client.delete_message(message)
       await client.send_message(message.channel, "Hey! You're not allowed to use that word here!")                                 
    if ('Niggers') in message.content:
       await client.delete_message(message)
       await client.send_message(message.channel, "Hey! You're not allowed to use that word here!")                                

    if message.content.startswith('.loli'):
       randomlist = ["Panda has a loli named Irma","Panda has a loli named Jenny","Panda has a loli named Rebecca","Panda has a loli named Emma","Panda has a loli named Sophia","Panda has a loli named Olivia"]
       await client.send_message(message.channel,(random.choice(randomlist)))
       
    if message.content == '.irma':
       await client.send_message(message.channel,"Panda's favorite Loli?")
    if message.content == '.vanessa':
       await client.send_message(message.channel,"@ⒷⓁⓄⓄⒹⓎ💜ⓋⒶⓃⒺⓈⓈⒶ")

client.run(os.getenv('TOKEN'))
