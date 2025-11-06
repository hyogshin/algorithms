from collections import defaultdict
import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = [''] * len(score)
        heap = [(-s, i) for i, s in enumerate(score)]
        heapq.heapify(heap)

        rank = 1
        while heap:
            s, i = heapq.heappop(heap)
            if rank == 1:
                ranks[i] = "Gold Medal"
            elif rank == 2:
                ranks[i] = "Silver Medal"
            elif rank == 3:
                ranks[i] = "Bronze Medal"
            else:
                ranks[i] = str(rank)

            rank += 1

        return ranks