'''
@file spex_bot.py
@brief Astrodynamics/Admin discord bot. 

@author SPEX
'''


import discord
# TODO: whether library for observation conditions?
# TODO: astropy to do FITS editing/calculations on the fly?


class SPEXBot(discord.Client):
    """
    Discord bot client. Handles events and commands.
    """

    __slots__ = ['__flag']


    def __init__(self):
        """ init """
        self.__flag = "$!"  # TODO: adjust flag if desired


    # FOR EVENT DOCUMENTATION: https://discordpy.readthedocs.io/en/stable/api.html#event-reference
    # NOTE: a fair amount of method documentation is rephrased/copy-pasted from the above documentation


    # ---- Connection Methods -------------------------------------------------


    async def on_connect(self):
        """
        Called when the client has successfully connected to Discord.
        
        NOTE: NOT the same as being fully prepared (see {@code on_ready} for full preperation call)
        
        TODO: implement
        """
        return


    async def on_disconnect(self):
        """
        Called when the client has disconnected from Discord.
        Causes range from internet being disconnected to explicit admin call to close.

        TODO: implement
        """
        return


    async def on_ready(self):
        """
        Called after successful login.

        NOTE: NOT guaranteed to be first function called.
        """

        print("logged in as {0}!".format(self.user))


    async def on_resumed(self):
        """
        Called when the client has resumed a session.
        Whatever that means....

        TODO: figure out when this actually gets called....
        TODO: implement
        """
        return


    # ---- User Interaction Methods -------------------------------------------


    async def on_message(self, message):
        """
        Message event handler.

            Parameters:
                message: message recieved

        Pre: Intents.messages enabled
        TODO: enable Intents.messages
        """

        if message.author == self.user:
            return

        # TODO: process different commands if message starts with bot flag

        if message.ccontent.startswith(self.__flag):
            await message.channel.send("SPEXBot recieved message!")

        return


    # ---- Reaction Methods ---------------------------------------------------
        # Give users rolls?


    async def on_reaction_add(reaction, user):
        """
        Called when a message has a reaction added to it.

            Parameters:
                reaction: idk....
                user: user that reacted

        TODO: implement
        """
        return


    async def on_reaction_add(self, reaction, user):
        """
        Called when a message has a reaction removed from it.

            Parameters:
                reaction: idk....
                user: user that reacted

        TODO: implement
        """
        return


def main():
    """
    Runs an instance of SPEXBot. 
    Bot requires discord token to run.
    """
    
    bot = SPEXBot()
    # TODO: figure out how we want to handle token (CLA, hardcode, etc., preferably not hardcoded)
    bot.run("insert token here")


if __name__ == "__main__":
    main()
