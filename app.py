# ------------ Wlan Password Viewer ------------ #

# author: Sayed Mohammad Rezaie -- 17.Nov.2020
# github: @cdied

#description:

#   1. Wlan password viewer with python 3
#   2. Only in windows

# ------------------- imports ------------------ #

import subprocess

# ------------------ functions ----------------- #

data = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8").split("\n")
wifis = [line.split(":")[1][1:-1] for line in data if "All User Profile" in line]

for wifi in wifis:
    result = subprocess.check_output(["netsh", "wlan", "show", "profile", wifi, "key=clear"]).decode("utf-8").split("\n")
    result = [line.split(":")[1][1:-1] for line in result if "Key Content" in line]

    try:
        print(f"Name: {wifi}, Password: {result}")
    except IndexError: 
        print(f"Name: {wifi}, Password: Cannot be read!!")
