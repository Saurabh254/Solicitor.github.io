import asyncio
from email import message
from http import server
from logging import shutdown
from discord.ext import commands
import discord
bot = commands.Bot(command_prefix="s!")
shutdown = False
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Messages", url="https://google.com/"))

@bot.event
async def on_message(message):
    if message.author != bot.user:
        if "saurabh" in (message.content.lower()).remove(":saurabh:"):
            channel = bot.get_channel(941355481589485630)
            await channel.send(f"<@767758266155401226>\n```py\nMessage: {message.content}\n\nAuthor: {message.author}\n\nchannel: {message.channel}\n\nserver: {message.guild.name}\n```")
bot.run("OTMyMTc0MTg0OTQyMDI2ODAy.YePI3A.hndJ0Hqpbn6QJcMMkFSBD0leaYw")
