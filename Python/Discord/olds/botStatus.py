import discord
from discord.ext import commands
cl = commands.Bot(command_prefix='%')

@cl.event
async def on_ready():
    await cl.change_presence(status = discord.Status.idle, activity = discord.Game('GameObject'))

cl.run('ODI0NjQ0MzYyMzI3MTYyODgx.YFyX6Q.wYANeBbu71zuo_09-rLMiPg_bNU')
