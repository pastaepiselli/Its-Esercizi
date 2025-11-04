def safe_parse_int_list(s: str) -> list[int]:
    s = s.rstrip().replace(',','')
    new_list = []
    for c in s:
        try:
            c = int(c)
            new_list.append(c)
        except Exception:
            pass
    return new_list
            