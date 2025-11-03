class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                total += min(neededTime[i-1], neededTime[i])
                neededTime[i] = max(neededTime[i-1], neededTime[i])
        
        return total 
        