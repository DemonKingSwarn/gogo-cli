import platform
import threading

from .__player__ import play as pl
from .__downloader__ import download as dl
from .__cast__ import open_cast

import os

def menu(url, referrer, anime, episode):
    #pl(url, referrer, anime, episode)
    pl_thread = threading.Thread(target=pl, args=(url, referrer, anime, episode))
    pl_thread.start()

    while True:
        plt = platform.system()
        if plt == "Windows":
            os.system("cls")
        else:
            os.system('clear')
        print(f"Playing E{episode} of {anime}")
        print("\n1. next\n2. replay\n3. previous\n4. select\n5. change quality\n6. chromecast\n7. download\n8. Quit\n")
        e = int(input(": "))
        if e == 1:
            from ..__gogo_cli__ import play
            episode = episode + 1
            play(anime, episode)
        elif e == 2:
            pl(url, referrer, anime, episode)
        elif e == 3:
            from ..__gogo_cli__ import play
            episode = episode - 1
            play(anime, episode)
        elif e == 4:
            from ..__gogo_cli__ import get_info
            get_info(anime)
        elif e == 5:
            from ..__gogo_cli__ import play
            play(anime, episode)
        elif e == 6:
            open_cast(url)
        elif e == 7:
            dl(anime, url, referrer, episode)
        elif e == 8:
            exit(0)
        else:
            print("[!] Invalid option")
            exit(1)


