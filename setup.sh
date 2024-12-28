#!/bin/bash

spinner() {
  local pid=$!
  local delay=0.75
  local spin=('◜' '◞' '◠' '◝')
  local i=0
  while kill -0 $pid 2>/dev/null; do
    printf "\r${spin[$i]}"
    ((i = i + 1))
    ((i >= 4)) && i=0
    sleep $delay
  done
  printf "\r✓ Done!       \n"
}

USER_HOME="$HOME"

if [ "$EUID" -eq 0 ]; then
  echo "If you don't want to break your system, don't run this script as root. You have been warned!"
  exit 1
fi

if [ ! -d "$USER_HOME/.config/mpvtui667" ]; then
  mkdir -p "$USER_HOME/.config/mpvtui667" &
  spinner
  if [ $? -eq 0 ]; then
    echo "Created directory $USER_HOME/.config/mpvtui667"
  else
    exit 1
  fi
fi

cp mpvtui.py "$USER_HOME/.config/mpvtui667/" &
spinner
if [ $? -eq 0 ]; then
  echo "Copied mpvtui.py to $USER_HOME/.config/mpvtui667/"
else
  exit 1
fi

echo "#!/bin/bash" | sudo tee /usr/bin/mpvtui667 >/dev/null
echo USER_HOME="$HOME" | sudo tee -a /usr/bin/mpvtui667 >/dev/null
echo "python \$USER_HOME/.config/mpvtui667/mpvtui.py" | sudo tee -a /usr/bin/mpvtui667 >/dev/null
sudo chmod +x /usr/bin/mpvtui667 &
spinner
if [ $? -eq 0 ]; then
  echo "Created /usr/bin/mpvtui667 and made it executable"
else
  exit 1
fi

echo "Done, my vro"

exit 0
