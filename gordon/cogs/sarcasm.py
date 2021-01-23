import discord
from discord.ext import commands
import pickle
from random import choice
from os.path import join
from pathlib import Path


class Sarcasm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def _open_pickle(self, fname):
        pickle_path = Path((join('db', fname+'.pkl')))
        with open(pickle_path, 'rb') as f:
            pickle_lst = pickle.load(f)
        return pickle_lst

    @ commands.command()
    async def meme(self, ctx):
        await ctx.send(choice(self._open_pickle('Memes')))

    @ commands.command()
    async def gif(self, ctx):
        await ctx.send(choice(self._open_pickle('GIFs')))

    @ commands.command()
    async def quote(self, ctx):
        await ctx.send(choice(self._open_pickle('Quotes')))


def setup(bot):
    bot.add_cog(Sarcasm(bot))
