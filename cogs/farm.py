import discord
from discord.ext import commands

class Farm(commands.Cog, name='Farming macros'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='farm', aliases=['farming'])
    async def farm(self, ctx):
        await ctx.send('''**Locations for Farming**
**Excalibur Gatherer DB**
`!gatherdb`

**Sporfish Locations**
`!sporefish`

**Bluefish Locations**
`!bluefish`

**Mudfish Locations**
`!mudfish`

**Golden Darter Locations**
`!goldends`

**Flamecap Locations**
`!flamecap`

**Windy Cloud Locations**
`!primalair`
''')

    @commands.command(name='gathererdb', aliases=['gatherer'])
    async def gathererdb(self, ctx):
        await ctx.send('''**Excalibur Gatherer DB**
https://twam.uk7.org/files/GathererDB_Excalibur.zip
''')

    @commands.command(name='sporefish', aliases=['farmsporefish'])
    async def sporefish(self, ctx):
        await ctx.send('''**Sporefish School Locations**
_(All Pools have a 5 min respawn. You must be in Zangarmarsh before using this macro)_
```
/way 18.5 45.7 Sporefish
/way 20.0 35.9 Sporefish
/way 25.1 33.7 Sporefish
/way 25.1 44.5 Sporefish
/way 14.8 52.1 Sporefish
/way 73.8 60.0 Sporefish
/way 75.5 62.4 Sporefish
```
(To clear all way points) 
`/noway`
''')

    @commands.command(name='bluefish', aliases=['farmbluefish'])
    async def bluefish(self, ctx):
        await ctx.send('''**Bluefish School Locations**
_(All Pools have a 5 min respawn. You must be in Nagrand before using this macro)_
```
/way 48.6 47.8 Bluefish
/way 54.4 25.6 Bluefish
/way 58.6 33.5 Bluefish
/way 60.6 34.2 Bluefish
```
(To clear all way points) 
`/noway`
''')

    @commands.command(name='Mudfish', aliases=['farmmudfish'])
    async def mudfish(self, ctx):
        await ctx.send('''**Mudfish School Locations**
_(All Pools have a 5 min respawn. You must be in Nagrand before using this macro)_
```
/way 55.9 31.7 Mudfish
/way 51.8 47.4 Mudfish
/way 50.2 48.5 Mudfish
/way 47.5 44.3 Mudfish
/way 34.4 45.8 Mudfish
/way 30.6 54.7 Mudfish
```
(To clear all way points) 
`/noway`
''')

    @commands.command(name='goldendarter', aliases=['goldends', 'farmdarter'])
    async def goldendarter(self, ctx):
        await ctx.send('''**Golden Darter School Locations**
_(All Pools have a 5 min respawn. You must be in Terokkar Forest before using this macro)_
_(Darter Pools are marked 80%, Brackish Mixed Pools are marked 50%)_
```
/way 55.1 44.1 80%
/way 60.0 53.9 80%
/way 71.0 43.4 80%
/way 60.0 53.9 50%
/way 58.1 51.6 50%
/way 60.7 50.6 50%
/way 55.8 49.4 50%
/way 63.1 48.8 50%
/way 66.2 46.2 50%
/way 61.6 40.6 50%
/way 53.3 38.0 50%
```
(To clear all way points) 
`/noway`
''')

    @commands.command(name='flamecaps', aliases=['farmflamecaps'])
    async def flamecaps(self, ctx):
        await ctx.send('''**Flame Cap Locations**
_(All Herbs have a 10 min respawn. You must be in Zangermarsh before using this macro)_
```
#show Flame Cap
/way 80.7 30.8 FC12
/way 80.3 37.0 FC11
/way 80.3 41.7 FC10
/way 74.7 48.0 FC9
/way 38.7 47.3 FC8
/way 36.6 32.0 FC7
/way 29.7 40.9 FC6
/way 25.4 56.4 FC5
/way 17.5 57.6 FC4
/way 13.3 63.7 FC3
/way 38.5 63.8 FC2
/way 70.6 72.5 FC1
```
(To clear all way points) 
`/noway`
''')

    @commands.command(name='primalair', aliases=['farmair'])
    async def primalair(self, ctx):
        await ctx.send('''**Windy Cloud Locations**
_(All clouds have a 5 min respawn. You must be in Nagrand before using this macro)_
```
/way 60.3 75.5 Number10
/way 43.9 78.8 Number9
/way 31.5 73.6 Number8
/way 30.3 63.2 Number7
/way 42.0 27.3 Number6
/way 50.8 29.5 Number5
/way 57.3 27.5 Number4
/way 56.0 37.6 Number3
/way 58.5 42.4 Number2
/way 68.5 65.5 Number1
```
(To clear all way points) 
`/noway`
''')

def setup(bot):
    bot.add_cog(Farm(bot))
