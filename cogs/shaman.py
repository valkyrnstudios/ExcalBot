import discord
from discord.ext import commands

class Shaman(commands.Cog, name='Shaman information'):
    def __init__(self, bot):
        self.bot = bot

    def _get_base_totems(self):
        return '''**Shaman macros**

**Single button fire totem**
```
/cast [nomod] Searing Totem; [mod:alt] Magma Totem; [mod] Fire Nova Totem
```
'''

    @commands.command(name='shaman')
    async def shaman(self, ctx):
        await ctx.send('''**Shaman**

**See `!totems`, `!spec enh`, `!spec ele`, and `!spec rsham` for spec-specific macros**

**Single button shield**
```
/cast [mod] Lightning Shield; [nomod] Water Shield
```

**Single button hearth**
```
/use [mod] Hearthstone
/cast [nomod] Astral Recall
```

**Single button mount**
```
/cast [nomod] Ghost Wolf; [mod:alt,flyable] FLYING_MOUNT; [mod] GROUND_MOUNT
```

**Show ankh timer, or use BL in combat**
```
/cast [mod:alt] Bloodlust; [combat] Bloodlust; [nocombat] Reincarnation
```
''')

    @commands.group(pass_context=True)
    async def totems(self, ctx):
        if ctx.invoked_subcommand is None:
            totems_list = []
            parents = self.get_commands()
            for cmd in self.walk_commands():
                if cmd not in parents:
                    cmd_line_str = f'* **{cmd.name}**'
                    if len(cmd.aliases) > 0:
                        cmd_line_str += ': [ ' + ' '.join(cmd.aliases) + ' ]'
                    if cmd_line_str not in totems_list:
                        totems_list.append(cmd_line_str)

            totems_str = f'Specific spec macros:\n' + '\n'.join(totems_list)
            if ctx.subcommand_passed != None:
                totems_str = f'Unknown Shaman spec: {ctx.subcommand_passed}\n' + totems_str
            await ctx.send(self._get_base_totems() + totems_str)

    @totems.command(name='enh', aliases=['enha'])
    async def _enhancement(self, ctx):
        await ctx.send('''**Enhancement totem macros**

**Primary enhance totem macro**
```
/castsequence [nomod] reset=8 Windfury Totem, Strength of Earth Totem, Mana Spring Totem, Searing Totem
/castsequence [mod] reset=8 Grace of Air Totem, Strength of Earth Totem, Mana Spring Totem, Searing Totem
```

**Twisting with obvious indicator of cycle time**
(WoA is yellow and easy to tell when it changes back to WF)
```
/castsequence [nomod] reset=7 Windfury Totem, Grace of Air Totem, Wrath of Air Totem
/cast [mod] Grace of Air Totem
```

''')

    @totems.command(name='resto', aliases=['rsham'])
    async def _restoration(self, ctx):
        await ctx.send('''**Restoration totem macro**
```
/castsequence [nomod] reset=8 Wrath of Air Totem, Mana Spring Totem, Strength of Earth Totem
/castsequence [mod] reset=8 Windfury Totem, Mana Spring Totem, Strength of Earth Totem
```

**Chain macro**
Rank 4 with rank 2 downrank
```
/cast [nomod,target=mouseover,exists][nomod,exists][nomod] Chain Heal(Rank 4)
/cast [mod,target=mouseover,exists][mod,exists][mod]Chain Heal(Rank 2)
```

''')

    @totems.command(name='ele', aliases=['elemental'])
    async def _elemental(self, ctx):
        await ctx.send('''**Elemental totem macros**
```
/castsequence [nomod] reset=8 Wrath of Air Totem, Mana Spring Totem, Totem of Wrath, Tremor Totem
/cast [mod] Totem of Wrath
```

''')

def setup(bot):
    bot.add_cog(Shaman(bot))
