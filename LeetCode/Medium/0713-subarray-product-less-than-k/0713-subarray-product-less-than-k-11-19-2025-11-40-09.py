class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # sliding window
        if k < 1:
            return 0
        left = 0
        total = 1
        num = 0 
        for right in range(len(nums)):
            total *= nums[right]
            while total >= k:
                total //= nums[left]
                left += 1
            
            num += right - left + 1
        
        return num