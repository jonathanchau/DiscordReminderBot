# Import all the libraries
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import datetime
import asyncio

# Create a TOKEN for discord bot logging
load_dotenv()
TOKEN = os.getenv('TOKEN')

# Code in between initializer and client.run
# Initialize bot, use "." for command prefix
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Shows us when bot is connected and online, shows that it is working
@client.event
async def on_ready():
    print(f"{client.user.name} is connected.")

# Command functions go here
@client.command()
async def setreminder(ctx, remindertitle: str, date: str, time: str):
    print(remindertitle, date, time)
    # Combine date and time strings to create datetime string
    reminder_datetime_str = f"{date} {time}"

    # Convert string to datetime object
    try:
        reminder_datetime = datetime.datetime.strptime(
            reminder_datetime_str, "%m/%d %I:%M %p"
        )
    except ValueError:
        # Handle the case where the conversion fails
        await ctx.send(
            "Incorrect date or time format. Please use the correct format!"
        )
        return

    # Format date and time for display
    formatted_date = reminder_datetime.strftime("%m/%d")
    formatted_time = reminder_datetime.strftime("%I:%M %p")  # Include AM/PM

    # Respond to the user
    await ctx.send(
        f"Your reminder is set for {formatted_date} and {formatted_time}, thank you!"
    )

    # Make wait for day and month difference
    
    # Wait for the correct time (hours, minute)
    now = datetime.datetime.now()
    then = now.replace(hour=reminder_datetime.hour, minute=reminder_datetime.minute)
    wait_time = (then - now).total_seconds()
    await asyncio.sleep(wait_time)

    # Mention everyone in the channel
    await ctx.send(f"@everyone {remindertitle}")

@setreminder.error
async def setreminder_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send(
            """Incorrect format. Use the command this way: '!setreminder month/day hours:minutes AM/PM'. For example: '!setreminder 3 PM Meeting 5/24 8:30 PM' """
        )

# Please find a way to do a repeat frequency

# Token goes here
client.run(TOKEN)
