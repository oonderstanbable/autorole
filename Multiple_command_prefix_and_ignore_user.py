import json
import discord
from discord.ext import commands
import asyncio
import requests as rq

igs=[]


def get_ignore_list():
    """
    [
        This async function will request the data until it's succesful and will append the data into the variable igs
    ]
    Example JSON structure of the database
    {
        "ignore list": ["405907326051024906"]
    }
    """
    while True:
        r = rq.get('your json database url here to request') #Requests the data from the given URL Example :https://jsonblob.com/api/c3dfe0c3-066a-11e9-bcad-bdb84d27a1c3
        if r.status_code == 200: # request was successful
            igs.append(r.json()) #appends the data that is converted into json
            break #break the loop


get_ignore_list()#runes the function 
def get_prefix(bot, msg):
    """[This funciton allows you to change the command prefixes or add more prefixes that can be used to tirgger the bot commands
        This can be used to make per server prefixes and or per user prefixes]
    
    Arguments:
        bot {[Class]} -- [The bot]
        msg {[Class]} -- [The messages being sent]
    
    Returns:
        [type] -- [This will return the command prefixes that can be used]
    """

    prefixes = ['a.', 's.','!','?'] #the normal prefixes that users can use if they are not in the igs list


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
    """[This command to add the user to the ignore list]
    
    Arguments:
        con {[Class Obj]} -- [The context of the user that used the command]
        user {discord.Member} -- [The tagged user if user is tagged]
    """

    if user.id in igs[0]['ignore list']: # check to see if user is already in the ignore list
        await bot.say("User already in ignore list")

    if user.id not in igs[0]['ignore list']: #check to see if user not in ignore list
        igs[0]['ignore list'].append(user.id) #add the user to the ignore list if the user is not in ignore list
        await bot.say("user added to list")
        while True: #update the data using while True loop until it's successful
            p = rq.put('the JSOn database url',data=json.dumps(igs[0])) #the example i used is https://jsonblob.com/api/c3dfe0c3-066a-11e9-bcad-bdb84d27a1c3
            if p.status_code == 200:
                await bot.say("Data has been updated on the web server database")
                break
            else:
                await asyncio.sleep(1)





@bot.command(pass_context=True)
async def remove_from_list(con,user:discord.Member):
    """[This function remove sthe user form the ignore list
    this can be edited to make it so that only certain people can use it like admins]
    
    Arguments:
        con {[Obj]} -- [The context of the user that used the command]
        user {discord.Member} -- [The user that was tagged]
    """

    if user.id in igs[0]['ignore list']: #check if user is in database of ignore list
        where = igs[0]['ignore list'].index(user.id) #find the locatin of the useri din list
        del igs[0]['ignore list'][where] #delete the user from the data base of ignore list
        await bot.say("User removed from the ignore list")
        while True: #update the current database 
            p = rq.put('your JSON database url', data=json.dumps(igs[0]))  # https://jsonblob.com/api/c3dfe0c3-066a-11e9-bcad-bdb84d27a1c3
            if p.status_code == 200: # if successful
                await bot.say("Data has been updated on the web server database")
                break
            else:
                await asyncio.sleep(1) #slep since not successful


bot.run(bot_token)
