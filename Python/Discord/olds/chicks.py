# actual checks
import discord
from discord.ext import commands, tasks
from itertools import cycle

cl = commands.Bot(command_prefix='%')

@cl.event
async def on_ready():
    print('ready')

@cl.command()
@commands.hash_permissions(manage_messages = True)
async def clear(ctx, amount:int):
    await ctx.channel.purge(limit=amount)

@cl.command()
async def exm(ctx):
    await ctx.send(f'{ctx.author}')
    
cl.run('ODI0NjQ0MzYyMzI3MTYyODgx.YFyX6Q.wYANeBbu71zuo_09-rLMiPg_bNU')
