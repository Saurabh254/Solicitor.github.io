
from discord.ext import commands
import discord
from datetime import datetime


token = "put token here"
channel__id = "int: put channel id"

bot = commands.Bot(command_prefix="s!")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Messages", url="https://google.com/"))
    print("bot is ready!!!")

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
                name="Author Username",
                value=f"```cpp\n{message.author}\n```",
                inline=True)

            embed.add_field(
                name="Author Nickname",
                value=f"```cpp\n{message.author.display_name}\n```",
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
                url=str(message.guild.icon_url))
            embed.timestamp = datetime.utcnow()
            
            embed.set_footer(
                             icon_url="https://cdn.discordapp.com/attachments/941355481589485630/949221082076938310/pinpng.com-timer-png-723861.png")

            await channel.send(embed=embed)


bot.run(token)
