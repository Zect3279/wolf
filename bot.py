from discord.ext import commands
from os import environ
import discord
import json


class Zect(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or(environ.get('PREFIX', '/')),
            help_command=None,
            intents=discord.Intents.all(),
        )

    async def on_ready(self):
        status = discord.Game("Wolf")
        # status = discord.Game("メンテナンス中")
        await self.change_presence(activity=status)
