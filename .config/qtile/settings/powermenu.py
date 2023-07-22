#!/usr/bin/env python3
import subprocess
from libqtile.command import lazy

power_menu_options = ["Shutdown", "Restart", "Suspend", "Logout"]

chosen_option = subprocess.check_output(
    [
        "rofi", "-show", "power-menu",
        "-modi", "power-menu:/usr/local/bin/rofi-power-menu"
    ]
)