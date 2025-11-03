class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        dp = [0] * len(colors)

        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                dp[i] = dp[i-1] + min(neededTime[i], neededTime[i-1])
                neededTime[i] = max(neededTime[i], neededTime[i-1])
            else:
                dp[i] = dp[i-1]
        return dp[-1]
