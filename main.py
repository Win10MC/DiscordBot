import discord
from discord.ext import commands
import top_secret.encryption as encryption
import time

intents = discord.Intents.all()
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Add an attribute to store start time
bot.start_time = None

@bot.event
async def on_ready():
    bot.start_time = time.time()  # Record the time when the bot is ready
    print(f'Logged in as {bot.user}')

@bot.command(name="ping", aliases=["pong", "p"])
async def ping(ctx):
    embed = discord.Embed(title="Ping", description="", color=discord.Color.green())
    embed.add_field(name="Pong! 🏓", value=f"{round(bot.latency * 1000)}ms", inline=False)
    await ctx.reply(embed=embed, ephemeral=True)

@bot.command(name="uptime")
async def uptime(ctx):
    if bot.start_time:
        uptime_seconds = time.time() - bot.start_time
        uptime_message = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))
        await ctx.reply(f'Uptime: {uptime_message}')
    else:
        await ctx.reply('Bot uptime is not available.')

with open("token.txt", "r", encoding="utf-8") as file:
    token = encryption.decrypt(file.readline().strip())

bot.run(token)