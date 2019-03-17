import discord
from discord.ext import commands

class Swp(commands.Cog, name='SWP leading'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='leadkalec', aliases=['kalec'])
    async def leadkalec(self, ctx):
        await ctx.send('''**Kalec**

**Upstairs**
- Spread 12-15 Yards
- Stack TIGHTLY in center if you HAVE the Spectral Exhaustion debuff
- Move out of the center and SPREAD when there is 5-8 Seconds left on your debuff
- Take the current or next portal if you do NOT have the debuff

**Downstairs**
- Stack behind Demon
- Heal the Tank
- Downstairs Tank will take 10k Damage plus a 3 second DOT (1k per second for 3 seconds) every 13 seconds
- Watch for Decurse and time properly
- Blow all Personal Cooldowns downstairs (Demon must die first)

Spectral Exhaustion - https://i.imgur.com/bSuQWqK.png
Curse of Boundless Agony - https://i.imgur.com/v8lZDrT.png 

**Assignment**
```
/rw --- Kalec ---
/rw Tanks - [Beef] + [Fetha]
/rw Group Melee - [Group 2] + [Nico]
/rw Group North - [Group 3] + [Group 1]
/rw Group South - [Group 4] + [Cath] 
/rw Floaters - [Cozzmo] + [Pallysk]
```
''')

    @commands.command(name='leadbrut', aliases=['brut'])
    async def leadbrut(self, ctx):
        await ctx.send('''**Brut**

Soulstones on Tanks
**Positions**
- Healers directly behind Tanks for priority chains
- Range DPS behind Healers
- Melee be prepared to move to soak damage
**Burns**
- Mages: Iceblock, Paladins: Bubble, Rogues: we don't take rogues
- If you cannot remove Burn then move to the burn zone
- Don't Spread Burn! (2-3 yards)
- If you can heal or announce your last 5 seconds of Burn
**Bloodlusts**
- Early Lusts at 95% (Groups without execute phase or potential secondary Bloodlust)
- All other Bloodlusts at 25% (Including secondary or group swap lusts)

Burn - https://i.imgur.com/Ns4HWT9.png
Stomp - https://i.imgur.com/3R1v4xx.png

**Assignments**
```
/rw --- Brut ---
/rw Tank East - [Bear]
/rw Group East - [Group 3] + [Group 1]
/rw Tank West - [Warrior]
/rw Group West - [Group 4] + [Group 5]
/rw Burn Healers - [RDruid] [RDruid]
```
''')
    @commands.command(name='leadfelm', aliases=['felm'])
    async def leadfelm(self, ctx):
        await ctx.send('''Felm
Gas Nova
https://i.imgur.com/QbxyIia.png 
https://i.imgur.com/rqE2N5X.png 

**Encapsulate macro**
```
/use Nightmare Seed 
/use Major Arcane Protection Potion 
/use Master Healthstone 
/use Super Healing Potion 
/use Healing Potion Injector
```

**Assignments**
```
/rw --- Felm ---
/rw Tank - [Warrior]
/rw Group Melee - [Group 2]
/rw Group Left - [Group 1] 
/rw Group Middle - [Group 5] + [SPriest]
/rw Group Right - [Group 3] + [Group 4]
```
''')

    @commands.command(name='leadtwins', aliases=['twins'])
    async def leadtwins(self, ctx):
        await ctx.send('''**Twins**
Conflagration - https://i.imgur.com/Gafwn3E.png 
Flame Sear - https://i.imgur.com/owqf5xm.png
Pyrogenics - https://i.imgur.com/Fc16Fjg.png 

**Conflag timing macro**
_Press this macro as soon as the first conflag is announced_
```
/in 27 /rw --- CONFLAG #2 IN 5~ SECONDS ---
/in 59 /rw --- CONFLAG #3 IN 5~ SECONDS ---
/in 91 /rw --- CONFLAG #4 IN 5~ SECONDS ---
/in 123 /rw --- CONFLAG #5 IN 5~ SECONDS ---
/in 155 /rw --- CONFLAG #6 IN 5~ SECONDS ---
```
''')

    @commands.command(name='leadmuru', aliases=['muru'])
    async def leadmuru(self, ctx):
        await ctx.send('''**Muru assignment**
```
TODO
```

**Buffs/Debuffs**

Shadowsword Berserker - Flurry - https://i.imgur.com/aCd03m9.png
Shadowsword Fury Mage - Spell Fury - https://i.imgur.com/Faitnvf.png

**Macros**

Priest/Sham Single Dispell/Purge 
```
#showtooltip Dark Fiends
/target Dark Fiend
/cast Dispel Magic
/cast Purge
```

Spellsteal Macros
```
/stopcasting
/cast [target=mouseover,harm][] Spellsteal
```
```
/target shadowsword fury mage
/focus
/cast [target=focus,harm][] Spellsteal
```
''')

    @commands.command(name='leadkj', aliases=['kj'])
    async def leadkj(self, ctx):
        await ctx.send('''**Muru assignment**
```
TODO
```
''')

def setup(bot):
    bot.add_cog(Swp(bot))
