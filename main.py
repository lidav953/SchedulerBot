from secret import *
import bot
import datetime
import discord
import pandas

bot = bot.SchedulerBot(AUTH_TOKEN)

@bot.event
async def on_ready():
    print('Ready & logged in as {}'.format(bot.user))

@bot.event
async def on_message(msg):
    if msg.author==bot.user:
        return
    
    if msg.content[0] != '!':
        return
    
    reply='Not a valid command.'

    if (' ' not in msg.content):
        #listevents, deleteallevents
        command = msg.content

        if command == '!listevents':
            reply = 'Current events:\n' + bot.list_events()

        elif command == '!deleteallevents':
            reply = bot.delete_all_events()
    
    else:
        #createevent
        msgparts=msg.content.split(' ', 1)
        command = msgparts[0]
        info = msgparts[1]

        if command == '!createevent':
            #fields = name, time in bot's local time (%m/%d/%y %I:%M%p), description
            fields = info.split(', ')
            event_name = fields[0]
            event_time = fields[1]
            event_description = fields[2]
            reply = bot.create_event(event_name, msg.author.name, event_time, event_description)

    await msg.channel.send(reply)
    print(reply)

bot.run()