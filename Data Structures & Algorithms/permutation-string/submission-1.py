class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        diff = len(s1)
        window_size = len(s1)

        for char in s1:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        for i in range(len(s2)):
            if s2[i] in count:
                if count[s2[i]] > 0:
                    diff -= 1
                count[s2[i]] -= 1
            
            if i >= window_size:
                excess_char = s2[i - window_size]
                if excess_char in count:
                    count[excess_char] += 1
                    if count[excess_char] > 0:
                        diff += 1
            
            if diff == 0:
                return True

        return diff == 0