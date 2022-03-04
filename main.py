
from discord.ext import commands
import discord
from decouple import config
import datetime

token = config("Token")
channelid = int(config("channel_id"))
bot = commands.Bot(command_prefix="s!")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Messages", url="https://google.com/"))


@bot.event
async def on_message(message):
    if message.author != bot.user:
        if "saurabh" in (message.content.lower()).replace(":saurabh:", ""):
            channel = bot.get_channel(channelid)
            embed = discord.Embed(title=f"Solicitor Headquarters!!!", color=16718362)
            embed.add_field(name="Message", value=f"```py\n{message.content[0:1000]}\n```", inline=False)
            embed.add_field(name="Author", value=f"```cpp\n{message.author}\n```", inline=True)
            embed.add_field(name="Ping", value=f"```py\n💚 {round(bot.latency * 1000)}ms\n```", inline=True)
            embed.add_field(name="Server Name", value=f"```py\n{message.guild.name}\n```", inline=True)
            embed.add_field(name="Channel", value=f"```py\n{message.channel}\n```", inline=True)
            embed.add_field(name="Message url:", value=f"[Jump to message]({message.jump_url})", inline=False)
            embed.set_footer(text=str(datetime.datetime.now())[0:-7], icon_url="https://cdn.discordapp.com/attachments/941355481589485630/949172446387372043/images.jpg")
            await channel.send(embed=embed)
            

bot.run(token)
