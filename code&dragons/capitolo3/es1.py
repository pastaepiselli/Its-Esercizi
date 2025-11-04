def unique_count(nums: list[int]) -> int:
    count = 0
    new_list = []
    for e in nums:
        if e not in new_list:
            new_list.append(e)
    return len(new_list)
      