'''
FILE: sarcasm.py
DESCRIPTION: Sarcasm cog of the productivity bot
DATE: 01/23/2021
AUTHOR: Ao Wang
'''

import discord
from discord.ext import commands
import pickle
from random import choice
from os.path import join, dirname


class Sarcasm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def _open_pickle(self, fname):
        pickle_path = join('db', fname+'.pkl')
        with open(pickle_path, 'rb') as f:
            pickle_lst = pickle.load(f)
        return pickle_lst

    @ commands.command(help='Outputs random Gordon Ramsay meme')
    async def meme(self, ctx):
        await ctx.send(choice(self._open_pickle('Memes')))

    @ commands.command(help='Outputs random Gordon Ramsay GIF')
    async def gif(self, ctx):
        await ctx.send(choice(self._open_pickle('GIFs')))

    @ commands.command(help='Outputs random Gordon Ramsay quote')
    async def quote(self, ctx):
        await ctx.send(choice(self._open_pickle('Quotes')))


def setup(bot):
    bot.add_cog(Sarcasm(bot))
