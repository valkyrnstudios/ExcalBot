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

prefix_separators = config['PREFIX_SEPARATORS']

bot = commands.Bot(
    case_insensitive=True,
    command_prefix=commands.when_mentioned_or(config['BOT_PREFIX']),
    description=config['BOT_DESCRIPTION'])

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    message.content = message.content.lower()
    print(f'"Original {message.content}"')

    for prefix in prefix_separators:
        if message.content.startswith(prefix, 1) and not message.content.startswith(f'{prefix} ', 1):
            message.content = message.content.replace(prefix, f'{prefix} ')
            break

    print(f'"Transformed {message.content}"')

    await bot.process_commands(message)

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
