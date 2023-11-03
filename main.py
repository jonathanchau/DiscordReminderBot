#import all the libraries
import discord
from discord.ext import commands
from discord import Interaction
import datetime

#code in between initializer and client.run
#initialize bot, use "." for command prefix
client = commands.Bot(command_prefix="!", intents = discord.Intents.all())

#Shows us when bot is connected and online, shows that it is working
@client.event
async def on_ready():
    print(f"{client.user.name} is connected.")

# Command functions go here
@client.command()
async def setreminder(ctx, remindertitle:str, date: float, time: float):
    print(remindertitle, date, time)
    #Combine date and time strings to create datetime string
    reminder_datetime_str = f"{date} {time}"
    
    # Convert string to datetime object
    try:
        reminder_datetime = datetime.datetime.strptime(reminder_datetime_str, "%m.%d %H.%M")
    except ValueError:
        # Handle the case where the conversion fails
        await ctx.send("Incorrect date or time format. Please use the correct format!")
        return
    
    # Format date and time for display
    formatted_date = reminder_datetime.strftime("%m/%d")
    formatted_time = reminder_datetime.strftime("%H:%M")
    

    #respond to the user
    await ctx.send(f"Your reminder is set for {formatted_date} and {formatted_time}, thank you!")

@setreminder.error
async def setreminder_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("""Incorrect format. Use the command this way: '.setreminder month.date hours.minutes'.
                       For example: '!setreminder "3 PM Meeting" 5.24 8.30' """)

#please find a way to do a repeat frequency

#Token goes here
client.run("MTE2OTg0MjczMTY1NzQ3MDAzMg.Gi8yYK.Efd3y8--rreoKTrpLPG9M25EFAqPPGwH5ZqDhI")