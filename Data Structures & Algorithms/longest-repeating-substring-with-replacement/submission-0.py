class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        distinct = defaultdict(int)
        max_freq = 0
        longest = 0

        l, r = 0, 0
        while r < len(s):
            distinct[s[r]] += 1
            max_freq = max(max_freq, distinct[s[r]])

            if (r - l + 1) - max_freq > k:
                distinct[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
            r += 1
        
        return longest