class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        has_zero = False
        for num in nums:
            if num != 0:
                product *= num
            else:
                if has_zero:
                    product = 0
                else:
                    has_zero = True

        if has_zero is True:
            return [0 if num != 0 else product for num in nums]

        return [product // num for num in nums]