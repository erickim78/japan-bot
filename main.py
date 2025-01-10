# Dependencies
import config

# Generic
import os
import random

# Discord
import discord
from discord.ext import commands
from discord import app_commands

class MyBot(commands.Bot):
    #Init
    def __init__(self):
        myIntents = discord.Intents.all()
        super().__init__(
            command_prefix = "!",
            intents = myIntents,
            application_id = config.clientID
        )

    # Setup hook
    async def setup_hook(self):
        await load_cogs()
        await bot.tree.sync(guild = config.myGuild)


    # On ready
    async def on_ready(self):
        print(f'Logged in as {self.user}')


# Load Cogs
async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'Loaded {filename} Cog')



# executer
if __name__ == '__main__':
    bot = MyBot()
    bot.run(config.botToken)