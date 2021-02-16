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
from cogs.test import Test



class Wolf(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.joiner = False
        self.mems = {}
        self.on_game = False
        self.instant = inst(bot)
        self.game = Master(bot)
        self.cont = Game(bot)
        self.test = Test(bot)

    @commands.command()
    async def testing(self,ctx):
        await self.test.abcd(ctx)



    def times(self):
        dt_now = datetime.datetime.now()
        txt = f"[{dt_now.hour}:{dt_now.minute}:{dt_now.second}]"
        return txt

    @commands.Cog.listener()
    async def on_ready(self):
        print('Wolf had started')

    @commands.Cog.listener()
    async def on_message(self, message):
        await dispand(message)

    @commands.command()
    async def ready(self,ctx):
        if self.on_game == True:
            return
        for chan in ctx.guild.channels:
            await chan.delete()

        all_role = ctx.guild.roles
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
        print(f"{self.times} [ready] : {ctx.author.name} has refreshed!")

    @commands.command()
    async def delete(self,ctx):
        if self.on_game == True:
            return
        await self.instant.dele(ctx)
        print(f"{self.times} [delete] : {ctx.author.name} has deleted All!")

    async def count(self,ctx):
        self.joiner = 0
        self.mems = {}
        await ctx.send("開始を確認...\n参加希望の方は、`/join` と入力してください。")
        count = 10
        edit = await ctx.send(f"開始まで{count}秒")
        self.joiner = True
        for i in range(count):
            num = count - i
            await edit.edit(content=f"開始まで{num}秒")
            await asyncio.sleep(0.9)
        self.joiner = False
        await edit.delete()
        await ctx.send("参加者が決定しました。")

    @commands.command()
    async def join(self,ctx):
        if self.joiner == False:
            return
        if ctx.author.id in self.mems:
            return
        self.mems[ctx.author.id] = ctx.author.name
        # chan = discord.utils.get(ctx.guild.voice_channels, name="総合チャット")
        # await ctx.author.edit(voice_channel=chan)
        role = discord.utils.get(ctx.guild.roles, name="人狼参加者")
        await ctx.author.add_roles(role)
        await ctx.message.add_reaction("⭕")

    @commands.command()
    async def start(self,ctx):
        if self.on_game == True:
            return
        self.on_game = True
        # make_channel = asyncio.create_task(self.instant.make(ctx))
        add_member = asyncio.create_task(self.count(ctx))
        # await make_channel
        await add_member
        if not self.mems:
            await ctx.send("no one")
            return
        # print(self.mems)
        # if len(self.mems) <= 3:
        #     await ctx.send("参加を希望したのが3名以下だったため、開始できません。\n停止します...")
        #     return
        # txt = "```\n"
        # for name in self.mems.values():
        #     txt += f"・{name}\n"
        # await ctx.send(f"{txt}```")
        cel = self
        self.jobs = self.game.job(cel,ctx)
        await ctx.send(self.jobs)
        await self.cont.on(ctx,self.jobs)












































def setup(bot):
    bot.add_cog(Wolf(bot))
