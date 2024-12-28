# IntZam's MPV TUI
![image](https://github.com/user-attachments/assets/49b332a0-8958-4953-a900-0051cb155ee9)

- Sick of using ranger and other various file manager TUI's to manage your videos? Well, me too.
- You are a computing nerd who hates GUI's for better? Well, me too.
- You want a useful TUI manager? Well, me too!

This is a simple terminal-based app I built using Python that lets you browse and play video files directly from your tehttps://github.com/intzam667/mpvtuirminal. I used the **Textual** library to create an interactive UI, so you can easily scroll through your videos and play them with **mpv**, all from within the terminal.

# **UPDATED!**
- **THE APP NOW HAS RENAMING FUNCTIONALITY BAKED IN.** 
- **(still working on search feature, though)**

## Why TF?

- **Scrollbar Included**: TUI with scrollbar is sensual.
- **Minimalist**
- **All femboys are welcome**: It comes with popular themes such as gruvbox, monokai, dracula, solarized, etc. 
- **Open Source!**: You can fork it and add your own features? Now that's that good FOSS feeling.

## SAD BUT TRUE
- It only works on Linux for now, if you want to maintain a fork with cross-platform features, please do so!

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
Run it in the commandline with "mpvtui667" and enjoy that good FOSSnerd mechanism.<br>
To rename a video, just press "R" on the keyboard and a dialog box will appear **BOTTOM** of the screen.<br>
You might need to scroll down using the scrollbar at the most right.<br>
(sorry Textual widget issues, not mine)<br>

## Future Updates
    Maybe I’ll add playlist support in the future. DON'T COUNT ON IT.




