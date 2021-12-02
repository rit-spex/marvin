import os

import discord

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    print(message.content)

    if message.content == 'marvin, are you alive?':
        await message.channel.send('Life? Don\'t talk to me about life.')

# run bot
if __name__ == '__main__':
    client.run(TOKEN)
