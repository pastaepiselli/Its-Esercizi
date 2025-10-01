def contains_line(lines: list[str], needle: str) -> bool:
    filename = 'textio_contains.txt'
    with open(filename, 'w') as f:
        for l in lines:
            f.write(l + '\n')
   
    with open(filename, 'r') as f:
        for _ in f:
            if needle in _:
                return True
        return False