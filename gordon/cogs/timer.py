import discord
from discord.ext. import commands,tasks

class Timer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


client=commands.Bot(command_prefix='>')

@climent.event
async def timer(ctx, seconds):
		try:
		secondint=int(seconds)
		if secondint>300;
		await ctx.send("Cannot go over 5 minutes.")
		raise BaseException
		if secondint<=0:
		await ctx.send("Negatives are not available.")
		raise BaseException

message=await ctx.send({"timer:{seconds}"})

while true:
secondint-=1
if secondint==0:
await message.edit(content="End!")
break

await message.edit(content=f"Timer: {seconint}")
await asyncio.sleep(1)
await ctx.send(f"{ctx.author.mention}, Countdown Over!")

except ValueError:
await ctx.send("Enter a number.")

def setup(bot):
    bot.add_cog(Timer(bot))