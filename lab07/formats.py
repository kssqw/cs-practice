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

def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    for r in rows:
        val = r.get(key)
        if val in extra:
            for k, v in extra[val].items():
                if k not in r:
                    r[k] = v
    return rows


def records_to_json(records: list[dict]) -> str:
    out = ["["]
    for i, r in enumerate(records):
        out.append("  {")
        keys = sorted(r.keys())

        for j, k in enumerate(keys):
            v = r[k]
            if isinstance(v, bool):
                v = "true" if v else "false"
            elif not isinstance(v, (int, float)):
                v = f'"{v}"'

            comma = "," if j < len(keys) - 1 else ""
            out.append(f'    "{k}": {v}{comma}')

        comma = "," if i < len(records) - 1 else ""
        out.append(f"  }}{comma}")
    out.append("]")
    return "\n".join(out)


