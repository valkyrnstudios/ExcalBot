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

    @commands.command(name='info', aliases=['raidtime', 'raidtimes'])
    async def info(self, ctx):
        embed = discord.Embed(title='http://eternalgamers.org',
                              description='Guild website',
                              colour=2550255)

        embed.set_author(name='Guild website',
                         url='http://eternalgamers.org/events',
                         icon_url='https://upload.wikimedia.org/wikipedia/commons/3/3d/Asahi-eg-company_icon.png')

        embed.add_field(name=':clock2: **Raid Times** :clock2:',
                        value='Monday: 8-11PM Eastern Time (01:00 - 04:00 Server Time)\nThur: 8-11PM Eastern Time (01:00 - 04:00 Server Time)\n**Please arrive 15 mins prior for raid invites and bring all consumables and gear you will need.\n**')

        embed.add_field(name=':no_entry: **Required Addons** :no_entry:',
                        value='Threat Meter (DTM > Omen)\nDeadlyBossMobs OR BigWigs\nGuild2Guild\n\nSee `!addons` in discord for Addon Downloads')

        embed.set_footer(text='EGBot',
                        icon_url='https://upload.wikimedia.org/wikipedia/commons/3/3d/Asahi-eg-company_icon.png')

        await ctx.send(embed=embed)

    @commands.command(name='addons')
    async def addons(self, ctx):
        embed = discord.Embed(title='http://eternalgamers.org',
                              description='**A list of the more common addons including download links.**',
                              colour=2550255)

        embed.set_author(name='Addon Downloads',
                         icon_url='https://upload.wikimedia.org/wikipedia/commons/3/3d/Asahi-eg-company_icon.png')

        embed.add_field(name='Be sure to enable out of date addons in the client',
                        value='''
**Ace Library Addons (Required for some addons to work)**
https://twam.uk7.org/files/Ace123.zip

**CombatLogClearer (Alternative to the Macro)**
https://twam.uk7.org/files/CombatLogClearer.zip

**DiamondThreatMeter (DTM)**
https://twam.uk7.org/files/DiamondThreatMeter.zip

**DeadlyBossMods (DBM)**
https://twam.uk7.org/files/DeadlyBossMods.zip

**BigWigs (DBM Alternative)**
https://twam.uk7.org/files/BigWigs.zip

**Guild2Guild**
https://twam.uk7.org/files/Guild2Guild.zip

**PallyPower**
https://twam.uk7.org/files/PallyPower.zip

**Prat (Chat Addon)**
https://twam.uk7.org/files/Prat.zip

**Recount**
https://twam.uk7.org/files/Recount.zip

**xperl**
https://twam.uk7.org/files/xperl.zip

**Grid**
https://twam.uk7.org/files/Grid.zip

**Full Addon Pack**
https://twam.uk7.org/files/Addons.zip
''')


        embed.set_footer(text='EGBot',
                        icon_url='https://upload.wikimedia.org/wikipedia/commons/3/3d/Asahi-eg-company_icon.png')

        await ctx.send(embed=embed)

    @commands.command(name='beef', aliases=['twam'], hidden=True)
    async def beef(self, ctx):
        messages_list = ['Soon:tm:', 'Made by Twam:tm:']
        await ctx.send(random.choice(messages_list))

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

    @commands.command(name='fading', hidden=True)
    async def fading(self, ctx):
        await ctx.send('https://i.imgur.com/XdjGCWh.jpg')

    @commands.command(name='gucci', hidden=True)
    async def gucci(self, ctx):
        await ctx.send('Totes gucci lit af fam #420 blaze it swag:tm:')

def setup(bot):
    bot.add_cog(EG(bot))
