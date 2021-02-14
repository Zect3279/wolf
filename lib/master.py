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
