# start.py

import discord
from discord.ext import commands

import json
import random
import asyncio
import os
import sys
from dispander import dispand


global anser
anser = False

# vq.cmdから渡された引数を格納したリストの取得
argvs = sys.argv


class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print('Start')

    @commands.Cog.listener()
    async def on_message(self, message):
        await dispand(message)


    @commands.command()
    async def start(self,ctx):
        print("yes")



















































def setup(bot):
    bot.add_cog(Game(bot))
