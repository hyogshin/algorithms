class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # weighted shortest path -> dijkstra (?)
        # how do dijkstra though
        # just studied a bit
        dist = [0] * n
        dist[start_node] = 1
        heap = []
        heapq.heappush(heap, (-1, start_node))
        graph = [[] for _ in range(n)]

        for i, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))

        while heap:
            wei, cur = heapq.heappop(heap)
            p = -wei
            if dist[cur] < p:
                continue

            for nei, prob in graph[cur]:
                if dist[nei] < dist[cur] * prob:
                    dist[nei] = dist[cur] * prob
                    heapq.heappush(heap, (-dist[nei], nei))
                
        return dist[end_node]

        