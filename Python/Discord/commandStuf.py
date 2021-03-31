import discord
import asyncio
from random import randint as rd
from discord.ext import commands
cl = commands.Bot(command_prefix='%')
botNameId = str(cl.user).split('#')

"""
@cl.event
async def on_ready():
    print('Logged in as')
    print(cl.user.name)
    print(cl.user.id)
    print('------')
"""



@cl.command()
async def ping(ctx):
    await ctx.send(str(round(cl.latency*1000))+'ms')
    
@cl.command(aliases=['rint'])
async def randint(ctx, *, get): # randint(int(get[0]),int(get[1]))
    await ctx.send((rd(int(str(get.split()[0])),int(str(get.split()[1])))))

@cl.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    
@cl.command()
async def otm(ctx, *, get):
    def is_me(m):
        return m.author == cl.user
    cmd = get.split()
    message = ""
    for i in cmd[1:]:
        message+=i+' '
    await ctx.channel.purge(limit=1) # clear message
    m = await ctx.send(''+message+'') #send message
    await asyncio.sleep(float(cmd[0][1:])) #sleep(float(cmd[0][1:])) # waiting time
    await m.delete()
    #await ctx.channel.purge(limit=1, check=is_me)

cl.run('ODI0NjQ0MzYyMzI3MTYyODgx.YFyX6Q.yQHaNuzDu91yzVGpOtBlG2BaVZQ')