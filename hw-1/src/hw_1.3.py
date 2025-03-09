#!/usr/bin/env python3
import sys


def print_stats(lines, words, bytes_count, name=""):
    if name:
        print(f"{lines:8} {words:8} {bytes_count:7} {name}")
    else:
        print(f"{lines:8} {words:8} {bytes_count:7}")


def wc():
    files = sys.argv[1:]
    if not files:
        content = sys.stdin.read()
        lines = content.splitlines()
        words = content.split()
        bytes_count = len(content.encode('utf-8'))
        print_stats(len(lines), len(words), bytes_count)
    else:
        total_lines = total_words = total_bytes = 0
        for file_name in files:
            try:
                with open(file_name, 'r', encoding='utf-8') as f:
                    content = f.read()
            except FileNotFoundError:
                print(f"hw_1.3.py: {file_name}: No such file or directory")
                continue
            lines = len(content.splitlines())
            words = len(content.split())
            bytes_count = len(content.encode('utf-8'))
            print_stats(lines, words, bytes_count, file_name)
            total_lines += lines
            total_words += words
            total_bytes += bytes_count

        if len(files) > 1:
            print_stats(total_lines, total_words, total_bytes, "total")


if __name__ == "__main__":
    wc()
