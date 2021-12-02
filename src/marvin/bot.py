'''A bot for the SPEX discord. 

Authors: Joshua Yoder, Stevie Alvarez
'''

import os
import discord

_TOKEN = os.getenv('DISCORD_TOKEN')
"""Bot account token, used to connect to bot's discord account."""

_FLAG = "!"
"""Indicates command when present in a message."""


client = discord.Client()
# NOTE: switch from Client to Bot? https://stackoverflow.com/questions/51234778/what-are-the-differences-between-bot-and-client

@client.event
async def on_ready():
    """Called when bot successfully loged in and 'ready'."""

    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    """Called when message sent to accessable text channel.

    Parameters
    -----------
        message: discord.Message instance 
            Message recieved from guild. 

    TODO: handle 'guild' and dm messages separatly, can cause internal issues.
    """

    if message.author == client.user:  # don't process messages from this bot
        return
    
    print(message.content)  # TODO: don't forget to remove this line.

    if message.content == 'marvin, are you alive?':
        await message.channel.send('Life? Don\'t talk to me about life.')

    if message.content.startswith(_FLAG):
        # handle message
        pass


# run bot
if __name__ == '__main__':
    client.run(_TOKEN)
