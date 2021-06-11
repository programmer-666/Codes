import discord
from discord.ext import commands, tasks
from itertools import cycle

cl = commands.Bot(command_prefix='%')
stats = cycle(['Stat1', 'Stat2'])

@cl.event
async def on_ready():
    print('ready')

@tasks.loop(seconds = 3)
async def changeStat():
    await cl.change_presence(activity=discord.Game(next(stats)))


cl.run('ODI0NjQ0MzYyMzI3MTYyODgx.YFyX6Q.wYANeBbu71zuo_09-rLMiPg_bNU')
