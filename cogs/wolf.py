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



class Wolf(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.joiner = False
        self.mems = {}
        self.live = []
        self.dead = []
        self.on_game = False
        self.on_voice = False
        self.instant = inst(bot)
        self.game = Master(bot)
        self.cont = Game(bot)

    def times(self):
        dt_now = datetime.datetime.now()
        txt = f"[{dt_now.hour}:{dt_now.minute}:{dt_now.second}]"
        return txt

    @commands.command()
    async def end(self):
        self.on_voice = False

    @commands.command()
    async def on(self,ctx):
        self.on_voice = True

    @commands.command()
    async def look(self,ctx,member: discord.Member):
        print(f"{self.times} [look] : {member.name} is able to look All-Channels!")
        role = discord.utils.get(ctx.guild.roles, name="観戦者")
        await member.add_roles(role)
        role = discord.utils.get(ctx.guild.roles, name="生存者")
        await member.add_roles(role)
        role = discord.utils.get(ctx.guild.roles, name="死亡者")
        await member.add_roles(role)

    @commands.command()
    async def kill(self,ctx,member: discord.Member):
        print(f"{self.times} [kill] : {member.name} is dead")
        role = discord.utils.get(ctx.guild.roles, name="生存者")
        await member.remove_roles(role)
        role = discord.utils.get(ctx.guild.roles, name="死亡者")
        await member.add_roles(role)

    @commands.command()
    async def live(self,ctx,member: discord.Member):
        print(f"{self.times} [live] : {member.name} is alive!")
        role = discord.utils.get(ctx.guild.roles, name="死亡者")
        await member.remove_roles(role)
        role = discord.utils.get(ctx.guild.roles, name="生存者")
        await member.add_roles(role)

    @commands.Cog.listener()
    async def on_ready(self):
        print('Wolf had started')

    @commands.Cog.listener()
    async def on_message(self, message):
        await dispand(message)

    @commands.Cog.listener()
    async def on_voice_state_update(self,member,before,after):
        if self.on_voice == False:
            return
        if before.channel == after.channel:
            return
        try:
            if before.channel.guild.id != 726233332655849514:
                return
            cname = before.channel.name
            if cname != "観戦中":
                return
            role = discord.utils.get(before.channel.guild.roles, name="観戦者")
            await member.remove_roles(role)
            print(f"{self.times} [Connection] : Removed {member.name} `s '観戦者'")
        except:
            a = "a"
        finally:
            try:
                if after.channel.guild.id != 726233332655849514:
                    return
                cname = after.channel.name
                if cname != "総合チャット":
                    return
                role = discord.utils.get(after.channel.guild.roles, name="生存者")
                if role in member.roles:
                    channel = discord.utils.get(after.channel.guild.voice_channels, name="会議所")
                    await member.edit(voice_channel=channel)
                    print(f"{self.times} [Connection] : {member.name} has connected into '会議所'")
                    return
                role = discord.utils.get(after.channel.guild.roles, name="死亡者")
                if role in member.roles:
                    channel = discord.utils.get(after.channel.guild.voice_channels, name="反省会")
                    print(f"{self.times} [Connection] : {member.name} has connected into '反省会'")
                    await member.edit(voice_channel=channel)
                    return
                channel = discord.utils.get(after.channel.guild.voice_channels, name="観戦中")
                role = discord.utils.get(after.channel.guild.roles, name="観戦者")
                await member.edit(voice_channel=channel)
                print(f"{self.times} [Connection] : {member.name} has connected into '観戦中'")
                await member.add_roles(role)
            except:
                a = "a"
            finally:
                a = "a"

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
        edit = await ctx.send("開始まで30秒")
        self.joiner = True
        for i in range(30):
            num = 30 - i
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
        make_channel = asyncio.create_task(self.instant.make(ctx))
        add_member = asyncio.create_task(self.count(ctx))
        await make_channel
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
        self.on_voice = True
        self.jobs = self.game.job(cel,ctx)
        await ctx.send(self.jobs)
        # await self.game.box(cel,ctx,"＜未設定＞")
        await self.play(ctx)
        self.cont.on(self.jobs)

        # await self.end()


    async def play(self,ctx):
        ids = self.jobs.keys()
        for id in ids:
            job = self.jobs[id]
            mem = ctx.guild.get_member(id)
            role = await ctx.guild.create_role(name=mem.name)
            chan = discord.utils.get(ctx.guild.text_channels, name=job)
            await chan.set_permissions(role,read_messages=True)
            await mem.add_roles(role)

        cel = self
        await self.game.move(cel,ctx)
        channel = discord.utils.get(ctx.guild.text_channels, name="会議所")
        await channel.send("@everyone\n全員に役職を付与しました。\nそれぞれの専用チャンネルにてメンションが飛びます。\n確認してください。")
        await self.game.call(cel,ctx)












































def setup(bot):
    bot.add_cog(Wolf(bot))
