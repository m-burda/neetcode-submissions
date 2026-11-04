class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1,2,4,6]
        [48,48,24,6] products_right are products that start from the end
        [ 1, 2, 8, 48] products_left are products that start from the start
        """
        products_left = [0] * len(nums)
        products_right = [0] * len(nums)
        
        multiplier = 1
        for i in range(len(nums)):
            products_left[i] = nums[i] * multiplier
            multiplier *= nums[i]

        multiplier = 1
        for i in range(len(nums) - 1, -1, -1):
            products_right[i] = nums[i] * multiplier
            multiplier *= nums[i]

        for i in range(len(nums)):
            left = products_left[i - 1] if i - 1 >= 0 else 1
            right = products_right[i + 1] if i + 1 < len(nums) else 1
            nums[i] = left * right

        return nums
