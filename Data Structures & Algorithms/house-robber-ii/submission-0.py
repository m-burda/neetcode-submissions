class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums = [2] -> 2
        # nums = [2, 9] -> 9
        # nums = [2, 9, 8] -> 1. Rob house 2: cannot rob house 0 or 1 -> 8
        # 2. Do not rob house 2: [2, 9] -> 9
        # nums = [2, 9, 8, 3]
        # How do we guarantee that the previous solution does not include house 0 (i.e. adjacent house)?
        # if we create an array[1:n] i.e. [9, 8, 3] and solve for it, the solutions guarantee to not include an adjacent house
        # [2, 9, 8] second array [:n-1] includes the first element and is used in case we decide to not rob the current house
        # [2,9,8,3,6]
        #        ^
        # [9,8,3,6] solution for non-adjacent houses + current amount
        #. ^
        # [2,9,8,3] solution for adjacent houses
        #  ^
        # nums[2] is always max(nums)

        if len(nums) <= 3:
            return max(nums)

        nonadj = nums[1:]
        nonadj[1] = max(nonadj[0], nonadj[1])
        adj = nums[:len(nums) - 1]
        adj[1] = max(adj[0], adj[1])

        for i in range(2, len(nums) - 1):
            nonadj[i] = max(nonadj[i] + nonadj[i - 2], nonadj[i - 1])
            adj[i] = max(adj[i] + adj[i - 2], adj[i - 1])

        return max(nonadj[-1], adj[-1])