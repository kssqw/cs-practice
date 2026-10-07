def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Ошибка: должно быть 3 поля!")
    city = parts[0].strip()
    temp_str = parts[1].strip()
    date = parts[2].strip()
    temp_str  = temp_str.replace(',', '.')
    if city == "" or date == "":
        raise ValueError("Ошибка: пустое поле!")
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError("Ошибка: температура не число!")
    res = {
        "city": city,
        "temperature": temp,
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
def average_by_city(records: list[dict]) -> dict:
    sums = {} 
    counts = {} 
    for r in records:
        city = r["city"]
        t = r["temperature"]
        if city not in sums:
            sums[city] = t
            counts[city] = 1
        else:
            sums[city] = sums[city] + t
            counts[city] = counts[city] + 1
    averages = {}
    for city in sums:
        averages[city] = round(sums[city] / counts[city], 1)
    return averages
def warmest_city(records: list[dict]) -> str:
    if len(records) == 0:
        return ""
        
    averages = average_by_city(records)
    best_city = ""
    max_temp = -999.0 
    
    for city in averages:
        current_temp = averages[city]
        if current_temp > max_temp:
            max_temp = current_temp
            best_city = city
        elif current_temp == max_temp:
            if city < best_city:
                best_city = city
                
    return best_city
