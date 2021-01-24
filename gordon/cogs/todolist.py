# Name: Joey Huang
# Date: 1/23/2021
# File: todolist.py
# Description: Features a to-do list
# Commands: All have todo prefix

import discord
from discord.ext import commands
import datetime as dt
import pickle

# --------------------------- CONVERTERS --------------------------------


def convert_to_datetime(date):
    return dt.datetime.strptime(date, '%m/%d/%y')
# ------------------------------------------------------------------------


class TodoList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.__tasks = []
        self.__date_tasks = {}

    @commands.command()
    async def todo(self, ctx, cmd, *arg):
        # >todo add <task>
        # Adds a task to to-do list
        if cmd == "add":
            task = ' '.join(arg)
            self.__tasks.append(task)
            await ctx.send(f'Added {task} as a task!')
        # >todo show
        # Shows current to-do list
        elif cmd == "show":
            todo_list_msg = ''
            for i, task in enumerate(self.__tasks, start=1):
                todo_list_msg += f'{i}. {task}\n'
            await ctx.send('>>> To-Do List\n')
            await ctx.send(f'```\n{todo_list_msg}```')

        # >todo remove <task number>
        # Removes item from list
        elif cmd == "remove":
            target_idx = int(''.join(arg)) - 1
            if len(self.__tasks):
                task = self.__tasks.pop(target_idx)
                await ctx.send(f'Removed task: {task}!\nGood work idiot sandwich!')

        # >clear
        # Clears the list
        elif cmd == "clear":
            self.__tasks = []
            await ctx.send('List cleared!')

        # Invalid command if anything else is entered
        else:
            await ctx.send('Invalid command.')

    @commands.command()
    async def mark(self, ctx, date: convert_to_datetime, deadline, *task):
        if date.year not in self.__date_tasks:
            self.__date_tasks[date.year] = {}
        if date.month not in self.__date_tasks[date.year]:
            self.__date_tasks[date.year][date.month] = {}
        if date.day not in self.__date_tasks[date.year][date.month]:
            self.__date_tasks[date.year][date.month][date.day] = []

        task_item = {'task': ' '.join(task),
                     'deadline': f"{date.strftime('%m/%d/%y')} {deadline}"}

        self.__date_tasks[date.year][date.month][date.day].append(task_item)
        print(self.__date_tasks)

    @commands.command()
    async def show(self, ctx, time):
        if time == 'today':
            pass
        elif time == 'week':
            pass
        elif time == 'month':
            pass


def setup(bot):
    bot.add_cog(TodoList(bot))
