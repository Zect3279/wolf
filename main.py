from os import environ
from bot import Zect
import sys

bot = Zect()




extensions = [
    # "cogs.help",
    "cogs.wolf",
    "cogs.controller",
    "cogs.test",
]
for extension in extensions:
    bot.load_extension(extension)

bot.run(environ["BOT_TOKEN"])

# bot.run(BOT_TOKEN)
