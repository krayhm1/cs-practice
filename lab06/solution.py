from pathlib import Path

def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts = {}
    for path in paths:
        ext = Path(path).suffix.lower().lstrip('.')
        counts[ext] = counts.get(ext, 0) + 1
    return counts