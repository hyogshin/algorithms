class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judges = set()
        unique = list()
        for i in range(1, n + 1):
            judges.add(i)
        
        for i, j in trust:
            unique.append(i)
            if i in judges:
                judges.remove(i)
        
        if len(unique) == n-1 and len(set(unique)) == 1 and judges:
            return judges.pop()
        else:
            return -1