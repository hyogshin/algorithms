class Solution:
    def romanToInt(self, s: str) -> int:
        # is it hash map? key == symbol and value is value, then just matching keys to find values.
        # 18/11/25 store roman symbol, val to defaultdict (hashmap) and search it when I get inputs but when i get input smaller than next roman symbol i need to substract it.
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M':1000}
        integer = 0
        for i in range(len(s)):
            if i < len(s):
                if symbols[s[i]] < symbols[s[i + 1]]:
                    integer += symbols[s[i + 1]] - symbols[s[i]]
                    continue
                integer += symbols[s[i]]
        
        return integer
                