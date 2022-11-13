#!/bin/sh

# systray volume
kmix & 
# volumeicon &
# network manager
# nm-applet &
#fondo de pantalla
python3 $HOME/.config/qtile/wallpaper.py fondorandom &
#ajustes de volumen
python3 $HOME/.config/qtile/volumen.py &
#activar opacity
# compton -r 12 -o 0.00 -l 15 -t 15 -I 0.028 -O 0.03 -D 3 -c -f -C -F -G -b &
picom &
# ejecutar key mouse
setxkbmap -option keypad:pointerkeys &
# ejecutar telegram
telegram-desktop -startintray %u &

