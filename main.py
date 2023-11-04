#import all the libraries
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord import Interaction
import datetime
from dateutil import parser

# Create a TOKEN for discord bot loggin
load_dotenv()
TOKEN = os.getenv('TOKEN')

#code in between initializer and client.run
#initialize bot, use "." for command prefix
client = commands.Bot(command_prefix="!", intents = discord.Intents.all())

#Shows us when bot is connected and online, shows that it is working
@client.event
async def on_ready():
    print(f"{client.user.name} is connected.")

# Command functions go here
@client.command()
async def setreminder(ctx, remindertitle:str, date: str, time: str):
    print(remindertitle, date, time)
    #Combine date and time strings to create datetime string
    reminder_datetime_str = f"{date} {time}"
    
    # Convert string to datetime object
    try:
        reminder_datetime = datetime.datetime.strptime(reminder_datetime_str, "%m/%d %H:%M")
    except ValueError:
        # Handle the case where the conversion fails
        await ctx.send("Incorrect date or time format. Please use the correct format!")
        return
    
    # Format date and time for display
    formatted_date = reminder_datetime.strftime("%m/%d")
    formatted_time = reminder_datetime.strftime("%H:%M")
    

    #respond to the user
    await ctx.send(f"Your reminder is set for {formatted_date} and {formatted_time}, thank you!")
    
    #make wait for day and month difference

    #wait for the correct time (hours, minute)
    now=datetime.datetime.now()
    then = now.replace(hour=reminder_datetime.hour,minute=reminder_datetime.min)
    wait_time = (then-now).total_seconds()
    await asyncio.sleep(wait_time)

    await ctx.send(f"@everyone {remindertitle}")

@setreminder.error
async def setreminder_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("""Incorrect format. Use the command this way: '!setreminder month/day hours/minutes'. For example: '!setreminder 3 PM Meeting 5/24 8:30' """)

#please find a way to do a repeat frequency

#Token goes here
client.run(TOKEN)