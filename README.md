<h1 align="center">
GOGO-CLI
</h1>
<br>

<div align="center">
<br>
  <a href="http://makeapullrequest.com"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome"></a>
  <img src="https://img.shields.io/badge/os-linux-brightgreen" alt="OS linux">
  <img src="https://img.shields.io/badge/os-mac-brightgreen"alt="OS Mac">
  <img src="https://img.shields.io/badge/os-windows-brightgreen" alt="OS Windows">
  <img src="https://img.shields.io/badge/os-android-brightgreen" alt="OS Android">
  <img src="https://img.shields.io/badge/os-ios-brightgreen" alt="OS IOS">
  <br>
</div>
<br>

<h3 align="center">
 A high efficient, powerful and fast anime scraper. This tool scrapes the site <a href="https://gogoanimehd.com">gogoanime</a>.
 </h3>


<img src="https://github.com/DemonKingSwarn/gogo-cli/raw/master/.assets/output.gif">

# Overview

- [Installation](#installation)
    1. [PIP Installation](#1-pip-installs-packages-aka-pip-installation)
    2. [Source Code Download](#2-source-code-download)
    3. [Android Installation](#3-android-installation)
    4. [IOS Installation](#4-ios-installation)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Support](#support)
- [Project Disclaimer](#project-disclaimer)

# Installation
<i>for dependencies <a href="#dependencies">(see below)</a>.</i>

This project can be installed on to your device via different mechanisms, these mechanisms are listed below in the order of ease.

## 1. PIP Installs Packages aka PIP Installation

```sh
pip install gogo-cli
```

## 2. Installing from Source

First ensure <a href="https://python-poetry.org/docs/#installation">Poetry is installed</a>.

Then run the following command:

```sh
git clone https://github.com/demonkingswarn/gogo-cli.git \
&& cd gogo-cli \
&& poetry build \
&& pip install gogo-cli \
&& cd ..
```

<b>Additional information</b>: You <b>must</b> have Python installed <b>and</b> in PATH to use this project properly. Your Python executable may be `py` or `python` or `python3`. <b>Only Python 3.6 and higher versions are supported by the project.</b>

## 3. Android Installation
Install termux <a href="https://termux.com">(Guide)</a>

```sh
pkg up -y && pkg in python
pip install gogo-cli
```

For it to be able to stream you need to add referrer in mpv by opening mpv <a href="https://play.google.com/store/apps/details?id=is.xyz.mpv">(playstore version)</a>, going into Settings -> Advanced -> Edit mpv.conf and adding
```sh
referrer="https://gogoanimehd.to/"
```

## 4. IOS Installation

Install iSH and VLC from the app store.

Make sure apk is updated using `apk update; apk upgrade` then run this:

```sh
[ ! -d ~/.local/bin ] && mkdir ~/.local/bin && echo "export PATH=$HOME/.local/bin:$PATH\nexport GOGO_CLI_PLAYER=\"iSH\"" >> ".$(echo $SHELL | sed -nE "s|.*/(.*)\$|\1|p")rc"
apk add --update-cache python3 py3-pip
git clone https://github.com/Lockl00p/ffmpeglibs-iSH.git ~/ffmpeg
cd ~/ffmpeg
cat fmp.?? > ffmpeg.tar.gz
tar -xvf ffmpeg.tar.gz
cd FFmpeg
make install
cd
rm -rf ffmpeg
apk add ffmpeg
pip install gogo-cli
```
note that downloading is going to be very slow. This is an iSH issue, not gogo-cli issue.

# Dependencies
- [`mpv`](https://mpv.io) - Video Player
- [`iina`](https://iina.io) - Alternate video player for MacOS
- [`ffmpeg`](https://github.com/FFmpeg/FFmpeg) - Download manager

# Usage

```sh
Usage: gogo-cli [ARGS]...

Options:
    download    Download your favourite anime by query.
    play        Stream your favourite anime by query.
```

# Support
You can contact the developer directly via this <a href="mailto:swarn@demonkingswarn.ml">email</a>. However, the most recommended way is to head to the discord server.

<a href="https://discord.gg/JF85vTkDyC"><img src="https://invidget.switchblade.xyz/JF85vTkDyC"></a>

If you run into issues or want to request a new feature, you are encouraged to make a GitHub issue, won't bite you, trust me.

# Project Disclaimer
The disclaimer of the project  can be found <a href="https://github.com/demonkingswarn/gogo-cli/blob/master/disclaimer.org">here</a>.
