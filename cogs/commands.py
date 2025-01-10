# Discord
import discord
from discord.ext import commands
from discord import app_commands

import config
import random

class Commands(commands.Cog):
    def __init__(self, bot):
        print("initializing commands.cog")
        self.bot = bot

    @app_commands.command(name='countdown', description='See how many days remaining until Japan')
    async def countdown(self, interaction: discord.Interaction) -> None:
        rand = random.randint(0,17)
        imgURL = "https://i.imgur.com/ZC44rDY.jpeg"
        embed=discord.Embed(color=0xf1d3ed)
        embed.set_image( url = imgURL )
        embed.add_field(name="You have asked Shams-kun:", value="Test", inline=False)
        embed.add_field(name="TEST", value='\u200b', inline=False)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Commands(bot), guilds=[config.myGuild])