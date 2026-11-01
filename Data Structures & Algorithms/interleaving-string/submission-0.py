class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # at each step, we can either pick a letter s1[p1], or pick a letter s2[p2]
        # I have no idea what that |n - m| <= 1 property means
        # With memoization, this is O(M * N) time, O(M * N) space, where M = len(s1), N = len(s2)

        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}
        
        def dfs(p1:int, p2: int):
            key = (p1, p2)
            if key in memo:
                return memo[key]
            if p1 == len(s1) and p2 == len(s2):
                memo[key] = True
                return True
            
            res = False
            if p1 < len(s1) and s1[p1] == s3[p1 + p2]:
                res = res or dfs(p1 + 1, p2)
            if p2 < len(s2) and s2[p2] == s3[p1 + p2]:
                res = res or dfs(p1, p2 + 1)
            
            memo[key] = res
            return res
        
        return dfs(0, 0)