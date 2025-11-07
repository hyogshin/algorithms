import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        placed = [(-s, i) for i, s in enumerate(score)]
        heapq.heapify(placed)
        places = [''] * len(score)
        for i in range(len(placed)):
            s, idx = heapq.heappop(placed)
            if i == 0:
                places[idx] = "Gold Medal"
            elif i == 1:
                places[idx] = "Silver Medal"
            elif i == 2:
                places[idx] = "Bronze Medal"
            else:
                places[idx] = str(i+1)
        return places

