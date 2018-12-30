import discord
import asyncio
import requests as rq
from discord.ext import commands


bot= commands.Bot(command_prefix='a.')
cms=bot.command(pass_context=True)
event=bot.event

database={'user_db':None}


async def get_data():
    """
    This is an async function that will retreive the data from your database if you're using one from the web.
    An Example Structure of the JSON database
    {
        "users":{
            "user 0 by id":{"value":"this will contain the user's value of points"},
            "user 1 by id":{"value":"this will contain the user's value of points"},
            "user 2 by id":{"value":"this will contain the user's value of points"}
        }
    }
    Make the `value` int to make it easier t oadd in the on_message function
    """
    while True: #this will request until the requeset is successful
        r=rq.Session().get('the url of the database in JSON') #request the data from the following URL
        if r.status_code == 200: # request is successful
            database['user_db']=r.json() #put JSON data inside the dict user_db inside the variable database
            break#break the loop if it's successful

        else:#if the request is not successful then sleep for 2 seconds then restart again
            await asyncio.sleep(2)#sleep for 2 seconds, must be async or the whole program will sleep


@event
async def on_ready():
    bot.loop.create_task(get_data()) #this will run the async function get_data
    print(bot.user.name)


@event
async def on_message(msg):
    """[This message function will control the automatic adding of points to users
    This function will also add new users to the database if they are not in database]
    
    Arguments:
        msg {[Context of the user]} -- [Contains context information from the user that sent the message]
    """
    if msg.author.id in database['user_db']['users']: #check if the user is inside the JSON user's database
        database['user_db']['users'][msg.author.id]['value']+=1 #add the amount to the user on message

    if msg.author.id not in database['user+db']['users']: #if the user id is not in the JSON database
        database['user_db']['users'][msg.author.id]={"value":1} #gives the user that was not in database a value of 1



@cms
async def check(con,user:discord.Member=None):
    """[
        This function(command) checks for points of a user that is in the JSON database
        If user is mentioned it will check the user mention's points
        If not mentioned it will check the command user's points
    ]
    
    Arguments:
        con {[Class Obj]} -- [The context of the user that used the command]
    
    Keyword Arguments:
        user {discord.Member} -- [The user that was tagged or mentioned] (default: {None})
    """
    ct=con.message
    if user == None or user.id == ct.author.id: #tagged user is not the command user
        if ct.author.id in database['user_db']['users']:#if the user is in database
            await bot.say('You have {} points'.format(database['user_db']['users'][ct.author.id]['value']))

        if ct.author.id not in database['user_db']['users']:#user not in database
            await bot.say("You have 1 points") #out points 1 point since it will auto add the value with the on_message function
    
    if user != None and user.id != ct.author.id: #makes sure that the tagged user is not the command user
        if user.id in database['user_db']['users']:#check if tagged user in database
            await bot.say("{} has {} points".format(user.name,database['user_db']['users'][user.id]['value']))
        if user.id not in database['user_db']['users']: #user is not in database
            await bot.say("{} has 1 point".format(user.name)) #auto 1 because on_message will auto add the value
    



bot.run('bot token')
