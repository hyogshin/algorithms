class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(complexity)

        root = complexity[0]

        for x in complexity[1:]:
            if x <= root:
                return 0

        ans = 1
        for k in range(1, n):
            ans = ans * k % MOD

        return ans
