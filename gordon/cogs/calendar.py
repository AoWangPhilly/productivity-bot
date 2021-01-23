import discord, calendar
from discord.ext import commands

class Calendar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Calendar(bot))