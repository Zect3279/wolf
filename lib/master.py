# start.py

import discord
from discord.ext import commands

import json
import random
import asyncio
import os
import sys
from typing import Union, Any, List, Tuple


global anser
anser = False


class Master():
    def __init__(self, bot: Any):
        self.bot = bot
        self.count = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]
        self.ment = ["🇦","🇧","🇨","🇩","🇪","🇫","🇬","🇭","🇮","🇯","🇰","🇱","🇲","🇳","🇴","🇵","🇶","🇷","🇸","🇹",]

    async def yes(self,ctx):
        print("yes")

    async def call(self,cel,ctx):
        for id in cel.jobs.keys():
            role = cel.jobs[id]
            channel = discord.utils.get(ctx.guild.text_channels, name=role)
            await channel.send(f"<@{id}> あなたは、 __{role}__ です。")

    async def box(self,cel,ctx,title):
        txt = ""
        for i, id in enumerate(cel.jobs.keys()):
            txt += f"\n{self.count[i]}. <@{id}>"

        test = discord.Embed(title=title,colour=0x1e90ff)
        test.add_field(name="プレイヤー一覧", value=txt, inline=True)
        msg = await ctx.send(embed=test)

        for i, id in enumerate(cel.jobs.keys()):
            await msg.add_reaction(self.ment[i])


# cel_mems = {
#     member.id : member.name
# }
#
#
# job_sample = {
#     member.id : "wolf",
#     member.id : "wolf",
#     member.id : "wolf",
# }
