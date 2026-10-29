class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # gas=[1,2,3,4,5]
        # cost=[3,4,5,1,2]
        # diffs = [-2, -2, -2, 3, 3]

        # gas=[5,8,2,8]
        # cost=[6,5,6,6]
        # diffs=[-1,3,-4,2]
        # Observations: we can only start at a non-negative diff if we want to arrive successfully
        # <i + 1>th - <i>th diff should always be positive
        # If the sum of the diffs is < 0, there is no answer

        # We traverse the diffs and keep track of our gas amount (total)
        # If total ever drops below 0, we reset it to 0 and more the answer to i + 1
        # If the total dropped to 0, we don't set the answer anywhere before current index. This is because we failed to drive the route even starting from point A, which produced a net positive. This means that there is no point in trying to compute the total from any intermediate points, since the net would be even smaller -> we would not reach the end anyway.
        # By the same logic, the first station in the sequence where the total is >= 0 is our answer, since we know that there exists only one answer to the problem.

        # We can drop the diffs array completely to make space complexity constant

        diffs = [gas[i] - cost[i] for i in range(len(gas))]

        if sum(diffs) < 0:
            return -1
        
        res = 0
        total = 0

        for i, diff in enumerate(diffs):
            total += diff
            if total < 0:
                total = 0
                res = i + 1
        
        return res
