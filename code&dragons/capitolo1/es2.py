def max_or_none(nums: list[int]) -> int | None:
    if nums:
        return max(nums)
    return None