from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        h = []
        for n, frq in counter.items():
            heapq.heappush(h, (frq, n))

            if len(h) > k:
                heapq.heappop(h)
            
        
        return [n for frq, n in h]
            
        