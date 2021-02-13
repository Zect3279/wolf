# start.py

import discord
from discord.ext import commands

import json
import random
import asyncio
import os
import sys
from dispander import dispand

import lib.instant




class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print('Wolf had started')

    @commands.Cog.listener()
    async def on_message(self, message):
        await dispand(message)

    @commands.command()
    async def ready(self,ctx):
        for chan in ctx.guild.channels:
            await chan.delete()

        channel = await ctx.guild.create_text_channel("welcome")
        for rol in all_role:
            try:
                await rol.delete()
            except:
                a = "a"

        category = await ctx.guild.create_category(name="総合")
        await category.create_text_channel("総合チャット")
        voice = await category.create_voice_channel("総合チャット")
        await voice.edit(user_limit=99)

    @commands.command()
    async def start(self,ctx):
        await ctx.send("開始を確認...\n参加希望の方は、`/join` と入力してください。")
        edit = await ctx.send("開始まで10秒")
        for i in range(10):
            await edit.edit(f"開始まで{i}秒")
        await edit.delete()
        await ctx.send("開始します。")
        # await instant.wolf(self,ctx)




# 人狼２
# 市民３
# 占い師１
# 霊媒師１
# 狩人１
# 狂人１














































def setup(bot):
    bot.add_cog(Game(bot))
