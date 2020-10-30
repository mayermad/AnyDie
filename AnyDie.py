import discord
from discord.ext import commands
from dotenv import load_dotenv
import os



initial_extensions = ['cogs.DiceCommands']


description = '''Dice rolling bot.'''
bot = commands.Bot(command_prefix='/', description=description)

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)


@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')
    print(f'Successfully logged in and booted...!')

load_dotenv()
token = os.getenv("TOKEN")
bot.run(token, bot=True, reconnect=True)
