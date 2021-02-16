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



class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.joiner = False
        self.jobs = {}
        self.live = []
        self.dead = []
        self.count = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]
        self.ment = ["🇦","🇧","🇨","🇩","🇪","🇫","🇬","🇭","🇮","🇯","🇰","🇱","🇲","🇳","🇴","🇵","🇶","🇷","🇸","🇹",]
        self.on_game = False
        self.instant = inst(bot)
        self.game = Master(bot)


    @commands.Cog.listener()
    async def on_voice_state_update(self,member,before,after):
        if self.on_game == False:
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
                    print(0)
                    return
                cname = after.channel.name
                if cname != "移動用":
                    print(1)
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
                print(2)
                a = "a"
            finally:
                print(3)
                a = "a"

    def yes(self):
        self.on_game = True

    def no(self):
        self.on_game = False

    @commands.command()
    async def close(self,ctx):
        self.no()

    @commands.command()
    async def open(self,ctx):
        self.yes()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "/start":
            self.yes()


    @commands.command()
    async def look(self,ctx,member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="観戦者")
        await member.add_roles(role)
        role = discord.utils.get(ctx.guild.roles, name="生存者")
        await member.add_roles(role)
        role = discord.utils.get(ctx.guild.roles, name="死亡者")
        await member.add_roles(role)

    @commands.command()
    async def kill(self,ctx,member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="生存者")
        await member.remove_roles(role)
        role = discord.utils.get(ctx.guild.roles, name="死亡者")
        await member.add_roles(role)

    @commands.command()
    async def live(self,ctx,member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="死亡者")
        await member.remove_roles(role)
        role = discord.utils.get(ctx.guild.roles, name="生存者")
        await member.add_roles(role)

    @commands.command()
    async def tfcheck(self,ctx):
        if self.on_game == True:
            print("I am True")
            return
        if self.on_game == False:
            print("I am False")
            return

    async def box(self,chan,title):
        txt = ""
        for i, id in enumerate(self.jobs.keys()):
            txt += f"\n{self.count[i]}. <@{id}>"

        test = discord.Embed(title=title,colour=0x1e90ff)
        test.add_field(name="プレイヤー一覧", value=txt, inline=True)
        msg = await chan.send(embed=test)

        for i, id in enumerate(self.jobs.keys()):
            await msg.add_reaction(self.ment[i])

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


    async def on(self,ctx,jobs):
        self.yes()
        self.jobs = jobs
        # print(self.jobs)
        await self.start(ctx)

    async def start(self,ctx):
        await ctx.send("ゲームが開始されました。")
        await self.play(ctx)
        await asyncio.gather(
            self.wolf(ctx),
            self.fortun(ctx)
        )

    async def wolf(self,ctx):
        chan = discord.utils.get(ctx.guild.text_channels, name="人狼")
        await self.box(chan,"殺害する人を選択してください。")

    async def fortun(self,ctx):
        chan = discord.utils.get(ctx.guild.text_channels, name="占い師")
        await self.box(chan,"占う人を選択してください。")


































def setup(bot):
    bot.add_cog(Game(bot))
