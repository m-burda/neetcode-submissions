class Solution:
    def jump(self, nums: List[int]) -> int:
        # [2,3,1,3,1,1]
        # [3,2,2,1,2,1]
        # if we can reach the end from current step, res = 1
        # otherwise, result = 1 + min(nums[i + 1:j + 1])
        # time O(N^2), space O(1)

        if len(nums) == 1:
            return 0
        
        nums[-1] = 0
        nums[-2] = 1

        for i in range(len(nums) - 3, -1, -1):
            if i + nums[i] > len(nums) - 1:
                nums[i] = 1
            else:
                res = float("inf")
                for j in range(i + 1, i + nums[i] + 1):
                    res = min(res, nums[j])
                nums[i] = 1 + res
        
        return nums[0]