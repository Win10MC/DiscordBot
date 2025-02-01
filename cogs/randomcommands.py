import discord
from discord import app_commands
from discord.ext import commands

class RandomBotCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online!")

    @app_commands.command(name="ping")
    async def ping(self, interaction: discord.Interaction):
        ping_embed = discord.Embed(title="Ping", description="Pong! 🏓", color=discord.Color.green())
        ping_embed.add_field(name="Latency", value=f"{round(self.bot.latency * 1000)}ms", inline=False)
        await interaction.response.send_message(embed=ping_embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(RandomBotCommands(bot))