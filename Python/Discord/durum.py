import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '%')

@bot.event
async def on_ready():
    #await bot.change_presence(activity=discord.Game(name='GameName'))
    #await bot.change_presence(activity=discord.Streaming(name='GameName', url='https://www.twitch.tv/terryadavis_templeos'))
    #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='song'))
    #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='watch'))

bot.run('ODI0NjQ0MzYyMzI3MTYyODgx.YFyX6Q.wYANeBbu71zuo_09-rLMiPg_bNU')
