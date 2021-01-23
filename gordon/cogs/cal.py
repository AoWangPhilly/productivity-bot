# Name: Joey Huang
# Date: 1/23/2021
# File: cal.py
# Description: Includes the calendar commands, printed with markdown.
# Commands:
# >cal - prints the current calendar
# >next - next month
# >back - previous month

import calendar, discord
from discord.ext import commands

class Cal(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.__currMonth = 1
        self.__currYear = 2021
        self.__currCal = calendar.month(self.__currYear,self.__currMonth)

    @commands.command()
    async def cal(self, ctx):
        self.__currMonth = 1
        self.__currYear = 2021
        self.__currCal = calendar.month(self.__currYear,self.__currMonth)
        await ctx.send('```' + self.__currCal + '```')
        
    @commands.command()
    async def next(self, ctx):
        if self.__currMonth == 12:
            self.__currMonth = 1
            self.__currYear += 1
        else:
            self.__currMonth += 1
        self.__currCal = calendar.month(self.__currYear,self.__currMonth)
        await ctx.send('```' + self.__currCal + '```')    

    @commands.command()
    async def back(self, ctx):
        if self.__currMonth == 1:
            self.__currMonth = 12
            self.__currYear -= 1
        else:
            self.__currMonth -= 1
        self.__currCal = calendar.month(self.__currYear,self.__currMonth)
        await ctx.send('```' + self.__currCal + '```')    

def setup(bot):
    bot.add_cog(Cal(bot))