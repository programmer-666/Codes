import discord
from discord.ext import commands

cl = commands.Bot(command_prefix='§')

@cl.event
async def on_ready():
    print('ReadyUp')
# Botu Hazır Hale Getirir

@cl.event
async def on_member_join(member):
    print(f'{member} geldi')
# Sunucuya Biri Katılırsa

@cl.event
async def on_member_remove(member):
    print(f'{member} gitti')
    
cl.run('ODI0NjQ0MzYyMzI3MTYyODgx.YFyX6Q.yQHaNuzDu91yzVGpOtBlG2BaVZQ')