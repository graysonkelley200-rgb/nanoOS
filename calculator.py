"""NanoOS Calculator - simple interactive calculator."""

import operator
import re


def run_calculator():
    """Launch the interactive calculator."""
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod,
        '**': operator.pow,
    }

    print("\n+---------------------------+")
    print("|     NanoOS Calculator     |")
    print("+---------------------------+")
    print("| Operators: + - * / % **  |")
    print("| Type 'exit' to quit       |")
    print("+---------------------------+\n")

    while True:
        try:
            expr = input("calc> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if expr.lower() in ("exit", "quit", "q"):
            break

        if not expr:
            continue

        # Match: number [op] number  (supports ** as two-char operator)
        match = re.fullmatch(
            r"(-?\d+(?:\.\d+)?)\s*(\*\*|[+\-*/%])\s*(-?\d+(?:\.\d+)?)",
            expr,
        )
        if not match:
            print("  Invalid expression. Example: 5 + 3")
            continue

        left = float(match.group(1))
        op_sym = match.group(2)
        right = float(match.group(3))

        if op_sym in ('/', '%') and right == 0:
            print("  Error: Division by zero")
            continue

        result = ops[op_sym](left, right)
        # Show integer if result has no fractional part
        if result == int(result):
            result = int(result)
        print(f"  = {result}")
