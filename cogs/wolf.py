# start.py

import discord
from discord.ext import commands

import json
import random
import asyncio
import os
import sys
from dispander import dispand
import asyncio

from lib.instant import inst
from lib.master import Master



class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.joiner = False
        self.mems = {}
        self.live = []
        self.dead = []
        self.on_game = False
        self.instant = inst(bot)
        self.game = Master(bot)


    @commands.Cog.listener()
    async def on_ready(self):
        print('Wolf had started')

    @commands.Cog.listener()
    async def on_message(self, message):
        await dispand(message)

    # @commands.Cog.listener()
    # async def on_voice_state_update(self,member,before,after):
    #     if after.channel.guild.name != "鯖改造":
    #         return
    #     Grole = discord.utils.get(before.channel.guild.roles, name="人狼参加者")
    #     if before.channel == after.channel:
    #         return
    #     try:
    #         cname = before.channel.name
    #         if cname != "観戦中":
    #             return
    #         channel = discord.utils.get(before.channel.guild.voice_channels, name=cname)
    #         role = discord.utils.get(before.channel.guild.roles, name=cname)
    #         await member.remove_roles(role)
    #         await channel.send(f"{member.name} が退出しました。")
    #     except:
    #         a = "a"
    #     finally:
    #         try:
    #             cname = after.channel.name
    #             if cname != "観戦中":
    #                 return
    #             channel = discord.utils.get(after.channel.guild.voice_channels, name=cname)
    #             role = discord.utils.get(after.channel.guild.roles, name=cname)
    #             await member.add_roles(role)
    #             await channel.send(f"{member.name} が参加しました。")
    #         except:
    #             a = "a"
    #         finally:
    #             a = "a"

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

    @commands.command()
    async def delete(self,ctx):
        if self.on_game == True:
            return
        await self.instant.dele(ctx)

    async def count(self,ctx):
        self.joiner = 0
        self.mems = {}
        await ctx.send("開始を確認...\n参加希望の方は、`/join` と入力してください。")
        edit = await ctx.send("開始まで10秒")
        self.joiner = True
        for i in range(10):
            num = 10 - i
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
        await self.game.call(cel,ctx)
        await self.game.box(cel,ctx,"＜未設定＞")
        await self.play(ctx)



    async def play(self,ctx):
        print("play has called")












































def setup(bot):
    bot.add_cog(Game(bot))
