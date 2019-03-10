import discord
from discord.ext import commands

class Macros(commands.Cog, name='Misc macros'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='healthstones', aliases=['lockrocks'])
    async def healthstones(self, ctx):
        await ctx.send('''**Ordered Healthstone Macro**
```
#showtooltip Master Healthstone
/use item:22105
/use item:22104
/use item:22103
```
''')

    @commands.command(name='spell', aliases=['spelleffect'])
    async def spelleffect(self, ctx):
        await ctx.send('''**Double the default Spell effect level**
```
/console spelleffectlevel 50
```
Change the value for custom setting (Changes will revert to default value (25) when logging out)
''')

    @commands.command(name='combat', aliases=['combatlog'])
    async def combat(self, ctx):
        await ctx.send('''**Manual Combat Log Clearing Macro**
```
/run local f = CreateFrame("frame",nil, UIParent); f:SetScript("OnUpdate", CombatLogClearEntries);
```
Combat Log Clearer Addon (Alternative to the Macro)
https://twam.uk7.org/files/CombatLogClearer.zip 
''')

    @commands.command(name='camera', aliases=['maxcam'])
    async def camera(self, ctx):
        await ctx.send('''**Set the max camera distance**
```
/console cameradistancemax 50
```

**Set the max camera zoom / scroll speed**
```
/console cameraDistanceMoveSpeed 50
```
''')

    @commands.command(name='avoidance')
    async def avoidance(self, ctx):
        await ctx.send('''**Warrior and Paladin Avoidance Macro**
```
/run DEFAULT_CHAT_FRAME:AddMessage("Need 102.4 combat table coverage. Currently at: "..string.format("%.2f", GetDodgeChance()+GetBlockChance()+GetParryChance() +5))
```
This macro includes the 5% base miss chance for mobs Pre-Sunwell 
''')

    @commands.command(name='drums')
    async def drums(self, ctx):
        await ctx.send('''**Manual Drumming Macro**
```
/p Using Drums of Battle
/use Drums of Battle
/in 25 /p My Drums will run out in 5 secs
/in 30 /w Player2 You're next drummer!
/in 115 /p My drums will be ready in 5 secs
```

NDrums Addon (Suggested Alternative to the Macro)
https://twam.uk7.org/files/NDrums.zip 
''')


def setup(bot):
    bot.add_cog(Macros(bot))
