import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        heap = []
        for num, f in freq.items():
            heapq.heappush(heap, (f, num))

            if len(heap) > k: 
                heapq.heappop(heap)

        return [num for (_, num) in heap]

        