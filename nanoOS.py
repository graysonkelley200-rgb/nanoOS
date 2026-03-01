#!/usr/bin/env python3
"""
NanoOS - A simple DOS-like operating system in Python.

Applications:
  edit [file]  - Text editor
  calc         - Calculator
  cal          - Calendar
  help         - Show this help
  cls          - Clear the screen
  ver          - Show version
  exit         - Shut down NanoOS
"""

import os
import sys

from calculator import run_calculator
from calendar_app import run_calendar
from text_editor import run_text_editor

VERSION = "1.0.0"
PROMPT = "C:\\> "


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_banner():
    print("=" * 44)
    print("  NanoOS  v{}".format(VERSION))
    print("  A simple DOS-like system written in Python")
    print("=" * 44)
    print('  Type "help" for a list of commands.\n')


def print_help():
    print("\n  NanoOS Commands")
    print("  " + "-" * 30)
    print("  edit [file]  Open the text editor")
    print("  calc         Open the calculator")
    print("  cal          Open the calendar")
    print("  cls          Clear the screen")
    print("  ver          Display NanoOS version")
    print("  help         Show this help message")
    print("  exit         Shut down NanoOS\n")


def main():
    clear_screen()
    print_banner()

    while True:
        try:
            raw = input(PROMPT).strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  Shutting down NanoOS...")
            sys.exit(0)

        if not raw:
            continue

        parts = raw.split(None, 1)
        cmd = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else None

        if cmd == "exit":
            print("  Shutting down NanoOS...")
            sys.exit(0)

        elif cmd == "help":
            print_help()

        elif cmd == "cls":
            clear_screen()

        elif cmd == "ver":
            print(f"  NanoOS version {VERSION}")

        elif cmd == "edit":
            run_text_editor(arg)

        elif cmd == "calc":
            run_calculator()

        elif cmd == "cal":
            run_calendar()

        else:
            print(f"  '{cmd}' is not recognized as a command. Type 'help'.")


if __name__ == "__main__":
    main()
