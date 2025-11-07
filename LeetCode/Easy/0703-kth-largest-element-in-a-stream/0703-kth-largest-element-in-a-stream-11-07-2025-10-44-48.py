import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [i for i in nums]
        heapq.heapify(self.heap)
        if len(self.heap) > k:
            for i in range(len(self.heap)-k):
                heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:       
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            for i in range(len(self.heap) - self.k):
                heapq.heappop(self.heap)
        return self.heap[0] if self.heap else None
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)