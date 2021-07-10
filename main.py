from secret import *
import discord
import requests
import json
import bot

if __name__ == "__main__":
    bot = bot.SchedulerBot(AUTH_TOKEN)
    bot.run()