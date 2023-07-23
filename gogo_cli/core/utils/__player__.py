import platform
import subprocess

MPV_EXECUTABLE = "mpv"
IINA_EXECUTABLE = "iina"

def play(url, referer, anime, episode):
    try:
        if(platform.system() == "Linux" or platform.system() == "Windows"):
            args = [
                MPV_EXECUTABLE,
                url,
                f"--referrer={referer}",
                f"--force-media-title=Playing {anime} Episode {episode}",
            ]

            mpv_process = subprocess.Popen(args, stdout=subprocess.DEVNULL)
            mpv_process.wait()

        elif(platform.system() == "Darwin"):
            args = [
                IINA_EXECUTABLE,
                "--no-stdin",
                "--keep-running",
                f"--mpv-referrer={referer}",
                url,
                f"--mpv-force-media-title=Playing {anime} Episode {episode}",
            ]

            iina_process = subprocess.Popen(args, stdout=subprocess.DEVNULL)
            iina_process.wait()

    except Exception as e:
        print("[!] no supported video player were found")
        exit(1)
