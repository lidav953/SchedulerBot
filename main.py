from secret import *
import bot
import datetime
import pytz
import discord

bot = bot.SchedulerBot(AUTH_TOKEN)

@bot.event
async def on_ready():
    print('Ready & logged in as {}'.format(bot.user))

@bot.event
async def on_message(msg):
    if msg.author==bot.user:
        return
    
    msgparts=msg.content.split(' ', 1)
    command = msgparts[0]
    info = msgparts[1]

    if command == '!createevent':
        #fields = name, time (mm/dd/YY hh:mmtt tz), description
        fields = info.split(', ')
        event_name = fields[0]
        #event_time = datetime.strptime(fields[1][:-2], '%m/%d/%y %I:%M')
        #event_description = 

    print(reply)

bot.run()