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

    async def move(self,cel,ctx):
        print("VCの強制移動")
        for id in cel.jobs.keys():
            mem = ctx.guild.get_member(id)
            chan = discord.utils.get(ctx.guild.voice_channels, name="会議所")
            await mem.edit(voice_channel=chan)


    async def box(self,cel,ctx,title):
        txt = ""
        for i, id in enumerate(cel.jobs.keys()):
            txt += f"\n{self.count[i]}. <@{id}>"

        test = discord.Embed(title=title,colour=0x1e90ff)
        test.add_field(name="プレイヤー一覧", value=txt, inline=True)
        msg = await ctx.send(embed=test)

        for i, id in enumerate(cel.jobs.keys()):
            await msg.add_reaction(self.ment[i])


    def select(self,mem):
        if mem == 1:
            return ["市民", "人狼"]
        if mem == 2:
            return ["市民", "人狼"]
        if mem == 3:
            return ["市民", "占い師", "人狼"]
        if mem == 4:
            return ["市民", "市民", "占い師", "人狼"]
        if mem == 5:
            return ["市民", "市民", "市民", "占い師", "人狼"]
        if mem == 6:
            return ["市民", "市民", "霊媒師", "占い師", "狂人", "人狼"]
        if mem == 7:
            return ["市民", "市民", "市民", "霊媒師", "占い師", "狂人", "人狼"]
        if mem == 8:
            return ["市民", "市民", "市民", "霊媒師", "占い師", "狂人", "人狼", "人狼"]
        if mem == 9:
            return ["市民", "市民", "市民", "市民", "霊媒師", "占い師", "狂人", "人狼", "人狼"]
        if mem == 10:
            return ["市民", "市民", "市民", "市民", "てるてる", "霊媒師", "占い師", "狂人", "人狼", "人狼"]
        if mem == 11:
            return ["市民", "市民", "市民", "市民", "市民", "てるてる", "霊媒師", "占い師", "狂人", "人狼", "人狼"]
        if mem == 12:
            return ["市民", "市民", "市民", "市民", "てるてる", "霊媒師", "占い師", "占い師", "狂人", "人狼", "人狼", "人狼"]
        if mem == 13:
            return ["市民", "市民", "市民", "市民", "市民", "てるてる", "霊媒師", "占い師", "占い師", "狂人", "人狼", "人狼", "人狼"]
        if mem == 14:
            return ["市民", "市民", "市民", "市民", "市民", "市民", "てるてる", "霊媒師", "占い師", "占い師", "狂人", "人狼", "人狼", "人狼"]
        if mem == 15:
            return ["市民", "市民", "市民", "市民", "市民", "市民", "市民", "てるてる", "霊媒師", "占い師", "占い師", "狂人", "人狼", "人狼", "人狼"]
        if mem == 16:
            return ["市民", "市民", "市民", "市民", "市民", "市民", "市民", "市民", "てるてる", "霊媒師", "占い師", "占い師", "狂人", "人狼", "人狼", "人狼"]
        if mem == 17:
            return ["市民", "市民", "市民", "市民", "市民", "市民", "市民", "市民", "市民", "てるてる", "霊媒師", "占い師", "占い師", "狂人", "人狼", "人狼", "人狼"]
        if mem == 18:
            return ["市民", "市民", "市民", "市民", "市民", "市民", "市民", "市民", "市民", "市民", "霊媒師", "占い師", "占い師", "狂人", "人狼", "人狼", "人狼", "人狼"]
        if mem == 19:
            return ["市民", "市民", "市民", "市民", "市民", "市民", "市民", "市民", "市民", "市民", "てるてる", "霊媒師", "占い師", "占い師", "狂人", "人狼", "人狼", "人狼", "人狼"]
        if mem == 20:
            return ["市民", "市民", "市民", "市民", "市民", "市民", "市民", "市民", "市民", "市民", "てるてる", "霊媒師", "占い師", "占い師", "占い師", "狂人", "人狼", "人狼", "人狼", "人狼"]


    def job(self,cel,ctx):
        mems = cel.mems
        mem = len(mems.keys())
        role = self.select(mem)
        # print(role)
        random.shuffle(role)
        # print(role)
        job = {}
        ids = mems.keys()
        for i, id in enumerate(ids):
            job[id] = role[i]
        print(job)
        return job



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
