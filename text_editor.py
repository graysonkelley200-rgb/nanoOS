"""NanoOS Text Editor - simple line-based text editor."""

import os


def run_text_editor(filename=None):
    """Launch the interactive text editor."""
    lines = []

    if filename and os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
        print(f"\nOpened: {filename}  ({len(lines)} line(s))")
    else:
        if filename:
            print(f"\nNew file: {filename}")
        else:
            filename = None
            print("\nNew unsaved buffer")

    def show_help():
        print("\n+--------------------------------------+")
        print("|       NanoOS Text Editor             |")
        print("+--------------------------------------+")
        print("| Commands (type at the prompt):       |")
        print("|  :list          - show all lines     |")
        print("|  :save          - save file          |")
        print("|  :save <file>   - save as <file>     |")
        print("|  :del <n>       - delete line n      |")
        print("|  :ins <n> <txt> - insert before n    |")
        print("|  :edit <n> <txt>- replace line n     |")
        print("|  :new           - clear buffer       |")
        print("|  :help          - show this help     |")
        print("|  :exit          - exit editor        |")
        print("|  (anything else appends a new line)  |")
        print("+--------------------------------------+\n")

    show_help()
    _show_lines(lines)

    while True:
        try:
            inp = input("editor> ")
        except (EOFError, KeyboardInterrupt):
            print()
            break

        inp = inp.rstrip("\n")

        if inp.startswith(":"):
            parts = inp.split(None, 2)
            cmd = parts[0].lower()

            if cmd == ":exit":
                break

            elif cmd == ":help":
                show_help()

            elif cmd == ":list":
                _show_lines(lines)

            elif cmd == ":new":
                lines = []
                filename = None
                print("  Buffer cleared.")

            elif cmd == ":save":
                target = parts[1] if len(parts) > 1 else filename
                if not target:
                    print("  Error: no filename specified. Use :save <filename>")
                    continue
                filename = target
                _save_file(filename, lines)

            elif cmd == ":del":
                if len(parts) < 2 or not parts[1].isdigit():
                    print("  Usage: :del <line_number>")
                    continue
                n = int(parts[1])
                if 1 <= n <= len(lines):
                    removed = lines.pop(n - 1)
                    print(f"  Deleted line {n}: {removed}")
                else:
                    print(f"  Line {n} out of range (1-{len(lines)})")

            elif cmd == ":ins":
                if len(parts) < 3 or not parts[1].isdigit():
                    print("  Usage: :ins <line_number> <text>")
                    continue
                n = int(parts[1])
                text = parts[2]
                # Allow inserting at position 1..len+1
                if n < 1 or n > len(lines) + 1:
                    print(f"  Line {n} out of range (1-{len(lines) + 1})")
                    continue
                lines.insert(n - 1, text)
                print(f"  Inserted at line {n}.")

            elif cmd == ":edit":
                if len(parts) < 3 or not parts[1].isdigit():
                    print("  Usage: :edit <line_number> <text>")
                    continue
                n = int(parts[1])
                if 1 <= n <= len(lines):
                    lines[n - 1] = parts[2]
                    print(f"  Updated line {n}.")
                else:
                    print(f"  Line {n} out of range (1-{len(lines)})")

            else:
                print(f"  Unknown command: {cmd}  (type :help for commands)")

        else:
            lines.append(inp)
            print(f"  [Line {len(lines)}] added.")


def _show_lines(lines):
    if not lines:
        print("  (empty buffer)")
        return
    width = len(str(len(lines)))
    for i, line in enumerate(lines, 1):
        print(f"  {i:{width}}| {line}")


def _save_file(filename, lines):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
            if lines:
                f.write("\n")
        print(f"  Saved: {filename}  ({len(lines)} line(s))")
    except OSError as e:
        print(f"  Error saving file: {e}")
