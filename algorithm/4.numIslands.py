class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    result += 1
                    self.dfs(grid, i, j)
        return result
    
    def dfs(self, grid, i, j):
        grid[i][j] = 0
        h, l = len(grid), len(grid[0])
        for x, y in [[i-1, j], [i, j-1], [i+1, j], [i, j+1]]:
            if 0<=x<h and 0<=y<l and grid[x][y]=='1':
                self.dfs(grid, x, y)


solution = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
# grid = [
#     ["1","1","1"],
#     ["0","1","0"],
#     ["1","1","1"]
# ]
res = solution.numIslands(grid)
print(res)
