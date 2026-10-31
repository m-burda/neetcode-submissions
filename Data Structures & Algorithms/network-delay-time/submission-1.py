class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # compute a SPT for node k using Dijkstra's algorithm
        
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((t, v))

        maxtime = 0
        visited = set()

        heap = [(0, k)]
        while heap:
            path, u = heapq.heappop(heap)
            if u not in visited:
                visited.add(u)
                maxtime = max(maxtime, path)
                for t, v in graph[u]:
                    if v not in visited:
                        heapq.heappush(heap, (path + t, v))
    
        return maxtime if len(visited) == n else -1
                






        

        
    

