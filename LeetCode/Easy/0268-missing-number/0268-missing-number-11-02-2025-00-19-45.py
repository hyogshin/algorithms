class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        expected_sum = sum(i for i in range(min(nums), max(nums) + 1))
        actual_sum = sum(nums)
        return max(nums) + 1 if expected_sum - actual_sum in nums else expected_sum - actual_sum
