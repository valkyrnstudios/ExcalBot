import logging

class Analytics:
    def __init__(self):
        self.logger = logging.getLogger('analytics')
        self.logger.setLevel(logging.INFO)
        fileHandler = logging.FileHandler(filename='logs/analytics.csv', encoding='utf-8', mode='a')
        self.logger.addHandler(fileHandler)

    def log_message(self, message):
        if message.author.bot:
            return
        self.logger.info(f'{message.author.name},{message.guild.name},{message.content}')
