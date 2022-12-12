import os
from keep_alive import keep_alive
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = discord.Client(intents=discord.Intents.default())

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 716163845508563014  # Change to your discord id!!!


@bot.event
async def on_ready():  # When the bot is ready
    print("Up and Running")
    print(bot.user)  # Prints the bot's username and identifier


extensions = [
    'cogs.mainCog'  # Same name as it would be if you were importing it
]

#if __name__ == '__main__':  # Ensures this is the file being ran
#    for extension in extensions:
#        bot.load_extension(extension)  # Loades every extension.

bot.load_extension("cogs." + "mainCog")

keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)  # Starts the bot
