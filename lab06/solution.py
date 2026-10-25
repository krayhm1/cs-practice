from pathlib import Path

def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts = {}
    for path in paths:
        ext = Path(path).suffix.lower().lstrip('.')
        counts[ext] = counts.get(ext, 0) + 1
    return counts

def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    return min(paths, key=lambda p: (-p.count('/'), p))

def human_size(n_bytes: int) -> str:
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = float(n_bytes)

    for i, unit in enumerate(units):
        if size < 1024 or i == len(units) - 1:
            if i == 0:
                return f"{int(size)} {unit}"
            return f"{size:.1f} {unit}"
        size /= 1024
