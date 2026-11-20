class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        prev = 0
        for num in nums:
            if num == prev:
                return num
            prev = num
        