from os import environ
from bot import Zect
import sys

bot = Zect()




extensions = [
    "cogs.manage",
    "cogs.instant",
]
for extension in extensions:
    bot.load_extension(extension)

bot.run(environ["BOT_TOKEN"])

# bot.run(BOT_TOKEN)
