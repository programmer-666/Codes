import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '%')

@bot.event
async def on_read():
    print('Ready')

@bot.command(aliases = ['say'])
async def test(ctx, *args):
    # ctx, komutu gööndere kişi ile ilgili bilgileri içerir
    text = ""
    for i in args:
        text+=i+" "
    await ctx.send(f'"{text}"')

@bot.command()
@commands.has_role("admin") # rol kısıtlaması
async def spoilerText(ctx):
    await ctx.send('||spoilerText||')

@bot.command()
async def user(ctx, *, member): # * ifadesinden sonraki tüm değerler member içine gider
    membername, memberid = member.split('#')
    await ctx.send(membername+" "+memberid)

@bot.command()
async def bsay(ctx, *, text):
    await ctx.send(f"'{text}'")
    
@bot.command()
async def cpyc(ctx):
    await ctx.channel.clone()
    # await asenkron fonksiyonda işlemi kuyruğa sokar
bot.run('ODI0NjQ0MzYyMzI3MTYyODgx.YFyX6Q.wYANeBbu71zuo_09-rLMiPg_bNU')
