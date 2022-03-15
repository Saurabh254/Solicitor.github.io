
from discord.ext import commands, tasks
import discord
from datetime import datetime
import re

from matplotlib.pyplot import title


token = "put your token"
channel__id = 'channel id'


bot = commands.Bot(command_prefix=["Plz ", 'plz '])

message_deleted = {}
bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Messages", url="https://google.com/"))
    cleanup.start()
    print("bot is ready!!!")


@bot.event
async def on_message(message):
    if not message.author.bot:
        msg = re.sub(
            '```| |:saurabh:|:sau:|:saur:|\`|\~|\!|\@|\#|\$|\%|\^|\&|\*|\(|\)|\_|\+|\||\-|\=|\|\[|\]|\:|\;|\"|\'|\<|\>|\?|\,|\.|\{|\}|\d+', '', message.content.lower())

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
    await bot.process_commands(message)


@bot.event
async def on_message_delete(message):
    if message.guild.id not in message_deleted:
        message_deleted[message.guild.id] = []
    message_deleted_list = message_deleted[message.guild.id]
    message_deleted_list = [(message, datetime.utcnow(),  message.attachments[0].url if message.attachments != [] else None)
                            ] + message_deleted_list
    message_deleted_list.pop() if len(message_deleted) >= 6 else message_deleted_list
    message_deleted[message.guild.id] = message_deleted_list


@bot.command(name='snipe')
async def snipe(ctx, number: int = 1):
    if ctx.guild.id not in message_deleted:
        message_deleted[ctx.guild.id] = []
    if not 0 <= number < 6:
        await ctx.reply("Messages can be snipped in range 1, 6")
    else:
        if len(message_deleted[ctx.guild.id]) >= number:
            # slicing to get the indexed message
            message, timestp, attachment = message_deleted[ctx.guild.id][number-1]

            # Embeds  title
            embed = discord.Embed(
                color=16718362)
            messageCont = re.sub("\`", "", message.content)
            # Embed Message
            embed.add_field(name='Snipe Message: ',
                            value= f'```\n { messageCont if len(messageCont) != 0 else "Invalid format"}\n```' if attachment is None else f'{messageCont}\u200b',
                            inline=False)
            embed.set_author(
                name=f"{message.author} ({message.author.name})", icon_url=message.author.avatar_url)
            # Embed footer to display about author
            embed.set_footer(
                text=f"Deleted in #{message.channel.name}",
                icon_url=str(message.guild.icon_url))
            if attachment is not None:
                embed.set_image(url=attachment)
            # Embed timestamp to get the time stamp of the deleted message
            embed.timestamp = timestp
            await ctx.send(embed=embed)

        else:
            await ctx.reply("Messages haven't been logged till there")


@bot.command(name='help')
async def help(ctx):
    embed = discord.Embed(title=f'Solicitor Help Panel',
                          color=16718362)
    embed.add_field(name='Commands',
                    value='Name: **snipe** \n\n**Usage:** \n```Plz snipe [index]\n```\n\n**Index** should be in range(1,10)\n\n **Examples:** \n```\nPlz snipe 4 \nPlz snipe\n```\n\n **Use Prefix\'s:**  **Plz** or **plz**',
                    inline=False)
    embed.set_thumbnail(
        url=str(ctx.guild.icon_url))
    embed.timestamp = datetime.utcnow()

    embed.set_footer(text=f'Hii! {ctx.author.name}',
                     icon_url="https://cdn.discordapp.com/attachments/941355481589485630/949221082076938310/pinpng.com-timer-png-723861.png")

    await ctx.reply(embed=embed)


message_edited = {}


@bot.event
async def on_message_edit(message_before, message_after):
    if message_before.guild.id not in message_edited:
        message_edited[message_before.guild.id] = []
    message_edited_list = message_edited[message_before.guild.id]
    message_edited_list = [
        (message_before, message_after, datetime.utcnow())] + message_edited_list
    message_edited_list.pop() if len(message_edited_list) >= 6 else message_edited_list
    message_edited[message_before.guild.id] = message_edited_list


@bot.command(name='esnipe')
async def esnipe(ctx, index: int = 1, *_):
    if not 0 < index < 6:
        await ctx.reply("Message can be esniped in range of (1,6)")
    else:
        if ctx.guild.id not in message_edited:
            message_edited[ctx.guild.id] = []
        if len(message_edited[ctx.guild.id]) >= index:
            message_before, message_after, timestp = message_edited[ctx.guild.id][index-1]

            embed = discord.Embed(color=16718362)

            embed.add_field(name="Original Message:",
                            value=f'```\n{message_before.content}\n```',
                            inline=False)

            embed.add_field(name="Edited Message:",
                            value=f'```\n{message_after.content}\n```',
                            inline=False)

            embed.timestamp = timestp

            embed.set_footer(
                text=f"Edited in #{message_before.channel.name}",
                icon_url=str(ctx.guild.icon_url))
            embed.set_author(
                name=f"{message_before.author} ({message_before.author.name})", icon_url=message_before.author.avatar_url)
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("Messages haven't been logged till there")


# tasks to clean up dicts
@tasks.loop(seconds=20)
async def cleanup():
    print("Cleanup Initiated")
    for i in message_edited:
        edit_list = message_edited[i]
        edit_list.pop() if len(edit_list) > 1 else edit_list
        message_edited[i] = edit_list
    for i in message_deleted:
        delete_list = message_deleted[i]
        delete_list.pop() if len(delete_list) > 1 else delete_list
        message_edited[i] = delete_list


bot.run(token)
