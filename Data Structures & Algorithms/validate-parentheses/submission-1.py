class Solution:
    def isValid(self, s: str) -> bool:
        counterparts = {"]": "[", "}":"{", ")":"("}
        stack = collections.deque()

        for b in s:
            if b not in counterparts:
                stack.append(b)
            else:
                if not stack or stack.pop() != counterparts[b]:
                    return False
        
        return not stack