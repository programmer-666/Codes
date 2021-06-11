import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '%')

@bot.command()
async def load(ctx, ext):
    bot.load_extension('cogs.'+ext)

@bot.command()
async def unload(ctx, ext):
    bot.unload_extension('cogs.'+ext)
    
@bot.command()
async def rld(ctx, ext):
    bot.unload_extension('cogs.'+ext)
    bot.load_extension('cogs.'+ext)

bot.run('ODI0NjQ0MzYyMzI3MTYyODgx.YFyX6Q.wYANeBbu71zuo_09-rLMiPg_bNU')
