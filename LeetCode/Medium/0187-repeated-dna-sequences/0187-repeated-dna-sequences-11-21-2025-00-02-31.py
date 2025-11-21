class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        repeated = set()
        left = 0 
        for right in range(9, len(s)):
            if s[left:right+1] in seen:
                repeated.add(s[left:right+1])
            seen.add(s[left:right+1])
            left += 1
            
        return list(repeated)