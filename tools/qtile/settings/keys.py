# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile keybindings
import os
from libqtile.config import Key
from libqtile.command import lazy


mod = "mod4"
terminal = "kitty -o background_opacity=0.65"
home = os.path.expanduser("~")
browser = "opera"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "k", lazy.layout.down()),
    ([mod], "i", lazy.layout.up()),
    ([mod], "j", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "j", lazy.layout.grow()),
    ([mod, "shift"], "l", lazy.layout.shrink()),
    #BSP control de ventana
    ([mod, "shift"], "k", lazy.layout.shuffle_down()),
    ([mod, "shift"], "i", lazy.layout.shuffle_up()),
    ([mod, "shift"], "j", lazy.layout.shuffle_left()),
    ([mod, "shift"], "l", lazy.layout.shuffle_right()),

    ([mod, "mod1"], "k", lazy.layout.flip_down()),
    ([mod, "mod1"], "i", lazy.layout.flip_up()),
    ([mod, "mod1"], "j", lazy.layout.flip_left()),
    ([mod, "mod1"], "l", lazy.layout.flip_right()),
    
    ([mod, "control"], "k", lazy.layout.grow_down()),
    ([mod, "control"], "i", lazy.layout.grow_up()),
    ([mod, "control"], "j", lazy.layout.grow_left()),
    ([mod, "control"], "l", lazy.layout.grow_right()),
    # Toggle floating
    ([mod], "space", lazy.window.toggle_floating()),

   # Toggle fullscreen
    ([mod], "f", lazy.window.toggle_fullscreen()),

    # Move windows up or down in current stack
    ([mod, "shift"], "k", lazy.layout.shuffle_down()),
    ([mod, "shift"], "i", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    ([mod, "shift"], "r", lazy.spawncmd()),

    # ------------ App Configs ------------

    # Menu
    ([mod], "d", lazy.spawn("rofi -show drun -show-icons")),

    #powermenu
    ([mod], "x", lazy.spawn(f"{home}/.config/rofi/bin/applet_powermenu")),

    # Window Nav
    ([mod, "shift"], "d", lazy.spawn("rofi -show ")),

    # Browser
    ([mod], "b", lazy.spawn(browser)),

    # File Explorer
    ([mod], "e", lazy.spawn(f"{terminal} -e ranger")),

    # Terminal
    ([mod], "Return", lazy.spawn(terminal)),

    # Redshift
    ([mod], "r", lazy.spawn("redshift -O 2400")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    ([mod], "s", lazy.spawn("scrot")),
    ([mod, "shift"], "s", lazy.spawn("scrot -s")),

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]
