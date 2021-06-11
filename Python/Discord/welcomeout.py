import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '%')

@bot.event
async def on_read():
    print('Ready')

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name = "welcome")
    await channel.send(member, 'comes')


bot.run('ODI0NjQ0MzYyMzI3MTYyODgx.YFyX6Q.wYANeBbu71zuo_09-rLMiPg_bNU')
