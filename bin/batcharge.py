#!/usr/bin/env python3
# coding=UTF-8
# saved to ~/bin/batcharge.py and from
# http://stevelosh.com/blog/2010/02/my-extravagant-zsh-prompt/#my-right-prompt-battery-capacity

import math
import re
import subprocess
import sys


def battery_value(lines, key):
    pattern = re.compile(r'^\s*"{}"\s*=\s*([0-9.]+)\s*$'.format(re.escape(key)))
    for line in lines:
        match = pattern.match(line)
        if match:
            return float(match.group(1))
    return None


result = subprocess.run(
    ["ioreg", "-rc", "AppleSmartBattery"],
    check=False,
    stdout=subprocess.PIPE,
    stderr=subprocess.DEVNULL,
    text=True,
)

lines = result.stdout.splitlines()
b_max = battery_value(lines, "MaxCapacity")
b_cur = battery_value(lines, "CurrentCapacity")

if not b_max or b_cur is None:
    sys.exit(0)

charge = max(0.0, min(1.0, b_cur / b_max))
filled_slots = int(math.ceil(10 * charge))

filled = filled_slots * "◼"
empty = (10 - filled_slots) * "◻"

color_green = "%{\033[32m%}"
color_yellow = "%{\033[33m%}"
color_red = "%{\033[31m%}"
color_reset = "%{\033[00m%}"
color_out = (
    color_green if filled_slots > 6
    else color_yellow if filled_slots > 3
    else color_red
)

sys.stdout.write(f"{color_out}{filled}{empty}{color_reset}")
