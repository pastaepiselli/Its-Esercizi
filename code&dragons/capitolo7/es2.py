def count_lines(lines: list[str]) -> int:
    filename = 'textio_count.txt'
    with open(filename, 'w') as f:
        for l in lines:
            f.write(l + '\n')
            
    count  = 0
    with open(filename, 'r') as f:
         for l in f:
            count += 1
    
    return count
          
   