import platform
import subprocess

MPV_EXECUTABLE = "mpv"
IINA_EXECUTABLE = "iina"

def play(url, referer, anime, episode):
    try:

        output = subprocess.check_output(["uname", "-o"])
        output_str = output.decode("utf-8").strip()
        if output_str == "Android":
            args = [
                "nohup",
                "am",
                "start", 
                "--user",
                "0",
                "-a",
                "android.intent.action.VIEW",
                "-d".
                f'"{url}"',
                "-n",
                "is.xyz.mpv/.MPVActivity",
            ]
            mpv_android_process = subprocess.Popen(args, stdout=subprocess.DEVNULL)
            mpv_android_process.wait()

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
