# Handle async play
# Need to have name of station in windows + a system tray

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


# Create Media_Player class
# Follows the singleton design pattern
# Initialise object using constructor
# define functions for start, stop, tracking functions for getting states for loading and active.
# Graceful exit functionality
class Media_Player:
