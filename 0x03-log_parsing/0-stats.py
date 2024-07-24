#!/usr/bin/python3
import sys
import signal

total_size = 0
status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0

def print_stats():
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 10:
            continue
        try:
            size = int(parts[-1])
            status_code = parts[-2]
            total_size += size
            if status_code in status_counts:
                status_counts[status_code] += 1
            line_count += 1
        except ValueError:
            continue

        if line_count == 10:
            print_stats()
            line_count = 0
except KeyboardInterrupt:
    print_stats()
    raise
