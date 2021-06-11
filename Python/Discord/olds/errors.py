import discord
from discord.ext import commands, tasks
from itertools import cycle

cl = commands.Bot(command_prefix='%')

@cl.event
async def on_ready():
    print('ready')

@cl.event # for all comands
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments.')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send('command not found')
@cl.command()
async def clear(ctx, amount:int):
    await ctx.channel.purge(limit=amount)

@clear.error
async def clearerr(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('take arguments')
cl.run('ODI0NjQ0MzYyMzI3MTYyODgx.YFyX6Q.wYANeBbu71zuo_09-rLMiPg_bNU')
