import subprocess
import platform
import os

FFMPEG_EXECUTABLE = "ffmpeg"

def determine_path() -> str:
    
    plt = platform.system()

    if plt == "Windows":
        return f"C://Users//{os.getenv('username')}//Downloads"

    elif plt == "Linux":
        return f"/home/{os.getlogin()}/Downloads"

    elif plt == "Darwin":
        return f"/Users/{os.getlogin()}/Downloads"

    else:
        print("[!] Make an issue for your OS.")
        exit(1)

path: str = determine_path()

def download(anime, url, referer, episode):
    
    subprocess.call(f"{FFMPEG_EXECUTABLE} -referer \"{referer}\" -i \"{url}\" -c copy \"{path}/{anime}-episode-{episode}.mp4\"", shell=True)

    print(f"Downloaded at {path}/{anime}-episode-{episode}.mp4")
