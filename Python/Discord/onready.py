import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '%')

@bot.event
async def on_read():
    print('Ready')

@bot.command()
async def test(ctx):
    await ctx.send('Testing')

bot.run('ODI0NjQ0MzYyMzI3MTYyODgx.YFyX6Q.wYANeBbu71zuo_09-rLMiPg_bNU')
