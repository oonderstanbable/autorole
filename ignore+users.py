import json
import discord
from discord.ext import commands
import asyncio
import requests as rq

igs=[]

async def get_ignore_list():
    while True:
        r = rq.get('your jsonblob url')
        if r.status_code == 200: # request was successful
            igs.append(r.json()) #appends the data that is converted into json
            break #break the loop
        else:
            await asyncio.sleep(1)

def get_prefix(bot, msg):
    prefixes = ['a.', 's.'] #the normal prefixes that users can use if they are not in the igs list

    me = ['nep.', 'k.', 'saki.', 'a.', 's.']

    if msg.author.id == '185181025104560128':
        return commands.when_mentioned_or(*me)(bot, msg)
    if msg.author.id in igs[0]['ignore list']:
        return 'ooGMNC90z1ihnl9IOrmZWENUbklyOP4eH2gjR96ddqawGepjqEdayZmuHed5gSe0qUHUgvw4hISrvkKhI8siKFqYTnWsB3C4LbKw1' #makes the command prefix into something they user won't know so that it wont' respond to them

    return commands.when_mentioned_or(*prefixes)(bot, msg)


bot = commands.Bot(command_prefix=get_prefix,description='A music bot fro discord Kurusaki')
chans = ['525911553698955264', '525193606374359040']
bot_token = 'token'


@bot.event
async def on_ready():
    bot.loop.create_task(get_ignore_list())
    print(bot.user.name)


@bot.command(pass_context=True)
async def on(con,user:discord.Member):
    if user.id not in igs[0]['ignore list']:
        igs.append(user.id)
    if user.id in igs[0]['ignore list']:
        await bot.say("User already in ignore list")

@bot.command(pass_context=True)
async def update_ignore_list_on_server():
    while True:
        p = rq.put('your jsonblob url',data=json.dumps(igs[0]))
        if p.status_code == 200:
            await bot.say("Data has been updated on the web server database")
            break
        else:
            await asyncio.sleep(1)

bot.run(bot_token)
