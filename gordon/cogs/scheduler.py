import discord
from discord.ext import commands


class Schedule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
