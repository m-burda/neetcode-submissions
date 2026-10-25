class Solution:
    def countSubstrings(self, s: str) -> int:
        # same as longest palindrom, except update the counter instead of pointers
        # time O(N^2), space O(1)
        palindroms = 0
        
        for i in range(len(s)):
            for r in range(i, i + 2):
                l = i
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    palindroms += 1

                    l -= 1
                    r += 1
        
        return palindroms
