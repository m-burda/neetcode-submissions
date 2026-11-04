import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = defaultdict(int)
        heap = []

        for num in nums:
            counter[num] += 1
        
        for num, freq in counter.items():
            heap.append((freq, num))
        
        heapq.heapify_max(heap)

        return [heapq.heappop_max(heap)[1] for _ in range(k)]