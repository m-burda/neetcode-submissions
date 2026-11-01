class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # we could also solve this using tabulation
        # init a matrix len(s1) + 1 * len(s2) + 1
        # if s1[i] != s3[i + j] and s2[i] != s3[i + j] return False
        # if s1[i] == s3[i + j], we move to i - 1, j
        # if s2[j] == s3[i + j], we move to i, j - 1
        # if we arrive at [0][0], return True
        # What happens when both strings have a match? How do we solve divergent paths?
        # If both letters have a match, it means we arrived here by either picking a letter from s1 or from s2. So if either bottom or right cell have an answer (True), then we set the cell to True
        # if s1[i] == s3[i + j], then result is True && grid[i + 1][j]
        # if s2[j] == s3[i + j], then result is True && grid[i][j + 1]
        # i guess both of these conditions already satisfy the case if both letter match
        # This is still O(M*N) time and space, and we can reduce space to O(M) or (N) since we only need the current row and an immediate bottom one

        if len(s1) + len(s2) != len(s3):
            return False

        grid = [[False] * (len(s1) + 1) for _ in range(len(s2)+1)]

        grid[-1][-1] = True

        for i in range(len(s2), -1, -1):
            for j in range(len(s1), -1, -1):
                if i < len(s2) and s2[i] == s3[i + j] and grid[i + 1][j]:
                    grid[i][j] = True
                if j < len(s1) and s1[j] == s3[i + j] and grid[i][j + 1]:
                    grid[i][j] = True
        
        return grid[0][0]

                 
