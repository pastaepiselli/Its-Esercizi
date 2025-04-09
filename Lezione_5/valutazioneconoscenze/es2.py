def find_disapparred_numbers(nums: list[int]):
    mylist: list[int] = list(range(1, len(nums) + 1))
    mancanti: list[int] = []
    for item in mylist:

        if item not in nums:
            mancanti.append(item)

    return mancanti

print(find_disapparred_numbers([1, 8, 9, 150]))