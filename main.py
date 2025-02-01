import discord
from discord.ext import commands as cmds, tasks
import top_secret.encryption as encryption
import asyncio
import os
from itertools import cycle
import random

statuses = ["with your mom", "with your dad", "with your sister", "with your brother", "with your grandma", "with your grandpa"]

intents = discord.Intents.all()
intents.presences = True

bot = cmds.Bot(command_prefix="!", intents=intents)

@tasks.loop(seconds=5)
async def status_task():
    await bot.change_presence(activity=discord.Game(statuses[random.randint(0, len(statuses) - 1)]))

with open("token.txt", "r", encoding="utf-8") as file:
    token = encryption.decrypt(file.readline().strip())

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")
    status_task.start()
    try:
        synced_commands = await bot.tree.sync()
        print(f"Synced {len(synced_commands)} commands.")
    except Exception as e:
        print(f"An error with syncing commands has occured: {e}")

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load()
        await bot.start(token)

asyncio.run(main())