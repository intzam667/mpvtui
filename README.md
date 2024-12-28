# IntZam's MPV TUI
![image](https://github.com/user-attachments/assets/49b332a0-8958-4953-a900-0051cb155ee9)

- Sick of using ranger and other various file manager TUI's to manage your videos? Well, me too.
- You are a computing nerd who hates GUI's for better? Well, me too.
- You want a useful TUI manager? Well, me too!

This is a simple terminal-based app I built using Python that lets you browse and play video files directly from your terminal. I used the **Textual** library to create an interactive UI, so you can easily scroll through your videos and play them with **mpv**, all from within the terminal.

## Why TF?

- **Scrollbar Included**: TUI with scrollbar is sensual.
- **Minimalist**
- **All femboys are welcome**: It comes with popular themes such as gruvbox, monokai, dracula, solarized, etc. 
- **Cross-Platform**: It works on Linux, macOS, and Windows, as long as you have **mpv** and **Textual** installed.
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
Run it with Python and enjoy that good FOSSnerd mechanism.


## Future Updates

    I plan to add features for managing files (like renaming or deleting them) VERY SOON, LIKE I'M WORKING ON IT RIGHT NOW.
    Maybe I’ll add playlist support in the future. DON'T COUNT ON IT.
