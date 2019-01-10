import discord
import asyncio
from discord.ext import commands

extensions=['fun','ok']


@bot.event
async def on_ready():
    bot.loop.create_task(bg())
    """WHEN BOT IS READY, PRINT MESSAGE IN TERMINAL"""
    print("I am running on " + bot.user.name)





for extension in extensions:
      try:
          bot.load_extension(extension)
          print("{} loaded".format(extension))
      except Exception as error:
          print("Unable to load extension {} error {}".format(extension, error))

bot.run(bot_token)
