import discord
import asyncio
from random import randint as rd
from discord.ext import commands
cl = commands.Bot(command_prefix='%')

@cl.event
async def on_ready():
    print('Ready')

@cl.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason = reason)
    
@cl.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason = reason)
    
    
cl.run('ODI0NjQ0MzYyMzI3MTYyODgx.YFyX6Q.wYANeBbu71zuo_09-rLMiPg_bNU')