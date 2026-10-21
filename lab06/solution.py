def count_by_extension(paths: list[str]) -> dict[str, int]:
    result = {}
    for path in paths:
      
        if '/' in path:
            filename = path.split('/')[-1]
        else:
            filename = path
            
        if '.' in filename:
            ext = filename.split('.')[-1].lower()
        else:
            ext = ""
            
        if ext in result:
            result[ext] += 1
        else:
            result[ext] = 1
            
    return result


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
        
    best_path = paths[0]
    max_slashes = best_path.count('/')
    
    for path in paths[1:]:
        slashes = path.count('/')
        if slashes > max_slashes:
            max_slashes = slashes
            best_path = path
        elif slashes == max_slashes:
            if path < best_path:
                best_path = path
                
    return best_path

def human_size(n_bytes: int) -> str:
    if n_bytes < 1024:
        return str(n_bytes) + " Б"
        
    labels = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    
    value = float(n_bytes)
    idx = 0
    
    while value >= 1024 and idx < len(labels) - 1:
        value /= 1024
        idx += 1
        
    return f"{round(value, 1)} {labels[idx]}"
