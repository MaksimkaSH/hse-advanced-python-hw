#!/usr/bin/env python3
import sys


def nl(input_stream):
    for i, line in enumerate(input_stream, start=1):
        print(f"{i}\t{line}", end='')


def main():
    if len(sys.argv) == 1:
        nl(sys.stdin)
    elif len(sys.argv) == 2:
        file_path = sys.argv[1]
        try:
            with open(file_path, 'r') as file:
                nl(file)
        except FileNotFoundError:
            print(f"task1: {file_path}: No such file or directory")


if __name__ == "__main__":
    main()
