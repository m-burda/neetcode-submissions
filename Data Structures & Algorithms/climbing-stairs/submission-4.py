class Solution:
    def climbStairs(self, n: int) -> int:
        # start from the end
        # to reach n from n - 1, there is 1 way
        # to reach n from n - 2, there are 2 ways
        # add up distinct ways on each step to arrive at 0

        # optimization: we are only interested in the last 2 results, so keep those in 2 variables instead of an array of size n. Memory complexity is reduced to constant
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        left, right = 1, 2

        for i in range(n - 2):
            temp = left + right
            left = right
            right = temp
        
        return right
