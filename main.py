import discord
import json
from discord.ext import commands
import os
from keep_alive import keep_alive
from dotenv import load_dotenv
import random

#bot init stuff
intents = discord.Intents.all()
client = commands.Bot(command_prefix=['c', 'C'],
                      intents=intents,
                      case_insensitive=True)
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game('chelp'))
    print('Bot is ready')


#give role to dudes
@client.event
async def on_member_join(member):
    channel = client.get_channel(871632953757802511)
    id = f"<@{member.id}>"
    await channel.send("Bonjour, %s" % id)
    role = discord.utils.get(member.guild.roles, name="not mod")
    await member.add_roles(role)


#commands
@client.command()
async def help(ctx):
    embed = discord.Embed(title="Help", color=0x00ffb7)
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/avatars/871638624716857366/d4acd269c443690c9378cf7c0fe3fce7.webp?size=1024"
    )
    embed.set_footer(text=f"Requested by: {ctx.message.author.name}",
                     icon_url=f"{ctx.message.author.avatar_url}")
    embed.add_field(name="ping:",
                    value="Returns the latency of the bot.",
                    inline=False)
    embed.add_field(name="source:",
                    value="Returns the github repo of the bot.",
                    inline=False)
    embed.add_field(name="insult {name/mention}:",
                    value="Insult someone :)",
                    inline=False)
    await ctx.send(embed=embed)


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! Latency: **{round(client.latency * 1000)}**ms')


@client.command()
async def insult(ctx, *, person=None):
    if ctx.author.id == 421240616694054913:  #check if the id is aidan's
        await ctx.send('Aidan u suck, no using this command LMAO')
        return
    if person == None:  #check if there is a person mentioned
        await ctx.send(':x: You gotta insult a person, you dingus.')
        return
    insults = [
        "you suck", "I hope you step on a lego",
        "may all your toast get burnt",
        "i hope your indentation gets messed up",
        "you are a classic example of the inverse ratio between the size of the mouth and the size of the brain",
        "you're about as much use as a condom machine in the Vatican",
        "you should put a condom on your head, because if you're going to act like a dick you better dress like one too.",
        "is an apehead",
        "I can't even call you Fucking Ugly, because Nature has already beaten me to it.",
    ]
    await ctx.send(f"{person}, {random.choice(insults)}.")


@client.command()
async def projects(ctx, member: discord.Member):
    """
    Command is still being developed lmao,
    finished version is supposed to be github like thingy
    """
    data = openfile()
    return


@client.command(aliases=['sourcecode'])
async def source(ctx):
    await ctx.send('https://github.com/wHo69/Computing-Bot')


#async functions
async def openfile():
    with open('projects.json', 'r') as f:
        data = json.load(f)
        f.close()
    return data


#random connec stuff
keep_alive()
load_dotenv()
client.run(os.getenv('DISCORD_TOKEN'))
