class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # subarray -> prefix or sliding window -> min len -> update min_len in a loop
        # return min len of subarray >= target else 0
        
        m = 10**6
        # left and right, if it's >= target -> increment left 1 by 1 (while loop) then update minimum length
        left = 0
        s = 0
        for right in range(len(nums)):
            s += nums[right]
            while s >= target:
                m = min(m, right - left + 1)
                s -= nums[left]
                left += 1
        
        return m if m != 10**6 else 0
                