# Name: Joey Huang
# Date: 1/23/2021
# File: todolist.py
# Description: Features a to-do list
# Commands: All have todo prefix

import discord
from discord.ext import commands

class todoList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.__currList = []
        self.__currIndex = 1
        self.__tempItem = None

    @commands.command()
    async def todo(self, ctx, comm, *arg):
        # >todo add <task>
        # Adds a task to to-do list
        if comm == "add": 
            task = ' '.join(arg)
            self.__currList.append(task)
            await ctx.send('Added "' + task + '" as a task!')      
        # >todo show 
        # Shows current to-do list     
        elif comm == "show":
            taskList = "\n".join(self.__currList)
            await ctx.send('>>> To-Do List\n')
            await ctx.send('```To-Do List \n' + str(taskList) + '```')
        
        # >todo remove <task number>
        # Removes item from list
        elif comm == "remove":
            targetInd = ''.join(arg)
            tempInd = int(targetInd)
            targetInd = tempInd - 1
            self.__currList.pop(targetInd)
            await ctx.send('Removed task ' + str(tempInd) + "!\nGood work idiot sandwich!")
        
        # Invalid command if anything else is entered
        else:
            await ctx.send('Invalid command.')

def setup(bot):
    bot.add_cog(todoList(bot))