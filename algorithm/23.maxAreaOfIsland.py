class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    self.count = 1
                    grid[i][j] = 0
                    self.dfs(grid, i, j)
                    result = max(result, self.count)
        return result

    def dfs(self, grid, i, j):
        for i, j in [[i-1, j], [i, j-1], [i+1, j], [i, j+1]]:
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                continue
            if grid[i][j]==1:
                self.count+=1
                grid[i][j]=0
                self.dfs(grid, i, j)

grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]

solution = Solution()
res = solution.maxAreaOfIsland(grid)
print(res)
