'''Help Command'''

def plz_help() -> str:
  """Generates a string documenting current functionality and use.

  Returns:
    formatted response describing use of the bot
  """
  s = "Usage: $[COMMAND] [OPTIONS...]\n\n"

  
  s+="\tAPOTD -- *Gets the NASA Astronomy Photo of the Day*\n\n"
  s+="\tminecraft [OPTIONS] -- *Easily manage the minecraft server whitelist*\n\t\twhitelist [USERNAME] - Add minecraft account of the given username to the whitelist\n\n"
  s+="\tweather -- *Get the upcoming weather conditions to see if it'll be a good night to go observing*\n\n"
  s+="\tStatic Responses ( __**NOT A SINGLE COMMAND**__, COLLECTION OF COMMANDS )\n\t\tThis list of commands is too long to print out, idk just check the github or something till I get permission to slap ~80-100 lines in here."

  # come up with a method of getting the documentation of each .py file in the src dir and using that instead?

  return s