'''A bot for the SPEX discord. 

Authors: Joshua Yoder, Stevie Alvarez, John Haley
'''

from email import message
import os
import discord
from discord.ext import tasks
from discord.utils import get
from marvin.help import plz_help
import marvin.minecraft as minecraft
import marvin.apotd as apod
from marvin.static_responses import STATIC_RESPONSES


# Bot account token, used to connect to bot's discord account.
_TOKEN = os.getenv('DISCORD_TOKEN')

# Indicates command when present in a message.
_FLAG = "$"


client = discord.Client()
# NOTE: switch from Client to Bot? https://stackoverflow.com/questions/51234778/what-are-the-differences-between-bot-and-client

@client.event
async def on_ready():
    """Called when bot successfully logged in and 'ready'."""
    print(f'{client.user} has connected to Discord!')
    astroDailyPic.start()


@client.event
async def on_message(message):
    """Called when message sent to accessable text channel.

    Args:
        message: discord.Message instance 
            Message recieved from guild. 

    TODO: handle 'guild' and dm messages separately, can cause internal issues.
    """
    # skip if bot is the one that said it
    if message.author == client.user: 
        return

    if message.content.startswith(_FLAG):
        body = message.content.strip(_FLAG)

        # handle simple messages
        if body in STATIC_RESPONSES:
            await message.channel.send(STATIC_RESPONSES[body])
            return
        
        body_array = body.split()

        # handle help request
        if body_array[0] == "help":
            if len(body_array) == 3:
              if body_array[1] == "Static" and body_array[2] == "Responses":
                await message.channel.send("I can't help you with my Static Responses unfortunately. Try mentioning the Discord Dev roll and someone should be able to help.")

            param = None
            if len(body_array) > 1:
                param = body_array[1]
            await message.channel.send(plz_help(param))

        # handle minecraft stuff
        elif body_array[0] == "minecraft" and len(body_array) == 1:
            await message.channel.send("<cool stuff goes here>")
        elif body_array[0] == "minecraft" and body_array[1] == "whitelist" and len(body_array) > 2:
            response = minecraft.whitelist(body_array[2])
            await message.channel.send(response)
        
        # handle apod request
        elif (body_array[0] == "apod"):
            await message.channel.send(apod.getAPOD())

        # handle weather request
        elif (body_array[0] == "weather"):
            await message.channel.send("'weather' command is not functional... yet....")

        # handle option DNE
        else:
            await message.channel.send("unknown option: " + body + "\nTry: '$help' for information on how to have me do your bidding.")



@tasks.loop(hours=24)
async def astroDailyPic():
    """Astro daily pic."""
    print("APOD.")
    channel = client.get_channel(os.getenv("DISCORD_GENERAL"))
    await channel.send(apod.getAPOD())


# run bot
if __name__ == '__main__':
    client.run(_TOKEN)
