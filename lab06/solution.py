def count_by_extension(paths: list[str]) -> dict[str, int]:
    
    
    extensions_count = {}
    for path in paths:
      
        filename = path.split('/')[-1] if '/' in path else path
        
        if '.' in filename:
        
            ext = filename.split('.')[-1].lower()
        else:
            ext = ""
            
        extensions_count[ext] = extensions_count.get(ext, 0) + 1
        
    return extensions_count
def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    sorted_paths = sorted(paths, key=lambda p: (-p.count('/'), p))
    return sorted_paths[0]
def human_size(n_bytes: int) -> str:
    units = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
  
    if n_bytes < 1024:
        return f"{n_bytes} Б"
    size = float(n_bytes)
    unit_index = 0
    
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1    
    return f"{size:.1f} {units[unit_index]}"
