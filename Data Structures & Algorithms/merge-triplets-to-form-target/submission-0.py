class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        # O(N) time, O(1) space

        best = [False] * 3

        for triplet in triplets:
            valid = True
            for i in range(3):
                if triplet[i] > target[i]:
                    valid = False
            if valid:
                for i in range(3):
                    if triplet[i] == target[i]:
                        best[i] = True

        return all(best)