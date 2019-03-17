import discord
from discord.ext import commands

class Specs(commands.Cog, name='Spec commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='talents')
    async def talents(self, ctx):
        talents_list = []
        parents = self.get_commands()
        for cmd in self.walk_commands():
            if cmd not in parents:
                cmd_line_str = f'* **{cmd.name}**'
                if len(cmd.aliases) > 0:
                    cmd_line_str += ': [ ' + ' '.join(cmd.aliases) + ' ]'
                if cmd_line_str not in talents_list:
                    talents_list.append(cmd_line_str)

        talents_str = 'Available specs:\n' + '\n'.join(talents_list)
        await ctx.send(talents_str)

    @commands.group(pass_context=True)
    async def spec(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Unknown spec: {0.subcommand_passed}'.format(ctx))

    @spec.command(name='coh', aliases=['mshate', 'cozzmo', 'priestsk'])
    async def _speccoh(self, ctx):
        await ctx.send('Spec CoH')

    @spec.command(name='enh', aliases=['enha'])
    async def _specenh(self, ctx):
        await ctx.send('''**Enhancement Shaman Spec**

http://db.excalibur.ws/?talent#hZxVbdVMsAuqoxbez
https://i.imgur.com/bwUt36c.png

**Single button proper weapon imbues** - https://forum.excalibur.ws/topic/1091-enhancement-weapon-imbues/
Left-click twice to apply, right-click to remove.
```
/castsequence [nobtn:2] reset=3 Windfury Weapon, Flametongue Weapon
/stopmacro [nobtn:2]
/run local c=CancelItemTempEnchantment c(1) c(2)
```
''')

    @spec.command(name='surv', aliases=['survival', 'sv'])
    async def _specsurv(self, ctx):
        await ctx.send('''**Survival Hunter Spec**
http://db.excalibur.ws/?talent#cxbZVxbRVZIhoMxcMhVbb
https://i.imgur.com/NBfiDo6.png
''')

    @spec.command(name='bm')
    async def _specbm(self, ctx):
        await ctx.send('''**BM Hunter Spec**
http://db.excalibur.ws/?talent#ctbMztxRwuVoVVbRV
https://i.imgur.com/uQkoYDP.png
''')

    @spec.command(name='mm', aliases=['marksman'])
    async def _specbm(self, ctx):
        await ctx.send('''**Marksman Hunter Spec**
No, go to Wrath+.
''')

    @spec.command(name='feral', aliases=['bear'])
    async def _specferal(self, ctx):
        await ctx.send('''**Feral Druid Spec**
http://db.excalibur.ws/?talent#0ZxhGsfroezioVxIz
https://i.imgur.com/BS7Wwwi.png
''')

    @spec.command(name='rdruid', aliases=['rdudu'])
    async def _specrdruid(self, ctx):
        await ctx.send('''**Resto Druid Spec**
http://db.excalibur.ws/?talent#0LZZxVIxeqrest
https://i.imgur.com/Mj6AsJt.png
''')

    @spec.command(name='moonkin', aliases=['oomkin', 'boomkin'])
    async def _specmoonkin(self, ctx):
        await ctx.send('''**Boomkin Druid Spec**
http://db.excalibur.ws/?talent#0xzrdicsguAZZxMIb
https://i.imgur.com/MeUKJbL.png
''')

def setup(bot):
    bot.add_cog(Specs(bot))
