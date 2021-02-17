# start.py

import discord
from discord.ext import commands

import atexit
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
        self.live.mem = {}
        self.dead.mem = {}
        self.count = ["B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]
        self.ment = ["🇧","🇨","🇩","🇪","🇫","🇬","🇭","🇮","🇯","🇰","🇱","🇲","🇳","🇴","🇵","🇶","🇷","🇸","🇹",]
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
            # print(f"{self.times} [Connection] : Removed {member.name} `s '観戦者'")
        except:
            a = "a"
        finally:
            try:
                if after.channel.guild.id != 726233332655849514:
                    # print(0)
                    return
                cname = after.channel.name
                if cname != "移動用":
                    # print(1)
                    return
                role = discord.utils.get(after.channel.guild.roles, name="生存者")
                if role in member.roles:
                    channel = discord.utils.get(after.channel.guild.voice_channels, name="会議所")
                    await member.edit(voice_channel=channel)
                    # print(f"{self.times} [Connection] : {member.name} has connected into '会議所'")
                    return
                role = discord.utils.get(after.channel.guild.roles, name="死亡者")
                if role in member.roles:
                    channel = discord.utils.get(after.channel.guild.voice_channels, name="反省会")
                    # print(f"{self.times} [Connection] : {member.name} has connected into '反省会'")
                    await member.edit(voice_channel=channel)
                    return
                channel = discord.utils.get(after.channel.guild.voice_channels, name="観戦中")
                role = discord.utils.get(after.channel.guild.roles, name="観戦者")
                await member.edit(voice_channel=channel)
                # print(f"{self.times} [Connection] : {member.name} has connected into '観戦中'")
                await member.add_roles(role)
            except:
                # print(2)
                a = "a"
            finally:
                # print(3)
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

    # @commands.command()
    # async def look(self,ctx,member: discord.Member):
    #     role = discord.utils.get(ctx.guild.roles, name="観戦者")
    #     await member.add_roles(role)
    #     role = discord.utils.get(ctx.guild.roles, name="生存者")
    #     await member.add_roles(role)
    #     role = discord.utils.get(ctx.guild.roles, name="死亡者")
    #     await member.add_roles(role)
    #
    # @commands.command()
    # async def kill(self,ctx,member: discord.Member):
    #     role = discord.utils.get(ctx.guild.roles, name="生存者")
    #     await member.remove_roles(role)
    #     role = discord.utils.get(ctx.guild.roles, name="死亡者")
    #     await member.add_roles(role)
    #
    # @commands.command()
    # async def live(self,ctx,member: discord.Member):
    #     role = discord.utils.get(ctx.guild.roles, name="死亡者")
    #     await member.remove_roles(role)
    #     role = discord.utils.get(ctx.guild.roles, name="生存者")
    #     await member.add_roles(role)

    @commands.command()
    async def tfcheck(self,ctx):
        if self.on_game == True:
            print("I am True")
            return
        if self.on_game == False:
            print("I am False")
            return

    async def on(self,ctx,jobs):
        self.yes()
        self.jobs = jobs
        self.live.mem = self.jobs
        await self.start(ctx)

    async def start(self,ctx):
        await ctx.send("ゲームが開始されました。")
        await asyncio.gather(
        self.set_channel(ctx),
        self.set_role(ctx)
        )
        await self.play(ctx)
        await self.manage(ctx)

    async def set_channel(self,ctx):
        self.cit.channel = discord.utils.get(ctx.guild.text_channels, name="市民")
        self.wolf.channel = discord.utils.get(ctx.guild.text_channels, name="人狼")
        self.fortun.channel = discord.utils.get(ctx.guild.text_channels, name="占い師")

    async def set_role(self,ctx):
        self.live.role = discord.utils.get(ctx.guild.roles, name="生存者")
        self.dead.role = discord.utils.get(ctx.guild.roles, name="死亡者")

    async def play(self,ctx):
        for id in self.jobs.keys():
            job = self.jobs[id]
            mem = ctx.guild.get_member(id)
            role = await ctx.guild.create_role(name=mem.name)
            chan = discord.utils.get(ctx.guild.text_channels, name=job)
            await chan.set_permissions(role,read_messages=True)
            await mem.add_roles(role)

        cel = self
        await self.game.move(cel,ctx)
        channel = discord.utils.get(ctx.guild.text_channels, name="会議所")
        await channel.send("@everyone\n全員に役職を付与しました。\nそれぞれの専用チャンネルにてメンションが飛びます。\n確認してください。\n__（市民の方にはメンションは飛んでません）__")
        await self.call(cel,ctx)

    async def call(self,cel,ctx):
        for id in cel.jobs.keys():
            role = cel.jobs[id]
            if role == "市民":
                continue
            channel = discord.utils.get(ctx.guild.text_channels, name=role)
            await channel.send(f"<@{id}> あなたは、 __{role}__ です。")

    async def manage(self,ctx):
        print("Game will start")
        role_list = self.live.mem.values()

        await asyncio.gather(
        self.wolf(ctx,role_list),
        self.fortun(ctx,role_list),
        )

        self.move_wait = True
        while self.move_wait == True:
            if self.wolf.can_move == True:
                continue
            if self.fortun.can_move == True:
                continue
            self.move_wait = False

        await asyncio.gather(
        self.move_wolf(self.wolf.flag),
        self.move_fortun(self.fortun.flag)
        )

        channel = discord.utils.get(ctx.guild.text_channels, name="会議所")
        await channel.send("一夜目終了")
        print("finish")

    async def box(self,chan,title):
        txt = "A. 誰も選択しない"
        for i, id in enumerate(self.jobs.keys()):
            txt += f"\n{self.count[i]}. <@{id}>"

        test = discord.Embed(title=title,colour=0x1e90ff)
        test.add_field(name=title, value=txt, inline=True)
        msg = await chan.send(embed=test)

        await msg.add_reaction('🇦')
        for i, id in enumerate(self.jobs.keys()):
            await msg.add_reaction(self.ment[i])

    async def wolf(self,ctx,role):
        if "人狼" not in role:
            self.wolf.can_move = False
            self.wolf.flag = None
            return
        self.wolf.can_move = True
        await self.box(self.wolf.channel,"殺害する人を選択してください。")

    async def fortun(self,ctx,role):
        if "占い師" not in role:
            self.fortun.can_move = False
            self.fortun.flag = None
            return
        self.fortun.can_move = True
        await self.box(self.fortun.channel,"占う人を選択してください。")


    async def move_wolf(self,mem):
        if mem == None:
            return
        await mem.remove_roles(self.live.role)
        await mem.add_roles(self.dead.role)
        await self.wolf.channel.send(f"<@{mem.id}> の殺害が完了しました。")

    async def move_fortun(self,mem):
        if mem == None:
            return
        print("a")
        role = self.live.mem[mem.id]
        if role == "人狼":
            bw = "黒"
        else:
            bw = "白"
        await self.fortun.channel.send(f"<@{mem.id}> は __{bw}__ です")


    @commands.Cog.listener()
    async def on_reaction_add(self,reaction,user):
        u_id = user.id
        if u_id not in self.live.mem.keys():
            return
        if self.live.mem[u_id] == "人狼":
            self.wolf.can_move = False
            if str(reaction.emoji) == '🇦':
                await self.wolf.channel.send(f"誰も殺害しませんでした。")
                self.wolf.flag = None
                return
            else:
                await self.wolf.channel.send(f"<@{user.id}> を殺害します。")
                self.wolf.flag = user
                return
        if self.live.mem[u_id] == "占い師":
            self.fortun.can_move = False
            if str(reaction.emoji) == '🇦':
                await self.fortun.channel.send(f"誰も占いませんでした。")
                self.fortun.flag = None
                return
            else:
                await self.fortun.channel.send(f"<@{user.id}> を占います。")
                self.fortun.flag = user
                return




































def setup(bot):
    bot.add_cog(Game(bot))
