import discord
from discord.ext import commands

class Commandz(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def sayhi(self, ctx):
        await ctx.send('Hi')
        
    @commands.command()
    async def users(self, ctx):
        await ctx.send(len(self.bot.guilds[0].members))

def setup(bot):
    bot.add_cog(Commandz(bot))