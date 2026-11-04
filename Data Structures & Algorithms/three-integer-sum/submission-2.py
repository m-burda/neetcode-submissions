class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        i = 0
        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            target = -1 * nums[i]
            
            l, r = i + 1, len(nums) - 1
            while l < r:                
                current = nums[l] + nums[r]
                if current == target:
                    res.append([-1 * target, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r < len(nums) - 1 and nums[r] == nums[r + 1]:
                        r -= 1
                elif current > target:
                    r -= 1
                else:
                    l += 1
        
            i += 1

        return res

