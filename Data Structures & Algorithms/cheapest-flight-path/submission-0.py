class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # we cannot use Dijkstra's algorithm direcly because of k stops constraint
        # we use bfs with queue and add outgoing edges to minheap only if the stops would not exceed k
        # then we can do edge relaxation

        # time O(E * k), space(V + E)

        queue = collections.deque()
        queue.appendleft((0, src, -1))

        dist_to = [float("inf")] * n
        dist_to[src] = 0

        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((w, v))

        while queue:
            path, u, stops = queue.pop()

            stops += 1
            
            if stops <= k:
                for w, v in graph[u]:
                    if path + w < dist_to[v]:
                        dist_to[v] = path + w
                        queue.appendleft((path + w, v, stops))
        
        
        return dist_to[dst] if dist_to[dst] != float("inf") else -1

