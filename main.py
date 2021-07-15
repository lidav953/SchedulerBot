from secret import *
import bot

if __name__ == "__main__":
    bot = bot.SchedulerBot(AUTH_TOKEN)
    bot.run()