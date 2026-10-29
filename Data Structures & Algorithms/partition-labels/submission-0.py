class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # build out dict of boundaries for each letter
        # init left and right pointers
        # right pointer will point at the smallest possible right boundary at a given step
        # right = max(right, boundary[i])
        # if i coincides with <right> we reached the end of the section; add r - l + 1 to result
        # this works because if we encounter any letter that goes out of bounds of the current rightmost value, we have move the goalpost further until we reach the last occurrence of that letter

        rboundaries = {}

        for i, letter in enumerate(s):
            rboundaries[letter] = i
        
        l, r = 0, 0
        res = []

        for i, letter in enumerate(s):
            r = max(r, rboundaries[letter]) 

            if i == r:
                res.append(r - l + 1)
                l = i + 1
        
        return res