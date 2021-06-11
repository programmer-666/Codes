import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '%')

@bot.command()
async def q(ctx):
    await ctx.message.add_reaction("🌍")

@bot.event
async def on_message(message):
    #print(message.attachments[0])
    #print(message.attachments)
    #print(message.attachments[0].filename)
    print(message.channel.name) # mesajın gönderildiği kanal ile ilgili bilgi
    # message.attachments ile ekler ile ilgili bilgi gelir

bot.run('ODI0NjQ0MzYyMzI3MTYyODgx.YFyX6Q.wYANeBbu71zuo_09-rLMiPg_bNU')
