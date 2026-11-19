class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        p1, p2 = 0, 1
        if len(s) <= 1:
            return len(s)
        
        longest = 0
        unique = set(s[p1])
        while p2 < len(s):
            while s[p2] in unique:
                unique.remove(s[p1])
                p1 += 1

            unique.add(s[p2])

            longest = max(longest, p2 - p1 + 1)
            p2 += 1
        
        return longest