import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        pq = [(0, k)]
        dist = {}
        
        while pq:
            time, node = heapq.heappop(pq)
            if node in dist:
                continue
            dist[node] = time
            for nei, w in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (time + w, nei))

        return max(dist.values()) if len(dist) == n else -1
