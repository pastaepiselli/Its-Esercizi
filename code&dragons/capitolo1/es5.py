def flatten_once(nested: list[list[int]]) -> list[int]:
    new_list = []
    for e in nested:
        for i in e:
            new_list.append(i)
    return new_list
            