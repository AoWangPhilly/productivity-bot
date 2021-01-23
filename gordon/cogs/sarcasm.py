import discord
from discord.ext import commands


class Sarcasm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx):
        pass

    @commands.command()
    async def gif(self, ctx):
        pass

    @commands.command()
    async def quote(self, ctx):
        pass
