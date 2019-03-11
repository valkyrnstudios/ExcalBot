import logging

logFormatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s')

discordLogger = logging.getLogger('discord')
discordLogger.setLevel(logging.INFO)
discordFileHandler = logging.FileHandler(filename='logs/app.log', encoding='utf-8', mode='a')
discordFileHandler.setFormatter(logFormatter)
discordLogger.addHandler(logging.FileHandler(filename='logs/discord.log', encoding='utf-8', mode='w'))

rootLogger = logging.getLogger('excal_bot')
rootLogger.setLevel(logging.INFO)

fileHandler = logging.FileHandler(filename='logs/app.log', encoding='utf-8', mode='a')
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)
