
from discord.ext import commands
import discord
from datetime import datetime
import re

token = "put ur token"
channel__id = "put channel id"

bot = commands.Bot(command_prefix="s!")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Messages", url="https://google.com/"))
    print("bot is ready!!!")


@bot.event
async def on_message(message):
    if not message.author.bot:
        msg = re.sub(
            '```| |\`|\~|\!|\@|\#|\$|\%|\^|\&|\*|\(|\)|\_|\+|\||\-|\=|\|\[|\]|\:|\;|\"|\'|\<|\>|\?|\,|\.|\{|\}|:saurabh:|:sau:|:saur:|\d+', '', message.content.lower())

        if "saurabh" in msg or "sau" in msg or "sarabh" in msg or 'surabh' in msg:
            ref_message = None
            reporting = bot.get_channel(channel__id)
            embed = discord.Embed(
                title=f"Solicitor Headquarters!!!",
                color=16718362)

            embed.add_field(
                name="Main Message",
                value=f"```py\n{(message.content[0:1000]).replace('```','')}\n```",
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

            if message.reference is not None:
                reference_channel = message.channel
                ref_message = await reference_channel.fetch_message(message.reference.message_id)

                embed.add_field(
                    name="Reference Message:",
                    value=f"```\n{(ref_message.content).replace('```','')}\n```",
                    inline=False,
                )

                embed.add_field(
                    name="Reference Author:",
                    value=f"```\n{ref_message.author}\n```",
                    inline=True,
                )

                embed.add_field(
                    name="Ref-Author's Nick:",
                    value=f"```\n{ref_message.author.display_name}\n```",
                    inline=True,
                )

            embed.add_field(
                name="Server Name",
                value=f"```py\n{message.guild.name}\n```",
                inline=False)

            embed.add_field(
                name="Channel",
                value=f"```py\n{message.channel}\n```",
                inline=False)

            embed.add_field(
                name="Main Message URL:",
                value=f"[Jump to message]({message.jump_url})",
                inline=True)
            if ref_message is not None:
                embed.add_field(
                    name="Ref Message URL:",
                    value=f"[Jump to message]({ref_message.jump_url})",
                    inline=True)

            embed.set_thumbnail(
                url=str(message.guild.icon_url))
            embed.timestamp = datetime.utcnow()

            embed.set_footer(text=f"Channel id : {message.channel.id}, Guild id: {message.guild.id}",
                             icon_url="https://cdn.discordapp.com/attachments/941355481589485630/949221082076938310/pinpng.com-timer-png-723861.png")

            await reporting.send(embed=embed)


bot.run(token)
