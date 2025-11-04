def head(lines: list[str], n: int) -> list[str]:
    filename = 'textio_head.txt'
    with open(filename, 'w') as f:
        for l in lines:
            f.write(l + '\n')
    new_list = []
    count = 0
    with open(filename, 'r') as f:
        for l in f:
            if count >= n:
                break
            new_list.append(l.rstrip())
            count += 1
    return new_list
        
           