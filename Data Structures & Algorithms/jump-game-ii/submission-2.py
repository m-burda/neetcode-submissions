class Solution:
    def jump(self, nums: List[int]) -> int:
        # two pointers
        # start at index 0. l = 0, r = nums[0]
        # step += 1. Calculate the farthest reachable index from the current range.
        # l = r + 1. r = farthest reachable index
        # Repeat. If farthest reachable index >= len(nums) - 1, return steps
        # O(N) time, O(1) space

        l, r = 0, 0
        steps = 0
        farthest = 0

        while farthest < len(nums) - 1:
            steps += 1

            for i in range(l, min(r + 1, len(nums))):
                farthest = max(farthest, i + nums[i])
            
            l = r
            r = farthest
        
        return steps