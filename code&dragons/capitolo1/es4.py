def chunk(lst: list[int], size: int) -> list[list[int]]:
    new_list = []
    for i in range(0, len(lst), size):
        new_list.append(lst[i:i + size])
    
    return new_list
        