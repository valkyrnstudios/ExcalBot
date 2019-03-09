import discord
from discord.ext import commands

import random

class EG(commands.Cog, name='Eternal Gamers'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='signup', aliases=['website'])
    async def signup(self, ctx):
        embed = discord.Embed(title='http://eternalgamers.org',
                              description='_Signup for Raids_',
                              colour=2550255)

        embed.set_author(name='Raiding Schedule',
                         url='http://eternalgamers.org/events',
                         icon_url='https://upload.wikimedia.org/wikipedia/commons/3/3d/Asahi-eg-company_icon.png')

        embed.add_field(name=':computer: Mark yourself as Yes, No, or Maybe, for all raid days :computer:',
                        value='Signing up is quick and easy; you\'re able to sign up for multiple raid days in advance if you know you will be making the whole month.')

        embed.add_field(name='We require all raiders to have a website account and signup for raids http://eternalgamers.org/events',
                        value='_!egbot to list bot commands_')

        embed.set_footer(text='EGBot',
                        icon_url='https://upload.wikimedia.org/wikipedia/commons/3/3d/Asahi-eg-company_icon.png')

        await ctx.send(embed=embed)

    @commands.command(name='beef', aliases=['twam'], hidden=True)
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
