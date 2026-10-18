def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError('полей не ровно три')

    city, temp1, date = parts
    city = city.strip()
    date = date.strip()
    temp1 = temp1.strip().replace(",", ".")

    if not city:
        raise ValueError("пустое название города")
    if not date:
        raise ValueError('пустая дата')

    try:
        temp = float(temp1)
    except ValueError:
        raise ValueError('температура - не число') from None

    return {"city": city, "temp": temp, "date": date}


def read_valid(lines: list[str]) -> list[dict]:
    records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            continue
    return records


def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}
    for rec in records:
        city = rec["city"]
        total[city] = total.get(city, 0.0) + rec["temp"]
        count[city] = count.get(city, 0) + 1
    return {city: round(total[city] / count[city], 1) for city in total}


def warmest_city(records: list[dict]) -> str:
    avg = average_by_city(records)
    if not avg:
        raise ValueError('нет записей')
    return max(sorted(avg), key=avg.get)