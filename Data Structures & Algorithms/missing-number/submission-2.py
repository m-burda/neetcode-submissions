class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # O(N) space is trivial

        expected = {i for i in range(len(nums) + 1)}
        for num in nums:
            expected.discard(num)

        return expected.pop()