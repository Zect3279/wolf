# start.py

import discord
from discord.ext import commands

import json
import datetime
import random
import asyncio
import os
import sys
from dispander import dispand
import asyncio

from lib.instant import inst
from lib.master import Master



class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.joiner = False
        self.jobs = {}
        self.live = []
        self.dead = []
        self.on_game = False
        self.instant = inst(bot)
        self.game = Master(bot)


    async def on(self,ctx,jobs):
        self.on_game = True
        self.jobs = jobs
        await self.start(ctx)

    async def start(self,ctx):
        channel = discord.utils.get(ctx.guild.text_channels, name="会議所")
        await channel.send("ゲームが開始されました。")
        await asyncio.gather(
            self.wolf(ctx),
            self.fortun(ctx)
        )



































def setup(bot):
    bot.add_cog(Game(bot))
