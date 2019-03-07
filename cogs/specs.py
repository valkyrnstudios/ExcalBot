import discord
from discord.ext import commands

class Specs(commands.Cog, name='Spec commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def spec(self, ctx):
        """Says if a user is cool.

        In reality this just checks if a subcommand is being invoked.
        """
        if ctx.invoked_subcommand is None:
            try:
                pass
            except Exception as e:
                await ctx.send('Unknown spec: {0.subcommand_passed}'.format(ctx))

    @spec.command(name='coh')
    async def _speccoh(self, ctx):
        await ctx.send('Spec coh')

def setup(bot):
    bot.add_cog(Specs(bot))
