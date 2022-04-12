'''Help Command'''

def plz_help(arg: str) -> str:
  """Generates a string documenting current functionality and use.

  Returns:
    formatted response describing use of the bot
  """
  s = "Usage: "
  if (arg == None) or (arg == "help"):
    s+="$[COMMAND] [OPTIONS...]\n"
    s+="Use: '$help [COMMAND]' for more information on each command (there probably won't be much more info other than what you'll find here)"
    s+="\tapod -- *Gets the NASA Astronomy Photo of the Day*\n\n"
    s+="\tminecraft [OPTIONS...] -- *Easily manage the minecraft server whitelist*\n\t\twhitelist [USERNAME] - Add minecraft account of the given username to the whitelist\n\n"
    s+="\tweather -- *Get the upcoming weather conditions to see if it'll be a good night to go observing.* ***Currently under development***\n\n"
    s+="\tStatic Responses ( __**NOT A SINGLE COMMAND**__, COLLECTION OF COMMANDS )\n\t\tThis list of commands is too long to print out, idk just check the github or something till I get permission to slap ~80-100 lines in here."
  else:
    # should switch to a 'match' conditional, but need python 10 installed (idk what we're using on the server atm....)
    if (arg == "apod"):
      s+="**$apod**\n\t*Gets the NASA Astronomy Photo of the Day*"

    elif (arg == "minecraft"):
      s+="**$minecraft [OPTIONS...]**\n\n\t***minecraft whitelist [USERNAME]*** - *Add the minecraft account of the given username to the SPEX minecraft server whitelist.*"

    elif (arg == "weather"):
      s = "'weather' command is currently under development, and is nonfunctional at the moment."
      
    else:
      s = "unknown option: " + arg + "\nTry: '$help' for information on how to have me do your bidding."


  # come up with a method of getting the documentation of each .py file in the src dir and using that instead?

  return s