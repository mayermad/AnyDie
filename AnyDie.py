import discord
from discord.ext import commands


initial_extensions = ['cogs.DiceCommands']


description = '''Dice rolling bot.'''
bot = commands.Bot(command_prefix='/', description=description)

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)


@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    # Changes our bots Playing Status. type=1(streaming) for a standard game you could remove type and url.
    await bot.change_presence(activity=discord.Game(name="WHFRP"))
    print(f'Successfully logged in and booted...!')


bot.run("NzcxNDQ1NTg0MjM0MTUyMDA2.X5sOsA.HARW5mMuD7o_NRLugiVQHGBjeB4", bot=True, reconnect=True)
