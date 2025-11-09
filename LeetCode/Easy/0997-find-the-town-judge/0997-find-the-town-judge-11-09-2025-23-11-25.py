from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_cnt = [0] * (n + 1)
        trusted_by = [0] * (n + 1)
        for a, b in trust:
            trust_cnt[a] += 1
            trusted_by[b] += 1
        
        for i in range(1, n + 1):
            if trusted_by[i] == n - 1 and trust_cnt[i] == 0:
                return i
        
        return - 1
        