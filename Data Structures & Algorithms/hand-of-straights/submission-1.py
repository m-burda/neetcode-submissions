class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        # brute force approach:
        # 1. start with the smallest number in the remaining array
        # 2. find a number that is == prevNum + 1
        # 3. Repeat #2 until reached groupSize
        # 4. Repeat #1 until reached the end
        # Time complexity would be through the roof

        # Proposition
        # Sort the array
        # Start with the second element
        # If cur == prev + 1, continue
        # If cur == prev, push it to a queue
        # Else, return False
        # When i % groupSize, pop the queue and set prev to that element
        # Repeat until reached the end
        # time O(NlogN), space O(groupSize)

        # The code is fragile incomplete dogwater
        # This cannot be the best solution

        # Using a counter
        # Add cur to the counter. If there is a value of <cur - 1> in the counter, decrement it.
        # By the end, if we have len(counter) > groupSize OR any of the values have count > 1, return False
        # Or even simpler, if the sum of the values in the counter != groupSize, return False

        # But if we follow this logic, we shouldn't decrement the number if the first number of the next group is equal to the last number of the previous group. How do we ensure that doesn't happen?

        # it seems we have to run an additional loop of size groupSize regardless
        # challenge: how to determine the first element of each group?
        # heapify the array
        # we pop the heap until we find the next starting element of the group. If the counter for last popped element is 0, it means it must have been used for the previous group already
        # when we find the next element, keep decrementing the counters for numbers in range (i, i + groupSize)
        # if any of the numbers drop below 0 during decrementing, it means it's impossible to construct a proper group

        # space O(N), time O(NlogN), where G is groupSize

        if len(hand) % groupSize:
            return False

        counter = Counter(hand)
        heapq.heapify(hand)
        
        for group in range(len(hand) // groupSize):
            groupMin = heapq.heappop(hand)
            # if it's 0, it must have already been added to prev group in the loop that comes after
            while counter[groupMin] == 0:
                groupMin = heapq.heappop(hand)
            
            for groupNum in range(groupMin, groupMin + groupSize):
                counter[groupNum] -= 1
                # if the count is < 0, this defies the happy path logic
                if counter[groupNum] < 0:
                    return False

        return True
