class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # Top-down DP with memoization

        # running a loop and checking dict for occurences would have a O(N^2) time complexity since we're creating new strings at each step
        # what if for "applepenorange" there's "apple", "pen", and "penorange" in the dict?
        # A single loop would not suffice. We need to explore until the end of the string on each split
        # Traverse the whole string and run "side jobs" each time a word is discovered mid-string. If the whole segment is in dict or is segmentable, return True

        memo = {}

        if s in wordDict:
            return True

        def is_segmentable(s: str, start: int) -> bool:
            key = (start, len(s))
            if start > 0 and memo.get(key):
                return True if memo[key] == 1 else False
            
            if start > 0 and s[start:] in wordDict:
                memo[key] = 1
                return True
            for i in range(start + 1, len(s) + 1):
                if s[start:i] in wordDict:
                    key = (start, i)
                    if memo.get(key):
                        return True if memo[key] == 1 else False
                    
                    if is_segmentable(s, i):
                        memo[key] = 1
                        return True
            memo[(start, len(s))] = -1
            return False
        
        for i in range(len(s)):
            if is_segmentable(s, 0):
                return True
        
        return False
