class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # init grid len(word1) + 1 x len(word2) + 1 with cells INF
        # grid[-1][-1] = 0
        # all elements in last row and col would be a sequence 1 -> len(word)
        # since we are comparing an empty string to a growing substring of a word
        # thus we will need len(substring) operations to convert "" -> <substring>

        # start at last cell
        # do nothing: go diagonally
        # deletion: 1 + go down
        # replacement: 1 + go diagonally
        # insertion: 1 + go right
        # we can imagine the letters have been inserted/replaced even if they haven't been, it doesn't matter
        # what matters is that pointers will point at correct letters on next step and the operation count is correct as well
        # if word1[i] == word2[j], grid[i][j] = grid[i + 1][j + 1]
        # else the result is 1 + min(grid[i + 1][j + 1], grid[i + 1][j], grid[i][j + 1])

        grid = [[float("inf")] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        
        grid[-1][-1] = 0
        for i in range(len(word1)):
            grid[i][-1] = len(word1) - i
        for j in range(len(word2)):
            grid[-1][j] = len(word2) - j

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    grid[i][j] = grid[i + 1][j + 1]
                else:
                    grid[i][j] = 1 + min(grid[i + 1][j + 1], grid[i + 1][j], grid[i][j + 1])

        return grid[0][0]
        