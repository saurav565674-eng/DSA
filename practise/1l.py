def findMax(nums: list[int]) -> int:
    max_v = nums[0]
    for num in nums:
        if num >max_v:
            max_v = num
    return max_v