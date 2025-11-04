def dedup_stable(nums: list[int]) -> list[int]:
    if not nums:
        return []

    new_list: list[int] = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            new_list.append(nums[i])
        
    return new_list
    