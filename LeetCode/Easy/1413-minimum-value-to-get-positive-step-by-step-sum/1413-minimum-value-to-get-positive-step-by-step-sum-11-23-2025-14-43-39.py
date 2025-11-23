class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = 0
        min_prefix = 101
        for i, n in enumerate(nums):
            prefix += n
            min_prefix = min(min_prefix, prefix)

        if min_prefix > 0:
            return 1
        else:
            return  1 - min_prefix