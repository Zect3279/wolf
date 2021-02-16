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
from cogs.controller import Game



class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.on_game = False
        self.check = False


    # @commands.Cog.listener()
    # async def on_voice_state_update(self,member,before,after):
    #     if self.on_game == False:
    #         return
    #     if before.channel == after.channel:
    #         return
    #     try:
    #         if after.channel.guild.id != 726233332655849514:
    #             return
    #         cname = after.channel.name
    #         if cname != "移動用":
    #             return
    #         channel = discord.utils.get(after.channel.guild.voice_channels, name="観戦中")
    #         await member.edit(voice_channel=channel)
    #         print("ok")
    #     except:
    #         print("not")
    #
    # @commands.command()
    # async def yeah(self,ctx):
    #     self.on_game = True
    #     channel = discord.utils.get(ctx.guild.voice_channels, name="移動用")
    #     await ctx.author.edit(voice_channel=channel)
    #     await ctx.send("ok")


    async def abcd(self,ctx):
        self.check = True
        print("done")

    @commands.command()
    async def checking(self,ctx):
        if self.check == True:
            check = True
        if self.check == False:
            check = False
        await ctx.send(f"self.check is {check}")


































def setup(bot):
    bot.add_cog(Test(bot))
