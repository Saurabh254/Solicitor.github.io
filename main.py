
from discord.ext import commands
import discord
from datetime import datetime

import pytz

token = "put token here"
channel__id = "int: put channel id"

bot = commands.Bot(command_prefix="s!")

IST = pytz.timezone('Asia/Kolkata')
IndianTime = datetime.now(IST)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Messages", url="https://google.com/"))


@bot.event
async def on_message(message):
    if not message.author.bot:
        if "saurabh" in (message.content.lower()).replace(":saurabh:", ""):
            channel = bot.get_channel(channel__id)

            embed = discord.Embed(
                title=f"Solicitor Headquarters!!!",
                color=16718362)

            embed.add_field(
                name="Message",
                value=f"```py\n{message.content[0:1000]}\n```",
                inline=False)

            embed.add_field(
                name="Author",
                value=f"```cpp\n{message.author}\n```",
                inline=True)

            embed.add_field(
                name="Ping",
                value=f"```py\n💚 {round(bot.latency * 1000)}ms\n```",
                inline=True)

            embed.add_field(
                name="Server Name",
                value=f"```py\n{message.guild.name}\n```",
                inline=True)

            embed.add_field(
                name="Channel",
                value=f"```py\n{message.channel}\n```",
                inline=True)

            embed.add_field(
                name="Message URL:",
                value=f"[Jump to message]({message.jump_url})",
                inline=False)

            embed.set_thumbnail(
                url="https://cdn.discordapp.com/avatars/932174184942026802/5b33de427fa67237c3dc0dd58c4dcd3d.png?size=4096")

            embed.set_footer(text=str(IndianTime.strftime('%d-%m-%Y %I:%M %p')),
                             icon_url="https://cdn.discordapp.com/attachments/941355481589485630/949221082076938310/pinpng.com-timer-png-723861.png")

            await channel.send(embed=embed)


bot.run(token)
