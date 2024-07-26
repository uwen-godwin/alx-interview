#!/usr/bin/python3
import sys
import signal

# Initialize metrics
total_size = 0
status_codes = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}


def print_stats():
    """ Print the metrics """
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """ Handle CTRL+C """
    print_stats()
    sys.exit(0)


# Setup signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

# Read from stdin
line_count = 0
for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) < 7:
            continue
        ip = parts[0]
        status_code = parts[-2]
        file_size = int(parts[-1])

        total_size += file_size

        if status_code in status_codes:
            status_codes[status_code] += 1

        line_count += 1
        if line_count == 10:
            print_stats()
            line_count = 0
    except Exception:
        continue

# Print final stats when the script ends
print_stats()
