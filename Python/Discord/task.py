import discord
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix = '%')

@bot.event
async def on_ready():
    loop.start()

@tasks.loop(seconds = 3)
async def loop():
    for c in bot.get_all_channels():
        #print(c, c.id)
        if c.id == 827932024001921114:
            await c.send('loop')

bot.run('ODI0NjQ0MzYyMzI3MTYyODgx.YFyX6Q.wYANeBbu71zuo_09-rLMiPg_bNU')
