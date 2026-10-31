class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        # Compute an MST
        # We could either use Kruskal's or Prim's
        # This would take V^2 either way since we don't have pre-computed edges
        # time V^2logV, space O(V*V!)
        mst = set()
        cost = 0
        
        heap = [(0, tuple(points[0]))]
        # Prim's algo: take the smallest edge where vertex is in mst, add it to the tree
        while heap:
            w, p1 = heapq.heappop(heap)
            p1 = tuple(p1)
            if p1 not in mst:
                cost += w
                for i, p2 in enumerate(points):
                    if tuple(p2) not in mst:
                        weight = abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
                        heapq.heappush(heap, (weight, p2))
            
            mst.add(p1)
            
        return cost if len(mst) == len(points) else -1

        