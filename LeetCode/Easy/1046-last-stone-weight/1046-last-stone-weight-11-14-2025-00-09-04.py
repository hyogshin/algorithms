import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        weights = []
        for w in stones:
            heapq.heappush(weights, -w)

        while len(weights) >= 2:
            y = heapq.heappop(weights)
            x = heapq.heappop(weights)
            if y != x:
                heapq.heappush(weights, y-x)

        if len(weights) == 1:
            return -heapq.heappop(weights)
    
        elif len(weights) == 0:
            return 0