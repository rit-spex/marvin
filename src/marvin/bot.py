''' A bot for the SPEX discord. 

Authors: Joshua Yoder, Stevie Alvarez
'''
import os

import discord

TOKEN = os.getenv('DISCORD_TOKEN')


client = discord.Client()

@client.event
async def on_ready():
    """ Called when bot successfully loged in and 'ready'. """

    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    """ Called when message sent to accessable text channel.

    Args:
        message: message recieved from guild. discord.Message instance. 
            NOTE: for more info on message objects: 
            https://discordpy.readthedocs.io/en/stable/api.html#discord.Message

    Pre:
        Intents.message must be enabled.

    TODO: handle 'guild' and dm messages separatly, can cause internal issues.
    """

    if message.author == client.user:  # don't process messages from this bot
        return
    
    print(message.content)

    if message.content == 'marvin, are you alive?':
        await message.channel.send('Life? Don\'t talk to me about life.')

# run bot
if __name__ == '__main__':
    client.run(TOKEN)
