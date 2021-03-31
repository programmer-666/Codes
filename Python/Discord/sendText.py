import discord
from discord.ext import commands

cl = commands.Bot(command_prefix='§')

@cl.event
async def on_ready(ctx):
    await ctx.send('gençler iyi akşamlar')
cl.run('ODIxODUzODExMjA2NTIwODUy.YFJxAQ.p7mwhYBja4W1EGywJ8AH6KOv0u8')