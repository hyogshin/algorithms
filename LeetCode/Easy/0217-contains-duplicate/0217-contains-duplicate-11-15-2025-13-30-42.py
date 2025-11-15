from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup = defaultdict(int)
        for n in nums:
            dup[n] += 1
            if dup[n] > 1:
                return True
        
        return False
        