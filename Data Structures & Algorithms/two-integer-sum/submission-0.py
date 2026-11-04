class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first = {}
        for i, num in enumerate(nums):
            if num in first:
                return [first[num], i]
            first[target - num] = i
        