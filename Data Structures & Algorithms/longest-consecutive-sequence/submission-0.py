class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        longest = 0

        for num in nums:
            # if the number is not part of a sequence we have already checked
            if num - 1 not in nums:
                end = num + 1
                # O(N) time since we check each consecutive sequence once
                while end in nums:
                    end += 1
                longest = max(longest, end - num)
        
        return longest
