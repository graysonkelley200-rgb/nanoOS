"""NanoOS Calendar - interactive month/year calendar viewer."""

import calendar
from datetime import date


def run_calendar():
    """Launch the interactive calendar."""
    today = date.today()
    year = today.year
    month = today.month

    print("\n+-------------------------------+")
    print("|       NanoOS Calendar         |")
    print("+-------------------------------+")
    print("| Commands:                     |")
    print("|  n / next  - next month       |")
    print("|  p / prev  - previous month   |")
    print("|  t / today - jump to today    |")
    print("|  <YYYY MM> - go to month      |")
    print("|  exit      - quit calendar    |")
    print("+-------------------------------+\n")

    _print_month(year, month, today)

    while True:
        try:
            cmd = input("cal> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if cmd in ("exit", "quit", "q"):
            break
        elif cmd in ("n", "next"):
            month += 1
            if month > 12:
                month = 1
                year += 1
            _print_month(year, month, today)
        elif cmd in ("p", "prev", "previous"):
            month -= 1
            if month < 1:
                month = 12
                year -= 1
            _print_month(year, month, today)
        elif cmd in ("t", "today"):
            today = date.today()
            year, month = today.year, today.month
            _print_month(year, month, today)
        elif cmd == "":
            continue
        else:
            # Try to parse "YYYY MM"
            parts = cmd.split()
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                y, m = int(parts[0]), int(parts[1])
                if 1 <= m <= 12 and 1 <= y <= 9999:
                    year, month = y, m
                    _print_month(year, month, today)
                else:
                    print("  Invalid date. Year: 1-9999, Month: 1-12")
            else:
                print("  Unknown command. Type 'exit' to quit or 'n'/'p' to navigate.")


def _print_month(year, month, today):
    """Print a formatted calendar month, highlighting today."""
    cal = calendar.TextCalendar(calendar.SUNDAY)
    month_name = calendar.month_name[month]
    header = f"  {month_name} {year}"
    print(f"\n{header}")
    print("  Su Mo Tu We Th Fr Sa")

    today_mark = (today.year == year and today.month == month)

    for week in cal.monthdayscalendar(year, month):
        row = ""
        for day in week:
            if day == 0:
                row += "   "
            elif today_mark and day == today.day:
                row += f"[{day:2}]"
            else:
                row += f" {day:2}"
        # Tighten up bracketed today display
        print(" " + row)
    print()
