import platform
import subprocess
import os

MPV_EXECUTABLE = "mpv"
IINA_EXECUTABLE = "iina"

def play(url, referer, anime, episode):
    try:

        player = f"{os.getenv('GOGO_CLI_PLAYER')}"
        output = subprocess.check_output(["uname", "-o"])
        output_str = output.decode("utf-8").strip()
        if output_str == "Android":
            subprocess.call(f"nohup am start --user 0 -a android.intent.action.VIEW -d \"{url}\" -n is.xyz.mpv/.MPVActivity", shell=True)

        elif player == "iSH":
            print("\x1b]8;;vlc-x-callback://x-callback-url/stream?url=%s&filename=%sepisode-%s\x07~~~~~~~~~~~~~~~~~~~~\n~ Tap to open VLC ~\n~~~~~~~~~~~~~~~~~~~~\x1b]8;;\x07" % (url, anime, episode))

        elif(platform.system() == "Linux" or platform.system() == "Windows"):
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
