"""Minecraft related functions."""

import os
from mcrcon import MCRcon

mcr = MCRcon("192.99.254.118", os.getenv("RCON_PASSWORD"), port=8144)
mcr.connect()

def whitelist(username: str) -> str:
    """Whitelist a minecraft user by username.

    Args:
        username: the minecraft username

    Returns:
        response from rcon command
    """
    response = mcr.command(f"/whitelist add {username}")
    return response