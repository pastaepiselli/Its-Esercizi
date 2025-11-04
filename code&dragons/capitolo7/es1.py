# esercizio prima del git pull

def write_and_read(lines: list[str]) -> list[str]:
    new_list = []
    for e in lines:
        new_list.append(e)
    return new_list

# post git pull

def write_and_read(lines: list[str]) -> list[str]:
    filename = 'textio_write_and_read.txt'
    with open(filename, 'w') as f:
        for l in lines:
            f.write(l + '\n')
    new_list = []
    with open(filename, 'r') as f:
         for l in f:
            new_list.append(l.rstrip())
    
    return new_list
            
            