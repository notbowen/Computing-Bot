import discord
import json
from discord.ext import commands
import os
from keep_alive import keep_alive
from dotenv import load_dotenv

#bot init stuff
intents = discord.Intents.all()
client = commands.Bot(command_prefix=['c', 'C'], intents=intents, case_insensitive=True)
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
      url="https://cdn.discordapp.com/avatars/871638624716857366/d4acd269c443690c9378cf7c0fe3fce7.webp?size=1024"
      )
    embed.set_footer(text=f"Requested by: {ctx.message.author.name}",
                     icon_url=f"{ctx.message.author.avatar_url}")
    embed.add_field(name="ping:",
                    value="Returns the latency of the bot.",
                    inline=False)
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! Latency: **{round(client.latency * 1000)}**ms')

#random connec stuff
keep_alive()
load_dotenv()
client.run(os.getenv('DISCORD_TOKEN'))
