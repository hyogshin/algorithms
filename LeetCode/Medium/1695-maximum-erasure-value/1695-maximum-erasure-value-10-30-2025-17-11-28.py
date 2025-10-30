class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        seen = set()
        m = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                left += 1
            seen.add(nums[right])
            m = max(m, sum(nums[left:right + 1]))
        return m