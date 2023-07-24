import os

def open_cast(url):
    try:
        os.system(f"catt cast \"{url}\"")
    except Exception as e:
        os.system("catt scan")
        ip = input("Enter the ip of your chromecast: ")
        os.system(f"catt -d \"{ip}\" cast \"{url}\"")

