#!/bin/python3
import discord, json, pyfiglet ,time, requests
from discord.ext import commands
ClientName = "Slatt Haxx Bv1.82"
ClientVersion = "Beta Version 1.82"
ClientAsciiTxt = pyfiglet.figlet_format(ClientName)
token = "Mzc0OTk4NTc3MzAwMzczNTA0.X9_HRw.3qefTSEv8uSdUkFzwLJI4F_9m6Q"
headers = { "Authorization": f"{token}"}
bot = commands.Bot(command_prefix="$",self_bot=True)
bot.remove_command(name="help")

def timestamp():
   return time.strftime("%H:%M:%S", time.localtime())

def channel_name(channel):
    if hasattr(channel,"name"):
        return (f'#{channel.name}')
    else:
        return(f'@{channel.recipient.name}')

def help_embed(ctx):
    embed = {
        "tts": False,
        "embed": {
            "title": f"{ClientName}",
            "url": "https://www.youtube.com/watch?v=lqrVRKlVLXM",
            "description": f"*{ctx.message.author.name}'s Discord Self Bot 🤫*",
            "footer":{
            "text": f"{ClientVersion}",
            "icon_url": "https://cdn.discordapp.com/embed/avatars/0.png"
            },
            "author": {
                "name" : f"Created by retracee",
                "url" : "https://github.com/retracee",
                "icon_url" : "https://avatars.githubusercontent.com/u/78283359?v=4",
            },
            "thumbnail":{
                "url": f"{ctx.message.author.avatar_url}",
            },
            "fields" : [
                {
                "name": "***Troll***   ",
                "value": "**$ghostping <@user> <num>** \n Ghostpings User \n **$spam <num>: <msg>** \n Spams Message"
                },
                {
                "name": "***Utils***",
                "value": "**$cmds** \n Show Commands \n **$delete <num>** \n Delete Msgs \n **$purge** \n Purges Sent Messages in Channel \n **$av <@user>** \n Shows User's Avatar\n **$stats <@user>** \n Shows User's Stats (Server Only)",
                },
                {
                "name": "***Misc***",
                "value": "**$ascii** \n Show Client Logo Ascii",
                },
                ]
        }
    }
    return embed

def avatar_embed(user):
    embed = {
        "tts": False,
        "embed":{
            "title": f"{user.name}'s Avatar",
            "image":{
                "url": f"{user.avatar_url}"
            }
        }
    }
    return embed
def stats_embed(ctx,user,msgs,roles):
    embed = {
        "tts": False,
        "embed":{
            "description": f"**✉️ Messages in {channel_name(ctx.channel)}:** *{msgs}* \n **🚪Joined the Server at:** *{user.joined_at.strftime('%b %d, %Y')}* \n **🔒 Account Created at:** *{user.created_at.strftime('%b %d, %Y')}* \n **📜Roles:** *{roles}*",
            "author":{
                "name": f"{user.name}'s Stats",
                "icon_url": f"{user.avatar_url}",
            },
        },
    }
    return embed

@bot.event
async def on_ready():
    print(f"{ClientAsciiTxt} Created by retracee (https://github.com/retracee)")
    print(f"\n          Welcome back, {bot.user.name}! Use $cmds for help.\n")  
@bot.command()
async def ascii(ctx):
    await ctx.message.delete()
    await ctx.send(f"```{ClientAsciiTxt}```")

@bot.command()
async def cmds(ctx):
    requests.post(f"https://discord.com/api/v8/channels/{ctx.channel.id}/messages", headers=headers, json=help_embed(ctx))
    print(f"[{timestamp()}]: Sent $cmds in {channel_name(ctx.channel)}")

@bot.command() # only works in servers for now
async def av(ctx, *, user: discord.Member = None):
    if not user:
        user = ctx.message.author
    requests.post(f"https://discord.com/api/v8/channels/{ctx.channel.id}/messages", headers=headers, json=avatar_embed(user))
    print(f"{timestamp()}]: Sending {user.name}'s avatar in {channel_name(ctx.channel)}")

@bot.command() # only works in servers for now
async def stats(ctx, *, user: discord.Member = None):
    msgs=int(0)
    if not user:
        user = ctx.message.author
    for message in await ctx.message.channel.history(limit=None).flatten():
        if message.author == user:
            msgs=msgs+1
    for x in user.roles:
        roles = x.name
    requests.post(f"https://discord.com/api/v8/channels/{ctx.channel.id}/messages", headers=headers, json=stats_embed(ctx,user,msgs,roles))
    print(f"[{timestamp()}]: Sending {user.name}'s stats in {channel_name(ctx.channel)}")

@bot.command()
async def figlet(ctx, *, args):
    await ctx.message.delete()
    text = pyfiglet.figlet_format(args)
    await ctx.send(f'```{text}```')
    print(f"""[{timestamp()}]: Sending figlet "{args}" in {channel_name(ctx.message.channel)}: {text}""")

@bot.command()
async def purge(ctx):
    a = int(0) 
    b = int(0)
    await ctx.message.delete()
    for message in await ctx.message.channel.history(limit = None).flatten(): 
        if message.author == ctx.message.author:
            a=a+1
    print(f"[{timestamp()}]: Purging {channel_name(ctx.channel)}.. {a} messages found.")
    for message in await ctx.message.channel.history(limit = None).flatten():
        if message.author == ctx.message.author:
            b=b+1 
            await message.delete()
            print(f"""[{timestamp()}]: ({str(b)}/{str(a)}) Deleting "{message.content}" at {message.created_at} in {channel_name(message.channel)}""")
    print(f"[{timestamp()}]: Purge Complete. {b} Messages Deleted!")


@bot.command()
async def delete(ctx, *, args):
    i = int(0)
    await ctx.message.delete()
    for message in await ctx.message.channel.history(limit = 200).flatten():
        if message.author == ctx.message.author:
            i=i+1
            if i<int(args)+1:
                await message.delete()
                print(f"""[{timestamp()}]: ({str(i)}/{args}) Deleting "{message.content}" at {message.created_at} in {channel_name(message.channel)}""")

@bot.command()
async def spam(ctx, *, args):
    rargs = args.split(": ")
    await ctx.message.delete()
    for x in range(int(rargs[0])):
       await ctx.send(rargs[1])
       print(f'''[{timestamp()}]: ({x+1}/{rargs[0]}) Spamming "{rargs[1]}" in {channel_name(ctx.channel)}''')

@bot.command()
async def ghostping(ctx, *, args):
    rargs = args.split(" ")
    await ctx.message.delete()
    for x in range(int(rargs[1])):
        await ctx.send(f"{rargs[0]}")
        print(f"[{timestamp()}]: ({x+1}/{rargs[1]}) Ghost Pinging {rargs[0]}")
        for message in await ctx.message.channel.history(limit=int(5)).flatten():
            if message.author == ctx.message.author:
                if message.content == rargs[0]:
                    await message.delete()
    print(f"[{timestamp()}]: Ghost Ping Complete. Pinged {rargs[0]} {rargs[1]} times!")

bot.run(token,bot=False)
