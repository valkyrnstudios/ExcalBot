import discord
from discord.ext import commands

import random

class EG(commands.Cog, name='Eternal Gamers'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='signup', aliases=['website'])
    async def signup(self, ctx):
        await ctx.send('http://eternalgamers.org/events')

    @commands.command(name='beef', aliases=['twam',], hidden=True)
    async def beef(self, ctx):
        await ctx.send('Soon:tm:')

    @commands.command(name='kynura', aliases=['kahira'], hidden=True)
    async def kynura(self, ctx):
        messages_list = [':kynura:', 'Improved by Kynura:tm:']
        await ctx.send(random.choice(messages_list))

    @commands.command(name='noah', aliases=['pallysk'], hidden=True)
    async def noah(self, ctx):
        await ctx.send('#scrubtotemlesssham')

    @commands.command(name='aira', hidden=True)
    async def aira(self, ctx):
        await ctx.send('https://i.imgur.com/f0SSY5s.gif')

    @commands.command(name='cath', aliases=['dirt'], hidden=True)
    async def cath(self, ctx):
        await ctx.send('/reroll mage')

def setup(bot):
    bot.add_cog(EG(bot))
