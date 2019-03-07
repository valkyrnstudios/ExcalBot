import json
import asyncio
import traceback
import discord

from discord import Game, Status
from discord.ext import commands

from os import listdir
from os.path import isfile, join

with open('config.json') as json_data_file:
    config = json.load(json_data_file)

bot = commands.Bot(
    case_insensitive=True,
    command_prefix=commands.when_mentioned_or(config['BOT_PREFIX']),
    description=config['BOT_DESCRIPTION'])

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    await bot.change_presence(status=Status.online, activity=Game(name='Waiting to be helpful'))

if __name__ == "__main__":
    cogs_dir = config['COGS_DIR']

    for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
        try:
            bot.load_extension(cogs_dir + "." + extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.')
            traceback.print_exc()

    bot.run(config['BOT_TOKEN'])
