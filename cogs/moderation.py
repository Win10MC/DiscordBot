import discord
from discord.ext import commands
from discord import app_commands
import datetime

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is online!")

    @app_commands.command(name="clear", description="Deletes a specified amount of messages from the current channel.")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def delete_messages(self, interaction: discord.Interaction, amount: int):
        if amount < 1:
            await interaction.response.send_message(f"{interaction.user.mention}, please specify a value greater than 1.", ephemeral=True)
            return
        
        await interaction.response.defer(ephemeral=True)
        deleted_messages = await interaction.channel.purge(limit=amount)
        embed = discord.Embed(title="Messages Deleted", description=f"{interaction.user.mention} has deleted {len(deleted_messages)} message(s).", color=discord.Color.red())
        await interaction.followup.send(embed=embed, ephemeral=True)

    @app_commands.command(name="kick", description="Kicks a specified member.")
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick(self, interaction: discord.Interaction, member: discord.Member):
        await interaction.guild.kick(member)
        embed = discord.Embed(title="Member Kicked", description=f"{interaction.user.mention} has kicked {member.mention}!", color=discord.Color.orange())
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @app_commands.command(name="ban", description="Bans a specified member.")
    @app_commands.checks.has_permissions(ban_members=True)
    async def ban(self, interaction: discord.Interaction, member: discord.Member):
        await interaction.guild.ban(member)
        embed = discord.Embed(title="Member Banned", description=f"{interaction.user.mention} has banned {member.mention}!", color=discord.Color.red())
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="unban", description="Unban a specified user ID.")
    @app_commands.checks.has_permissions(ban_members=True)
    async def unban(self, interaction: discord.Interaction, user_id: str):
        user = await self.bot.fetch_user(user_id)
        await interaction.guild.unban(user)
        embed = discord.Embed(title="User Unbanned", description=f"{interaction.user.mention} has unbanned {user.name}!", color=discord.Color.green())
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="timeout", description="Times out a specified member.")
    @app_commands.checks.has_permissions(moderate_members=True)
    async def timeout(self, interaction: discord.Interaction, member: discord.Member, seconds: int = 0, minutes: int = 0, hours: int = 0, days: int = 0, reason: str = None):
        duration = datetime.timedelta(seconds = seconds, minutes = minutes, hours = hours, days = days)
        await member.timeout(duration, reason=reason)
        embed = discord.Embed(title="User Timed Out", description=f"{interaction.user.mention} has timed out {member.mention} for {duration}!", color=discord.Color.green())
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @app_commands.command(name="untimeout", description="Times out a specified member.")
    @app_commands.checks.has_permissions(moderate_members=True)
    async def untimeout(self, interaction: discord.Interaction, member: discord.Member):
        await member.edit(timed_out_until=None)
        embed = discord.Embed(title="User Untimed Out", description=f"{interaction.user.mention} has untimed out {member.mention}!", color=discord.Color.green())
        await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(Mod(bot))