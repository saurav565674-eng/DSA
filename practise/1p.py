def twoSum(nums: List[int], target: int) -> List[int]:
    if isinstance(nums,dict):
        target = nums.get("target")
        nums = nums.get("nums",[])
    seen={}
    for i ,num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement],i]
        seen[num]=i
    return[]