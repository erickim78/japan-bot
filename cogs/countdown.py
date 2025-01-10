# Discord
import discord
from discord.ext import commands
from discord import app_commands

import config
import random

class Countdown(commands.Cog):
    def __init__(self, bot):
        print(f'initializing countdown.cog')

async def setup(bot):
    await bot.add_cog(Countdown(bot), guilds=[config.myGuild])