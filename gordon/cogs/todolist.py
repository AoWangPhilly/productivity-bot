# Name: Joey Huang
# Date: 1/23/2021
# File: todolist.py
# Description: Features a to-do list
# Commands: All have todo prefix

import discord
from discord.ext import commands

class TodoList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.__tasks = []

    @commands.command()
    async def todo(self, ctx, comm, *arg):
        # >todo add <task>
        # Adds a task to to-do list
        if comm == "add":
            task = ' '.join(arg)
            self.__tasks.append(task)
            await ctx.send(f'Added {task} as a task!')
        # >todo show
        # Shows current to-do list
        elif comm == "show":
            todo_list_msg = ''
            for i, task in enumerate(self.__tasks, start=1):
                todo_list_msg += f'{i}. {task}\n'
            await ctx.send('>>> To-Do List\n')
            await ctx.send(f'```\n{todo_list_msg}```')

        # >todo remove <task number>
        # Removes item from list
        elif comm == "remove":
            target_idx = int(''.join(arg)) - 1
            if len(self.__tasks):
                task = self.__tasks.pop(target_idx)
                await ctx.send(f'Removed task: {task}!\nGood work idiot sandwich!')

        #>clear 
        # Clears the list
        elif comm == "clear":
           self.__tasks = []   
           await ctx.send('List cleared!')
                
        # Invalid command if anything else is entered
        else:
            await ctx.send('Invalid command.')

def setup(bot):
    bot.add_cog(TodoList(bot))
