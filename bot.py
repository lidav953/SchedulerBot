from secret import *
import discord
import requests
import json
import tinydb

class SchedulerBot(discord.Client):
    def __init__(self, AUTH_TOKEN):
        super(SchedulerBot, self).__init__()
        self.auth_token = AUTH_TOKEN
    
    def run(self):
        print('running')
        super(SchedulerBot, self).run(self.auth_token)