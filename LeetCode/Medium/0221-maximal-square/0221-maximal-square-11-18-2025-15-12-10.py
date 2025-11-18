class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # if the pivot is left top square
        # to make another square I have to travel to bottom, next, and right bottom diagonial.
        # but what if it's bigger than that,
        # then, save it to dp and start another travel from bottom left square to to aound the original square
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        rs = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                    rs = max(dp[i][j], rs)

        return rs ** 2