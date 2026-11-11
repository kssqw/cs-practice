def csv_to_records(text: str) -> list[dict]:
    lines = [line.strip() for line in text.strip().split("\n") if line.strip()]
    if not lines:
        return []
    headers = lines[0].split(",")

    records = []
    for line in lines[1:]:
        values = line.split(",")
        records.append(dict(zip(headers, values)))
    return records


def parse_settings(lines: list[str]) -> dict:
    res = {}
    cur_key = None

    for line in lines:
        line = line.split("#")[0].strip()
        if not line:
            continue

        if line.startswith("-"):
            val = line.lstrip("- ").strip()
            res[cur_key].append(val)
        elif ":" in line:
            k, v = line.split(":", 1)
            k, v = k.strip(), v.strip()

            if not v:
                res[k] = []
                cur_key = k
            else:
                if v.isdigit():
                    v = int(v)
                elif v.replace(".", "", 1).isdigit():
                    v = float(v)
                elif v in ["true", "yes"]:
                    v = True
                elif v in ["false", "no"]:
                    v = False
                res[k] = v
    return res


