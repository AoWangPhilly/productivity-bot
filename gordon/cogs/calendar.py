import discord
from discord.ext import commands


class Calendar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
