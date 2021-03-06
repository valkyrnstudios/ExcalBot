import discord
from discord.ext import commands
import json

# Based on https://gist.github.com/OneEyedKnight/f0411f9a5e9dea23b96be0bf6dd86d2d#file-owner-py

class OwnerCog(commands.Cog, name='Owner commands', command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot
        with open('config.json') as json_data_file:
            self.cogs_dir = json.load(json_data_file)['COGS_DIR']
    
    # Hidden means it won't show up on the default help.
    @commands.command(name='load')
    @commands.is_owner()
    async def cog_load(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='unload')
    @commands.is_owner()
    async def cog_unload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='reload')
    @commands.is_owner()
    async def cog_reload(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            try:
                self.bot.unload_extension(f'{self.cogs_dir}.{cog}')
                self.bot.load_extension(f'{self.cogs_dir}.{cog}')
            except Exception as e:
                await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
            else:
                await ctx.send('**`SUCCESS`**')
        else:
            await ctx.send('**`SUCCESS`**')

def setup(bot):
    bot.add_cog(OwnerCog(bot))
