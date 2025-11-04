def copy_list(src: list[str]) -> list[str]:
    source_file = 'textio_source.txt'
    copy_file = 'textio_copy.txt'
    mylist = []
    with open(source_file, 'w') as f:
        for l in src:
            f.write(l + '\n')
    with open(copy_file, 'w') as f:
        with open(source_file, 'r') as f2:
            for l in f2:
                f.write(l.rstrip())
                mylist.append(l.rstrip())
    return mylist
        