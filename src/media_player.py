# Class that connects to Windows Media Player
# Follows the singleton design pattern
# Create a Class Media_Player
# Initialise object using constructor
# Create connection to media player api
# define functions for start, stop
# Handle async play

import asyncio

from winrt.windows.foundation import Uri
from winrt.windows.media.playback import MediaPlayer

mp = MediaPlayer()


def play_stream(url_to_play):
    # Initialise media player
    # parse url into a Uri
    # play url

    uri = Uri(url_to_play)
    mp.set_uri_source(uri)
    mp.play()


play_stream(
    "https://mediaserviceslive.akamaized.net/hls/live/2038316/classicfmnsw/index.m3u8"
)

input("\nPress ENTER to close the player and exit script...\n")
