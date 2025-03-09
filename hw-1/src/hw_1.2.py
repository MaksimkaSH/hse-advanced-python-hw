#!/usr/bin/env python3
import sys


def print_lines(lines, lines_number=10):
    if len(lines) > 0 and lines[-1].endswith('\n'):
        lines[-1] = lines[-1][:-1]
    result = "".join(lines[-lines_number:])
    print(result)


def tail():
    files = sys.argv[1:]
    if not files:
        print_lines(sys.stdin.readlines(), 17)
    else:
        for i, file_name in enumerate(files):
            if len(files) > 1:
                print(f"==> {file_name} <==")
            try:
                lines = open(file_name).readlines()
                if lines:
                    print_lines(lines)
                if i != len(files) - 1:
                    print()
            except FileNotFoundError:
                print(f"hw_1.2.py: {file_name}: No such file or directory")


if __name__ == "__main__":
    tail()
