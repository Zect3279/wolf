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

    async def yes(self,ctx):
        print("yes")

    async def move(self,cel,ctx):
        for id in cel.jobs.keys():
            mem = ctx.guild.get_member(id)
            role = discord.utils.get(ctx.guild.roles, name="生存者")
            await mem.add_roles(role)
            chan = discord.utils.get(ctx.guild.voice_channels, name="移動用")
            await mem.edit(voice_channel=chan)

    def select(self,mem):
        if mem == 1:
            # return ["市民", "人狼"]
            return ["人狼", "人狼"]
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
