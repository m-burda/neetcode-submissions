class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = defaultdict(int)

        for c in s:
            counter[c] += 1
        for c in t:
            counter[c] -= 1
        
        for val in counter.values():
            if val != 0:
                return False
        
        return True