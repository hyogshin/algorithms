class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        res = 0
        
        is_sorted = [False] * (n - 1)
        
        for j in range(m):
            is_bad = False
            for i in range(n - 1):
                if not is_sorted[i] and strs[i][j] > strs[i+1][j]:
                    is_bad = True
                    break
            
            if is_bad:
                res += 1
            else:
                for i in range(n - 1):
                    if strs[i][j] < strs[i+1][j]:
                        is_sorted[i] = True
                        
        return res