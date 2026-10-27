class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # init an array of results. Last element is always 1
        # traverse the nums array in reverse
        # for every number, if the number that comes after it is greater, we can peek into the result to see what length sequence it belongs to. Assign the maximum value of this iteration + 1 to result[i]
        # Note that we do not store the longest sequence so far in the results. We only store the longest sequence that STARTS with the number nums[i] at position i
        # O(N^2) time, O(N) space

        res = [1] * len(nums)

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    res[i] = max(res[i], 1 + res[j])
        
        return max(res)
