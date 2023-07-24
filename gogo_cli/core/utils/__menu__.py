import platform

from .__player__ import play as pl
from .__downloader__ import download as dl
from .__cast__ import open_cast

import os

def menu(url, referrer, anime, episode):
    while True:
        plt = platform.system()
        if plt == "Windows":
            os.system("cls")
        else:
            os.system('clear')
        print("\n1. Play\n2. Download\n3. Replay episode\n4. Play next episode\n5. Cast to a chromecast device\n6. Quit\n")
        e = int(input(": "))
        if e == 1:
            pl(url, referrer, anime, episode)
        elif e == 2:
            dl(anime, url, referrer, episode)
        elif e == 3:
            pl(url, referrer, anime, episode)
        elif e == 4:
            from ..__gogo_cli__ import play
            playNext = 1
            play(anime, episode, playNext)
        elif e == 5:
            open_cast(url)
        elif e == 6:
            exit(0)
        else:
            print("[!] Invalid option")
            exit(1)


