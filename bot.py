from secret import *
import discord
import json
import datetime
from tinydb import TinyDB, Query
import pandas as pd

class SchedulerBot(discord.Client):

    def __init__(self, AUTH_TOKEN):
        #auth_token is the discord authentication token
        #db contains all of the tables
        #events is a table of existing events 

        super(SchedulerBot, self).__init__()
        self.auth_token = AUTH_TOKEN
        self.db = TinyDB('db.json')
        self.events = self.db.table('Events')
        self.reminders = self.db.table('Reminders')
    
    #Initializes and runs the bot
    def run(self):
        print('Initializing')
        super(SchedulerBot, self).run(self.auth_token)
    
    #Creates an event and inserts it into the events database
    def create_event(self, name, creator, event_time, description):
        # Each event contains: name, creator, time (%m/%d/%y %I:%M%p), description

        event = Query()

        if self.events.contains(event['name'] == name):
            return 'There already exists an event named {}.'.format(name)
        
        event_info = {'name':name, 'creator':creator, 'time':event_time, 'description':description}

        self.events.insert(event_info)
        return '{} event was created.'.format(name)
    
    #Returns a pandas dataframe of all events
    def list_events(self):
        event_list = self.events.all()
        eventdf = pd.DataFrame(event_list)
        if eventdf.empty:
            return 'There are no events.'
        return eventdf.to_string(index=False)

    """
    #Returns a list of events matching the name/creator
    def find_event(self, field, query):
        event = Query()
        return self.events.search(event[field] == query)
    """

    #Returns a pandas dataframe of events matching the query
    def list_events(self, field=None, query=None):
        if not field:
            event_list = self.events.all()
            if len(event_list) == 0:
                return 'There are no events created.'
        else:
            event = Query()
            return self.events.search(event[field] == query)
            if len(event_list) == 0:
                return 'There is no event with the given {}.'.format(field)
        eventdf = pd.DataFrame(event_list)
        return 'Events: \n' + eventdf.to_string(index=False)
    
    #Deletes all events
    def delete_all_events(self):
        event = Query()
        self.events.truncate()
        return 'All events deleted.'
    
    #Deletes an event with the given name/creator
    def delete_event(self, field, query):
        event = Query()
        removed_events = self.events.remove(event[field] == query)
        if len(removed_events) == 0:
            return 'There is no event with the given {}.'.format(field)
        if field=='name':
            return 'Removed the event named {}.'.format(query)
        else: #field=='creator'
            return 'Removed all events created by {}'.format(query)