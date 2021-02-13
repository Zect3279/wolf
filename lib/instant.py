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

# vq.cmdから渡された引数を格納したリストの取得

class instant:

    def __init__(self, bot: Any):
        self.bot = bot

    async def wolf(self,cel,ctx,mems):
        self.mems = cel.mems

        # self.mems = await lol.cho(self.mems)

        category = await ctx.guild.create_category(name="生存者")
        await category.create_text_channel("会議所")
        voice = await category.create_voice_channel("会議所")
        await voice.edit(user_limit=50)

        category = await ctx.guild.create_category(name="役職")
        chan = await category.create_text_channel("市民")
        # await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
        # await chan.set_permissions(self.mems.cit,read_messages=True)
        chan = await category.create_text_channel("人狼")
        # await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
        # await chan.set_permissions(self.mems.wolf,read_messages=True)
        chan = await category.create_text_channel("占い師")
        # await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
        # await chan.set_permissions(self.mems.for,read_messages=True)
        chan = await category.create_text_channel("霊媒師")
        # await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
        # await chan.set_permissions(self.mems.med,read_messages=True)
        chan = await category.create_text_channel("狩人")
        # await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
        # await chan.set_permissions(self.mems.han,read_messages=True)
        chan = await category.create_text_channel("狂人")
        # await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
        # await chan.set_permissions(self.mems.mad,read_messages=True)

        category = await ctx.guild.create_category(name="志望者")
        await category.create_text_channel("反省会")
        voice = await category.create_voice_channel("反省会")
        await voice.edit(user_limit=50)



            # if ins[0] == "labo":
            #     category = await ctx.guild.create_category(name="研究所")
            #     chan = await category.create_text_channel("bot研究室")
            #     voice = await category.create_voice_channel("会議室")
            #     await voice.edit(user_limit=50)
            #     role = await ctx.guild.create_role(name="研究員",colour=discord.Colour.from_rgb(0, 255, 255))
            #     text = f"{ins[0]} の実行が完了しました。"
            #     await ctx.send(text)
            #     await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
            #     await chan.set_permissions(ctx.author,read_messages=True)
            #     # await chan.set_permissions(role,read_messages=True)
            #     await voice.set_permissions(ctx.guild.roles[0],read_messages=False)
            #     await voice.set_permissions(ctx.author,read_messages=True)
            #     # await voice.set_permissions(role,read_messages=True)

















































def setup(bot):
    bot.add_cog(Game(bot))
