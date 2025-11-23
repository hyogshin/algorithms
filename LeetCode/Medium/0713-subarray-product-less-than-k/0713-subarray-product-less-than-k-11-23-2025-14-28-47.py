class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # sliding window -> left = 0 and if multiplication of subarrays is larger than k -> increment left by 1 (while loop) -> else store subarrays to list and return len(stored subarrays)
        # but why is this prefix problems? is it not only sliding window, because we don't calculate prefix anywhere..

        left = 0
        prod = 1
        cnt = 0

        if k <= 0:
            return 0

        for right in range(len(nums)):
            prod *= nums[right]
            while prod >= k:
                prod //= nums[left]
                left += 1
            
            cnt += right - left + 1
        
        return cnt