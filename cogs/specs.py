import discord
from discord.ext import commands

class Specs(commands.Cog, name='Spec commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='talents')
    async def talents(self, ctx):
        parents = self.get_commands()
        talents_list = []

        for cmd in self.walk_commands():
            if cmd not in parents:
                #print (vars(cmd))
                if cmd.name not in talents_list:
                    talents_list.append(cmd.name)

                for cmdalias in cmd.aliases:
                    if cmdalias not in talents_list:
                        talents_list.append(cmdalias)

        talents_str = 'Available specs:\n* ' + '\n* '.join(talents_list)
        await ctx.send(talents_str)

    @commands.group(pass_context=True)
    async def spec(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Unknown spec: {0.subcommand_passed}'.format(ctx))

    @spec.command(name='coh', aliases=['mshate', 'cozzmo', 'pristsk'])
    async def _speccoh(self, ctx):
        await ctx.send('Spec CoH')

    @spec.command(name='enh', aliases=['enha'])
    async def _specenh(self, ctx):
        await ctx.send('Spec Enhancement')

def setup(bot):
    bot.add_cog(Specs(bot))
