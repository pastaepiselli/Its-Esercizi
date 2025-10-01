def count_even(nums: list[int]) -> int:
    # se usi set O(n)
    count = 0
    for n in nums:
        if n % 2 == 0:
            count += 1

    return count