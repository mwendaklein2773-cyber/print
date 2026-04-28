#!/usr/bin/env python3
"""Traffic light simulator.

Run this script to display an animated terminal traffic light cycle.
"""

import os
import sys
import time

RED = "\033[1;31m●\033[0m"
YELLOW = "\033[1;33m●\033[0m"
GREEN = "\033[1;32m●\033[0m"
OFF = "\033[2m○\033[0m"

CYCLE = [
    ("RED", RED, OFF, OFF, 3.0),
    ("RED + YELLOW", RED, YELLOW, OFF, 1.5),
    ("GREEN", OFF, OFF, GREEN, 3.0),
    ("YELLOW", OFF, YELLOW, OFF, 1.5),
]


def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def render_light(label, red, yellow, green):
    print("+-------------+")
    print("|   TRAFFIC   |")
    print("|    LIGHT    |")
    print("+-------------+")
    print("|             |")
    print(f"|     {red}     |")
    print("|             |")
    print(f"|     {yellow}    |")
    print("|             |")
    print(f"|     {green}     |")
    print("|             |")
    print("+-------------+")
    print(f"State: {label}")
    print("Press Ctrl+C to stop.")


def main():
    try:
        while True:
            for label, red, yellow, green, duration in CYCLE:
                clear_console()
                render_light(label, red, yellow, green)
                time.sleep(duration)
    except KeyboardInterrupt:
        clear_console()
        print("Traffic light simulation stopped.")
        sys.exit(0)


if __name__ == "__main__":
    main()
