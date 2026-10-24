class Solution:
    def climbStairs(self, n: int) -> int:
        # start from the end
        # to reach n from n - 1, there is 1 way
        # to reach n from n - 2, there are 2 ways
        # add up distinct ways on each step to arrive at 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        ways = [1] * n
        ways[1] = 2


        for i in range(2, len(ways)):
            ways[i] = ways[i-1] + ways[i-2]
        
        print(ways)
        return ways[len(ways) - 1]
