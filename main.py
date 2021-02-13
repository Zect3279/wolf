from os import environ
from bot import Zect
import sys

bot = Zect()




bot.load_extension(f"cogs.wolf")

bot.run(environ["BOT_TOKEN"])

# bot.run(BOT_TOKEN)
