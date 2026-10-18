import sys

from stats import average_by_city, parse_record, read_valid, warmest_city

lines = sys.stdin.read().splitlines()
records = read_valid(lines)

skip = 0
for line in lines:
    if not line.strip():
        continue
    try:
        parse_record(line)
    except ValueError:
        skip += 1

print(len(records))
print(skip)

if records:
    best = warmest_city(records)
    print(f"{average_by_city(records)[best]:.1f}")
else:
    print("0.0")