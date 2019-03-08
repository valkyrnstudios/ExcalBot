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
        await ctx.send('Spec Enhancement')

def setup(bot):
    bot.add_cog(Specs(bot))
