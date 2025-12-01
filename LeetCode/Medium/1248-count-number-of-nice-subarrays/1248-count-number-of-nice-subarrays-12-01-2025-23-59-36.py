class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        odds = 0
        ans = 0
        
        for x in nums:
            if x % 2:
                odds += 1
            
            # odds - k 가 이전에 몇 번 나왔는지
            ans += prefix.get(odds - k, 0)
            
            prefix[odds] = prefix.get(odds, 0) + 1
        
        return ans
