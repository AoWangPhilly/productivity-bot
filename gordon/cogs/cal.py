# Name: Joey Huang
# Date: 1/23/2021
# File: cal.py
# Description: Includes the calendar commands, printed with markdown.

import calendar
import discord
from discord.ext import commands
import datetime as dt


class Cal(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.__currMonth = dt.datetime.now().month
        self.__currYear = dt.datetime.now().year
        self.__currCal = calendar.month(self.__currYear, self.__currMonth)

    # >cal <opt. year> <opt. month>
    # Prints the current calendar, unless specified
    @commands.command()
    async def cal(self, ctx, intYear: int = None, intMonth: int = None):
        if intYear == None and intMonth == None:
            self.__currMonth = dt.datetime.now().month
            self.__currYear = dt.datetime.now().year
            self.__currCal = calendar.month(self.__currYear, self.__currMonth)
        else:
            if intMonth > 12 or intMonth < 1:
                await ctx.send('Invalid month and/or year.')
            else:
                self.__currCal = calendar.month(intYear, intMonth)
        await ctx.send('```' + self.__currCal + '```')

    # >next
    # Prints next month
    @commands.command()
    async def next(self, ctx):
        if self.__currMonth == 12:
            self.__currMonth = 1
            self.__currYear += 1
        else:
            self.__currMonth += 1
        self.__currCal = calendar.month(self.__currYear, self.__currMonth)
        await ctx.send('```' + self.__currCal + '```')

    # >back -
    # Prints previous month
    @commands.command()
    async def back(self, ctx):
        if self.__currMonth == 1:
            self.__currMonth = 12
            self.__currYear -= 1
        else:
            self.__currMonth -= 1
        self.__currCal = calendar.month(self.__currYear, self.__currMonth)
        await ctx.send('```' + self.__currCal + '```')


def setup(bot):
    bot.add_cog(Cal(bot))
