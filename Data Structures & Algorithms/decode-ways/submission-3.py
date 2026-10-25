from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:
        # dfs with memoization

        # check amount of valid numbers on each step. Each step includes 2 consecutive digits
        # decision tree: 
        # 1. include 1st digit (if valid)
        # 2. include whole number (if valid)
        # if reached the end, return 1
        # if failed anywhere along the way, return 0
        # result is the sum of individual traversals
        # Without memoization, this has (2^N) time complexity

        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1

        ways = 0

        def is_valid_num(n: int):
            return 1 <= n <= 26
        
        @cache
        def dfs(i: int, s: str):
            print(i)
            if i >= len(s):
                return 1

            ways = 0
            single = int(s[i])

            if not is_valid_num(single):
                return 0
            else:
                ways += dfs(i + 1, s)

                if i < len(s) - 1:
                    double = single * 10 + int(s[i + 1])
                    if is_valid_num(double):
                        ways += dfs(i + 2, s)
            
            return ways

        return dfs(0, s)