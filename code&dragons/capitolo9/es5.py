def parse_int_list_strict(s: str) -> list[int]:
    my_list = []
    if not s:
        return my_list
    s = s.split(',')
    for c in s:
        if not c:
            raise ValueError
        my_list.append(int(c))
    return my_list
        
            
            
        