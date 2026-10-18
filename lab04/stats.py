def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError('полей не ровно три')

    city, temp1, date = parts
    city = city.strip()
    date = date.strip()
    temp1 = temp1.strip()

    if not city:
        raise ValueError("пустое название города")
    if not date:
        raise ValueError('пустая дата')

    try:
        temp = float(temp1)
    except ValueError:
        raise ValueError('температура - не число') from None

    return {"city": city, "temp": temp, "date": date}
