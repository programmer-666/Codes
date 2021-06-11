import discord
import asyncio
from random import randint as rd
from discord.ext import commands
cl = commands.Bot(command_prefix='%')

@cl.event
async def on_ready():
    print('Ready')
    
@cl.command()
async def unban(ctx,* ,member):
    banneds = await ctx.guild.bans()
    m_name, m_disc = member.split('#')
    
    for banentry in banneds:
        user = banentry.user
        
        if (user.name, user.discriminator) == (m_name, m_disc):
            await ctx.guild.unban(user)
            await ctx.send('unbanned success')
            return 