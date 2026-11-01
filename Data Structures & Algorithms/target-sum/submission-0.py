class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        # top-down with memoization

        # two choices: add, subtract
        # Base cases: 1. spent all coins and overshot the target, return 0
        # 2. spent all coins and reached the target, return 1
        # if we add a num, target -= num
        # if we subtract a num, target += num

        memo = {}

        def dfs(i:int, target: int) -> int:
            key = (i, target)
            if key in memo:
                return memo[key]
            
            if i == len(nums):
                if target == 0:
                    return 1
                else:
                    return 0

            memo[key] = dfs(i + 1, target - nums[i]) + dfs(i + 1, target + nums[i])
            return memo[key]

        return dfs(0, target)