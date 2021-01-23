import discord
from discord.ext import commands

import logging
import os

# -------------------- DISCORD LOGGING ------------------------
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
# -------------------------------------------------------------

# -------------------- SECRET KEY -----------------------------
with open('secret_key', 'r') as f:
    SECRET_KEY = f.read()
# -------------------------------------------------------------

bot = commands.Bot(command_prefix='>')

# ----------------------- ADD COGS ----------------------------
bot.load_extension("cogs.sarcasm")
bot.load_extension("cogs.calendar")

# -------------------------------------------------------------


@ bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

bot.run(SECRET_KEY)
