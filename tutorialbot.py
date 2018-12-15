import discord
from discord.ext import commands

TOKEN = 'NTIyNzI4MDA1OTk1NDYyNjkx.DvZ2GQ.z1lzc_M24CCDmAllBaf50zC0g8I'

@client.event
async def on_ready():
    print ('Bot is ready.')

client.run(TOKEN)
