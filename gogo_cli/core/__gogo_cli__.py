import httpx

import json
import subprocess
import sys
import random

from .utils.__player__ import play as pl
from .utils.__downloader__ import download as dl
from .utils.__menu__ import menu

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82"
}

client = httpx.Client(headers=headers, follow_redirects=True, timeout=None)

color = [  
    "\u001b[31m",
    "\u001b[32m",
    "\u001b[33m",
    "\u001b[34m",
    "\u001b[35m",
    "\u001b[36m",
    "\u001b[37m"
]

if len(sys.argv) == 1:
    try:
        query = input("Search: ")
        if query == "":
            print("ValueError: no query parameter provided")
            exit(1)
    except KeyboardInterrupt:
        exit(0)
else:
    query = " ".join(sys.argv[1:])

query = query.replace(' ', '%20')

url = f"https://api.consumet.org/anime/gogoanime/{query}"



def play(anime, episode, playNext):
    if playNext == 1:
        episode = episode + 1
    play_url = f"https://api.consumet.org/anime/gogoanime/watch/{anime}-episode-{episode}"
    data = client.get(play_url, params = { "server": "gogocdn" },).text
    parsed_data = json.loads(data)
    referrer = parsed_data["headers"]["Referer"]
    quality_options = [source["quality"] for source in parsed_data["sources"]]
   
    if len(quality_options) > 1:

        for idx, quality in enumerate(quality_options, start=1):
            color_idx = random.randint(0, len(color)-1) if idx >= len(color) else idx
            print(f"{color[color_idx]}{idx}. {quality}\u001b[0m")
        ch = int(input(': '))
    
    if 1 <= ch <= len(quality_options):
        chosen_quality = quality_options[ch - 1]
    
    for source in parsed_data["sources"]:
        if source["quality"] == chosen_quality:
            #print(source["url"] + ' ' + referrer)
            menu(source["url"], referrer, anime, episode)
            
def get_info(anime):
    info_url = f"https://api.consumet.org/anime/gogoanime/info/{anime}"
    data = client.get(info_url).text
    parsed_data = json.loads(data)
    total_episodes = parsed_data['totalEpisodes']
    if total_episodes > 1:
        ch = int(input(f"Total Episodes: {total_episodes}, Enter episode to play: "))
    else:
        ch = 1
    playNext = 0
    uwu = play(anime, ch, playNext)

def search():
    try:
        result = client.get(url).text
        parsed_data = json.loads(result)
        result_ids = [result['id'] for result in parsed_data['results']]
        for idx, result_id in enumerate(result_ids, start=1):
            color_idx = random.randint(0, len(color)-1) if idx >= len(color) else idx
            print(f"{color[color_idx]}{idx}. {result_id}\u001b[0m")
        ch = int(input("Enter your selection: "))
        ch = ch - 1
        anime = get_info(result_ids[ch])
    except Exception as e:
        print(e)

search()
