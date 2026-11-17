class Solution:
    def findMin(self, nums: list[int]) -> int:
        res = nums[0]

        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1
            res = min(res, nums[m])

        return res