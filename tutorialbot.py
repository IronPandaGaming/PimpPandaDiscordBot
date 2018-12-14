import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os
import time
import random
from discord import Game

Client = discord.client
client = commands.Bot(command_prefix = '.')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Hunting Lolis..."))

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
    if ('nigger') in message.content:
       await client.delete_message(message)
    if ('niggers') in message.content:
       await client.delete_message(message)
    if message.content.startswith('.loli'):
        randomlist = ["Panda has a loli named Jenny","Panda has a loli named Rebecca","Panda has a loli named Emma","Panda has a loli named Sophia","Panda has a loli named Olivia"]
        await client.send_message(message.channel,(random.choice(randomlist)))

@client.command(pass_context=True)
async def clear(ctx, amount):
	channel = ctx,message,channel
	messages = []
	async for message in client.logs_from(channel, limit=int(amount)):
		messages.append(message)
	await client.delete_messages(messages)
	await client.say("Messages Deleted.")
        
client.run(os.getenv('TOKEN'))
