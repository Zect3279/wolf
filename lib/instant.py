# start.py

import discord
from discord.ext import commands

import json
import random
import asyncio
import os
import sys


global anser
anser = False

# vq.cmdから渡された引数を格納したリストの取得

class instant:

    def __init__(self, bot: Any):
        self.bot = bot
        
    async def wolf(self,ctx):
        await ctx.guild.create_text_channel("welcome")


        category = await ctx.guild.create_category(name="自由部屋")
        await category.create_text_channel("自由部屋①")
        await category.create_text_channel("自由部屋②")
        await category.create_text_channel("自由部屋③")
        voice = await category.create_voice_channel("自由部屋①")
        await voice.edit(user_limit=50)
        voice = await category.create_voice_channel("自由部屋②")
        await voice.edit(user_limit=50)
        voice = await category.create_voice_channel("自由部屋③")
        await voice.edit(user_limit=50)




            if ins[0] == "labo":
                category = await ctx.guild.create_category(name="研究所")
                chan = await category.create_text_channel("bot研究室")
                voice = await category.create_voice_channel("会議室")
                await voice.edit(user_limit=50)
                role = await ctx.guild.create_role(name="研究員",colour=discord.Colour.from_rgb(0, 255, 255))
                text = f"{ins[0]} の実行が完了しました。"
                await ctx.send(text)
                await chan.set_permissions(ctx.guild.roles[0],read_messages=False)
                await chan.set_permissions(ctx.author,read_messages=True)
                # await chan.set_permissions(role,read_messages=True)
                await voice.set_permissions(ctx.guild.roles[0],read_messages=False)
                await voice.set_permissions(ctx.author,read_messages=True)
                # await voice.set_permissions(role,read_messages=True)

















































def setup(bot):
    bot.add_cog(Game(bot))
