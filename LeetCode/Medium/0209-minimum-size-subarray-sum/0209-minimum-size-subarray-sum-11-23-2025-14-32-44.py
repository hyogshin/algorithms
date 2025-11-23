class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # subarray sum -> prefix
        # return minimum length of subarray else 0

        length = []
        prefix = 0
        left = 0
        for right in range(len(nums)):
            prefix += nums[right]
            while prefix >= target:
                length.append(right - left + 1)
                prefix -= nums[left]
                left += 1
        
        return min(length) if length else 0