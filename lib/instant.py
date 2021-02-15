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


class inst():
    def __init__(self, bot: Any):
        self.bot = bot

    async def make(self,ctx):
        on_role = await ctx.guild.create_role(name="人狼参加者")
        live_role = await ctx.guild.create_role(name="生存者")
        dead_role = await ctx.guild.create_role(name="死亡者")
        no_role = await ctx.guild.create_role(name="観戦者")

        # self.mems = await lol.cho(self.mems)

        category = await ctx.guild.create_category(name="生存者")
        chan = await category.create_text_channel("会議所")
        await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
        await chan.set_permissions(on_role,read_messages=True)
        voice = await category.create_voice_channel("会議所")
        await voice.edit(user_limit=50)
        await voice.set_permissions(ctx.guild.roles[0],connect=False,speak=False)

        category = await ctx.guild.create_category(name="役職")
        chan = await category.create_text_channel("市民")
        await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
        await chan.set_permissions(dead_role,read_messages=True)
        await chan.set_permissions(no_role,read_messages=True)
        chan = await category.create_text_channel("人狼")
        await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
        await chan.set_permissions(dead_role,read_messages=True)
        await chan.set_permissions(no_role,read_messages=True)
        chan = await category.create_text_channel("占い師")
        await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
        await chan.set_permissions(dead_role,read_messages=True)
        await chan.set_permissions(no_role,read_messages=True)
        chan = await category.create_text_channel("霊媒師")
        await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
        await chan.set_permissions(dead_role,read_messages=True)
        await chan.set_permissions(no_role,read_messages=True)
        chan = await category.create_text_channel("狩人")
        await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
        await chan.set_permissions(dead_role,read_messages=True)
        await chan.set_permissions(no_role,read_messages=True)
        chan = await category.create_text_channel("狂人")
        await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
        await chan.set_permissions(dead_role,read_messages=True)
        await chan.set_permissions(no_role,read_messages=True)
        chan = await category.create_text_channel("てるてる")
        await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
        await chan.set_permissions(dead_role,read_messages=True)
        await chan.set_permissions(no_role,read_messages=True)

        category = await ctx.guild.create_category(name="死亡者")
        chan = await category.create_text_channel("反省会")
        await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
        await chan.set_permissions(dead_role,read_messages=True)
        voice = await category.create_voice_channel("反省会")
        await voice.edit(user_limit=50)
        await voice.set_permissions(ctx.guild.roles[0],connect=False)

        category = await ctx.guild.create_category(name="不参加者")
        chan = await category.create_text_channel("観戦")
        await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
        await chan.set_permissions(no_role,read_messages=True)
        voice = await category.create_voice_channel("観戦中")
        await voice.edit(user_limit=99)
        await voice.set_permissions(ctx.guild.roles[0],connect=False)


    async def dele(self,ctx):
        all_role = ctx.guild.roles
        for rol in all_role:
            try:
                await rol.delete()
            except:
                a = "a"
        channel = discord.utils.get(ctx.guild.text_channels, name='観戦')
        for chan in channel.category.channels:
            await chan.delete()
        await channel.category.delete()
        channel = discord.utils.get(ctx.guild.text_channels, name='反省会')
        for chan in channel.category.channels:
            await chan.delete()
        await channel.category.delete()
        channel = discord.utils.get(ctx.guild.text_channels, name='市民')
        for chan in channel.category.channels:
            await chan.delete()
        await channel.category.delete()
        channel = discord.utils.get(ctx.guild.text_channels, name='会議所')
        for chan in channel.category.channels:
            await chan.delete()
        await channel.category.delete()






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
