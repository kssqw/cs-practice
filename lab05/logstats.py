lvls = ["DEBUG", "INFO", "WARNING", "ERROR"]

def parse_event(line):
    line = line.strip()
    if line == "":
        raise ValueError()
    
    parts = line.split()
    if len(parts) < 3:
        raise ValueError()
        
    t = parts[0]
    lvl = parts[1]
    
    if lvl not in lvls:
        raise ValueError()
    msg = " ".join(parts[2:])
    
    d = {"time": t, "level": lvl, "message": msg}
    return d


def count_levels(lines):
    res = {"BROKEN": 0, "DEBUG": 0, "ERROR": 0, "INFO": 0, "WARNING": 0}
    
    for s in lines:
        if s.strip() == "":
            continue
        try:
            e = parse_event(s)
            l = e["level"]
            res[l] = res[l] + 1
        except ValueError:
            res["BROKEN"] = res["BROKEN"] + 1
            
    return res
