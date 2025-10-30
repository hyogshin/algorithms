from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount % 2 != 0 and all(c % 2 == 0 for c in coins):
            return -1

        INF = amount + 1
        dp = [INF] * (amount + 1)
        dp[0] = 0

        for c in coins:
            for a in range(c, amount + 1):
                dp[a] = min(dp[a], dp[a - c] + 1)
        
        return dp[amount] if dp[amount] != INF else -1

        