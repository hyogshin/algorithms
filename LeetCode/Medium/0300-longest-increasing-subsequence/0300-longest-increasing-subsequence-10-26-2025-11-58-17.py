class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums))
        dp[0] = 1

        if len(nums) > 1:
            if nums[0] < nums[1]:
                dp[1] = max(dp[0] + 1, dp[1])
            else:
                dp[1] = 1

            for i in range(2, len(nums)):
                for j in range(i):
                    if nums[j] < nums[i]:
                        dp[i] = max(dp[j] + 1, dp[i])
        
        return max(dp)

        