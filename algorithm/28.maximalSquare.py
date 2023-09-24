class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        maxSize = 0
        dp = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            if matrix[i][0]=='1':
                dp[i][0]=1
                maxSize = 1
        for j in range(len(matrix[0])):
            if matrix[0][j]=='1':
                dp[0][j]=1
                maxSize = 1
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j]=='1':
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1
                    maxSize = max(maxSize, dp[i][j])
        return maxSize**2


solution = Solution()
res = solution.maximalSquare([["0"],["1"]])
print(res)
