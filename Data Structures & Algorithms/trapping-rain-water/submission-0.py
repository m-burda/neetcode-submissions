class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        
        max_heights_l = [0] * len(height)
        max_heights_r = [0] * len(height)
        water = [0] * len(height)
        
        max_height_l = 0
        for i in range(len(height)):
            max_height_l = max(max_height_l, height[i])
            max_heights_l[i] = max_height_l

        max_height_r = 0
        for i in range(len(height) - 1, -1, -1):
            max_height_r = max(max_height_r, height[i])
            max_heights_r[i] = max_height_r

        for i in range(1, len(water) - 1):
            water[i] = min(max_heights_l[i - 1], max_heights_r[i + 1]) - height[i]
            water[i] = max(0, water[i])
        
        return sum(water)


        


