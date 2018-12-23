import json
import discord
from discord.ext import commands
import asyncio
import requests as rq

igs=[]

def get_ignore_list():
    while True:
        r = rq.get('https://jsonblob.com/api/c3dfe0c3-066a-11e9-bcad-bdb84d27a1c3')
        if r.status_code == 200: # request was successful
            igs.append(r.json()) #appends the data that is converted into json
            break #break the loop


get_ignore_list()
def get_prefix(bot, msg):
    prefixes = ['a.', 's.'] #the normal prefixes that users can use if they are not in the igs list


    # if msg.author.id not in igs[0]['ignore list'] and msg.server.name == 'Wuxia World':
    #     print('200')
    #     return 'asdf.'

    if msg.author.id in igs[0]['ignore list']:
        print('okooook')
        return 'ooGMNC90z1ihnl9IOrmZWENUbklyOP4eH2gjR96ddqawGepjqEdayZmuHed5gSe0qUHUgvw4hISrvkKhI8siKFqYTnWsB3C4LbKw1' #makes the command prefix into something they user won't know so that it wont' respond to them

    return commands.when_mentioned_or(*prefixes)(bot, msg)


bot = commands.Bot(command_prefix=get_prefix,description='A music bot fro discord Kurusaki')
chans = ['525911553698955264', '525193606374359040']
bot_token = 'bot token'


@bot.event
async def on_ready():
    print(bot.user.name)


@bot.command(pass_context=True)
async def on(con,user:discord.Member):
    if user.id in igs[0]['ignore list']:
        await bot.say("User already in ignore list")

    if user.id not in igs[0]['ignore list']:
        igs[0]['ignore list'].append(user.id)
        await bot.say("user added to list")
        while True:
            p = rq.put('https://jsonblob.com/api/c3dfe0c3-066a-11e9-bcad-bdb84d27a1c3',data=json.dumps(igs[0]))
            if p.status_code == 200:
                await bot.say("Data has been updated on the web server database")
                break
            else:
                await asyncio.sleep(1)





@bot.command(pass_context=True)
async def remove_from_list(con,user:discord.Member):
    if user.id in igs[0]['ignore list']:
        where = igs[0]['ignore list'].index(user.id)
        del igs[0]['ignore list'][where]
        await bot.say("User removed from the ignore list")
        while True:
            p = rq.put(
                'https://jsonblob.com/api/c3dfe0c3-066a-11e9-bcad-bdb84d27a1c3', data=json.dumps(igs[0]))
            if p.status_code == 200:
                await bot.say("Data has been updated on the web server database")
                break
            else:
                await asyncio.sleep(1)


bot.run(bot_token)
