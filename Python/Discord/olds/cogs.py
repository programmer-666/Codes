import discord
import os
from discord.ext import commands
cl = commands.Bot(command_prefix='%')

@cl.command()
async def load(ctx, extension):
    cl.load_extension(f'cogs/{extension}')

@cl.command()
async def unload(ctx, extension):
    cl.unload_extension(f'cogs.{extension}')

cl.load_extension('example.py')

cl.run('ODI0NjQ0MzYyMzI3MTYyODgx.YFyX6Q.wYANeBbu71zuo_09-rLMiPg_bNU')
