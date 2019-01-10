from discod.ext import commands
import discord
import asyncio

class Ok:
  def __init__(self,bot):
    self.bot = bot
    
    
  @commands.command(pass_context=True)
  async def ok(con):
    await self.bot.say("OK")

def setup(bot):
    bot.add_cog(Ok(bot))
