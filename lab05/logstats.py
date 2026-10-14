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
        