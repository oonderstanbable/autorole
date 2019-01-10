import discord
import asyncio
from discord.ext import commands

extensions=['fun','ok'] #the command files


@bot.event
async def on_ready():
    bot.loop.create_task(bg())
    """WHEN BOT IS READY, PRINT MESSAGE IN TERMINAL"""
    print("I am running on " + bot.user.name)





for extension in extensions: #this will load the commands from the file fun.py and ok.py or any file names inside the extension list at line 5
      try: #all the commands from the fun.py and ok.py will be added into the main.py file and will work as one bot
          bot.load_extension(extension) #load the extension
          print("{} loaded".format(extension))
      except Exception as error:
          print("Unable to load extension {} error {}".format(extension, error))

bot.run(bot_token)
