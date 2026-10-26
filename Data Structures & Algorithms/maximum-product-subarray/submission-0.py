class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # Subproblem: find the largest product for an array of length growing from 1 to <nums>
        # Product can be of any adjacent numbers
        # Greedily computing max at each step wouldn't work since we have negative numbers

        # We can still treat this as solvable by a single-pass greedy algorithm if we keep track of both local minimums and maximums
        # I guess we can just keep track if there is 0 present in the equation and if so, set our solution to 0 if it's negative
        # So if we have a zero, we multiply by 1 instead. This means that our solution is either in a subarray that starts after the 0 or 0 itself
        
        res = max(nums)
        prev_min, prev_max = nums[0], nums[0]

        has_zero = False

        for i in range(1, len(nums)):
            num = nums[i]
            if num == 0:
                has_zero = True
                prev_min = 1
                prev_max = 1
                continue
            else:
                local_max = max(num, prev_max * num, prev_min * num)
                local_min = min(num, prev_min * num, prev_max * num)
            prev_min, prev_max = local_min, local_max
            res = max(res, prev_max)
        
        return max(res, 0) if has_zero else res
    