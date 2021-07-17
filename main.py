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
            reply = bot.list_events()

        elif command == '!deleteallevents':
            reply = bot.delete_all_events()
    
    else:
        #createevent, findevent

        msgparts=msg.content.split(' ', 1)
        command = msgparts[0]
        fields = msgparts[1].split(', ')

        if command == '!createevent':
            #fields = name, time in bot's local time (%m/%d/%y %I:%M%p), description
            event_name = fields[0]
            event_time = fields[1]
            event_description = fields[2]
            reply = bot.create_event(event_name, msg.author.name, event_time, event_description)
        
        elif command == '!findevent':
            #fields = 'name'/'creator', name/creator
            reply = bot.list_events(fields[0], fields[1])
        
        elif command == '!deleteevent':
            #fields = 'name'/'creator', name/creator
            reply = bot.delete_event(fields[0], fields[1])

    await msg.channel.send(reply)
    print(reply)

bot.run()