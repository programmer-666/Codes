# actual checks
import discord
from discord.ext import commands, tasks

cl = commands.Bot(command_prefix='%')

@cl.event
async def on_ready():
    print('ready')

cl.run('ODI0NjQ0MzYyMzI3MTYyODgx.YFyX6Q.wYANeBbu71zuo_09-rLMiPg_bNU')
