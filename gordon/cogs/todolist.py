# Name: Joey Huang & Ao Wang
# Date: 1/23/2021
# File: todolist.py
# Description: Features a to-do list
# Commands: All have todo prefix

import discord
from discord.ext import commands
import datetime as dt
import pickle
import os

# --------------------------- CONVERTERS --------------------------------


def convert_to_datetime(date):
    return dt.datetime.strptime(date, '%m/%d/%y')
# ------------------------------------------------------------------------


class TodoList(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.__tasks = []
        self.__today = dt.datetime.now()

        # Opens Task pickle file if not empty
        try:
            with open('db/Tasks.pkl', 'rb') as f:
                tasks = pickle.load(f)
                self.__date_tasks = tasks
        except EOFError:
            self.__date_tasks = {}

    @commands.command(help='A quick TODO note with options to add, show, and remove tasks. Or wipe it clean with "clear".')
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

    @commands.command(help='Assign tasks to dates and given deadline.')
    async def mark(self, ctx, date: convert_to_datetime, deadline, *task):
        # Given dictionary doesn't include the year, month, or day key, make one
        if date.year not in self.__date_tasks:
            self.__date_tasks[date.year] = {}
        if date.month not in self.__date_tasks[date.year]:
            self.__date_tasks[date.year][date.month] = {}
        if date.day not in self.__date_tasks[date.year][date.month]:
            self.__date_tasks[date.year][date.month][date.day] = []

        # Create task
        task_item = {'task': ' '.join(task),
                     'date': date.strftime('%m/%d/%y'),
                     'deadline': f'{deadline}'}

        # Add it to the backlog
        self.__date_tasks[date.year][date.month][date.day].append(task_item)

        # Save backlog if Bot shutsdown
        with open('db/Tasks.pkl', 'wb') as f:
            pickle.dump(self.__date_tasks, f)

    @commands.command(help='Marks tasks in dates when complete.')
    async def complete(self, ctx, date: convert_to_datetime, task_id: lambda x: int(x) - 1):
        self.__date_tasks[date.year][date.month][date.day][task_id]['task'] = \
            self.__date_tasks[date.year][date.month][date.day][task_id]['task'] + ' ✅'

    @commands.command(help='Delete tasks in dates.')
    async def delete(self, ctx, date: convert_to_datetime, task_id: lambda x: int(x) - 1):
        del self.__date_tasks[date.year][date.month][date.day][task_id]

    # CREDIT: https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
    def daterange(self, start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + dt.timedelta(n)

    @commands.command(help='Display all tasks from daily to weekly.')
    async def show(self, ctx, time):
        list_msg = ''
        if time == 'today':
            # Grab list of today's tasks
            today_tasks = self.__date_tasks[self.__today.year][self.__today.month][self.__today.day]

            # Loop through tasks
            for i, task in enumerate(today_tasks, start=1):
                list_msg += f"{i}. {task['task']} - DEADLINE: {task['date']} {task['deadline']}\n"

            await ctx.send(f">>> Today's Tasks - {self.__today.strftime('%m/%d/%Y')}\n")
            await ctx.send(f'```\n{list_msg}```')

        elif time == 'week':
            complete_msg = ''
            month_tasks = self.__date_tasks[self.__today.year][self.__today.month]

            # Get start week day and end week day
            start_wk_day = self.__today - \
                dt.timedelta(days=self.__today.weekday())
            end_wk_day = start_wk_day + dt.timedelta(days=7)

            # Loop through the days in the week
            for single_date in self.daterange(start_wk_day, end_wk_day):
                # Given that there's a task in the day
                list_msg = ''
                if single_date.day in month_tasks:
                    for i, task in enumerate(month_tasks[single_date.day], start=1):
                        list_msg += f"{i}. {task['task']} - DEADLINE: {task['date']} {task['deadline']}\n"
                    if list_msg:
                        complete_msg += f"```Weekly's Tasks - {single_date.strftime('%m/%d/%Y')}\n{list_msg}```"
            await ctx.send(complete_msg)


def setup(bot):
    bot.add_cog(TodoList(bot))
