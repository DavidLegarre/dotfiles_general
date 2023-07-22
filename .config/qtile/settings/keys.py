# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile keybindings

from libqtile.config import Key
from libqtile.command import lazy


mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Change window sizes 
    ([mod, "control"], "h", lazy.layout.grow_left()),
    ([mod, "control"], "l", lazy.layout.grow_right()),
    ([mod, "control"], "j", lazy.layout.grow_down()),
    ([mod, "control"], "k", lazy.layout.grow_up()),

    # Normalize sizes
    ([mod, "control"], "n", lazy.layout.grow_up()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "h", lazy.layout.shuffle_left()),
    ([mod, "shift"], "l", lazy.layout.shuffle_right()),
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "q", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # ------------ App Configs ------------

    # Menu
    ([mod], "f", lazy.spawn("rofi -show drun")),

    # Window Nav
    ([mod, "shift"], "m", lazy.spawn("rofi -show drun")),

    # Browser
    ([mod], "b", lazy.spawn("brave")),

    # File Explorer
    ([mod], "e", lazy.spawn("thunar")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),

    # Redshift
    ([mod], "r", lazy.spawn("redshift -O 2400")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Screenshot
    # ([mod], "s", lazy.spawn("scrot")),
    ([mod, "shift"], "s", lazy.spawn("flameshot gui")),

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pulsemixer --change-volume -10"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pulsemixer --change-volume +10 --max-volume 100"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pulsemixer --toggle-mute"
    )),

    # Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl --min-value=760 set 10%-")),
]]
