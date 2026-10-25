def parse_event(line: str) -> dict:
    parts = line.strip().split(maxsplit=2)
    if len(parts) != 3:
        raise ValueError("Недостаточно частей в строке")
    
    time, level, message = parts
    if level not in {"DEBUG", "INFO", "WARNING", "ERROR"}:
        raise ValueError("Неизвестный уровень")
        
    return {"time": time, "level": level, "message": message}

def count_levels(lines) -> dict:
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            level = event["level"]
        except ValueError:
            level = "BROKEN"
        counts[level] = counts.get(level, 0) + 1
    return counts

def top_errors(lines, n: int) -> list[list]:
    error_counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                msg = event["message"]
                error_counts[msg] = error_counts.get(msg, 0) + 1
        except ValueError:
            pass
    
    sorted_errors = sorted(error_counts.items(), key=lambda x: (-x[1], x[0]))
    return [[msg, count] for msg, count in sorted_errors[:n]]
