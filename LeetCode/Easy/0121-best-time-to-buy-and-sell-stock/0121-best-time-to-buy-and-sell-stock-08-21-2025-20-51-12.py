class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        largest = 0
        least = prices[0]
        for i in range(len(prices)):
            least = min(prices[i], least)
            largest = max(prices[i] - least, largest)
        return max(dp)
            