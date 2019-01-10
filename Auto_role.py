import discord
from discord.ext import commands
import asyncio
from discord.utils import find,get


bot=commands.Bot(command_prefix='a.')
bot.remove_command('help')


cms=bot.command(pass_context=True)

@bot.event
async def on_ready():
    print(bot.user.name)



@bot.event
async def on_member_join(user):
    role=find(lambda m:m.name == 'Role Name here',user.server.roles)
    await bot.add_roles(user,role)



@cms
async def get_role(con,role:discord.Role):
    """
    Bots can't add roles that has admin permissions to other users"
    THIS MAKES IT SO THAT ANYONE CAN GET ANY ROLE EVEN IF THEIR CURRENT ROLE IS LOWER THAN THE NEW ROLE
    (THIS DOES NOT INCLUDE ADMIN ROLES AS BOT IS NOT ABLE TO ADD IT TO USERS)"""
    try:
        await bot.add_roles(con.message.author,role)
        await bot.say("Role added")
    except:
        await bot.say("Bot could not add that role")


bot.run('bot_token_here')
