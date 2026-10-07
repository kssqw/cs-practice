def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Ошибка: должно быть 3 поля!")
    city = parts[0]
    temp_str = parts[1]
    date = parts[2]
    if city == "" or date == "":
        raise ValueError("Ошибка: пустое поле!")
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError("Ошибка: температура не число!")
    res = {
        "city": city,
        "temp": temp,
        "date": date
    }
    return res
def read_valid(lines: list[str]) -> list[dict]:
    valid_records = [] 
    
    for line in lines:
        if line == "":
            continue
            
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            pass
            
    return valid_records