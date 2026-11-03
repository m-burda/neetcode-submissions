class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # O(1) space and time solution by computing the total difference
        res = 0
        nums.append(0)
        for i in range(len(nums)):
            res -= nums[i] - i
        return res