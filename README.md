# IntZam's MPV TUI

I was so sick and tired of using ranger/nnn to manage the videos on my PC, so I said:

![image](https://github.com/user-attachments/assets/aed32731-55b2-4857-9ec9-d83e5276956c)


This is a simple terminal-based app I built using Python that lets you browse and play video files directly from your terminal. I used the **Textual** library to create an interactive UI, so you can easily scroll through your videos and play them with **MPV**, all from within the terminal.

## Why TF?

- **Scrollbar Included**: TUI with scrollbar is sensual.
- **Minimalist**
- **All femboys are welcome**: It comes with popular themes such as gruvbox, monokai, dracula, solarized, etc. 
- **Cross-Platform**: It works on Linux, macOS, and Windows, as long as you have **MPV** and **Textual** installed.
- **Open Source!**: You can fork it and add your own features? Now that's that good FOSS feeling.

## You convinced me, magic man!

1. Install mpv, duh...
   ```bash
   sudo pacman -S mpv
   sudo dnf install mpv
   sudo zypper install mpv
   sudo apk add mpv
   ... (and all your other distros)

...sorry I don't know the package manager for your custom FurryBSD

2. Install the necessary Python packages:
   ```bash
   pip install textual
   pip install pathlib

Note: Pathlib should be in your system already, if you don't have it, you can install it.

## Usage
Run it with python and enjoy that good FOSSnerd mechanism.

   ```bash
   python mpvtui.py



