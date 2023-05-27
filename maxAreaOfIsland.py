class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.count = 0
        def dfs(grid, x,y, res):
            if 0 <= x < len(grid) and 0 <= y < len(grid[x]) and grid[x][y]:
                grid[x][y] = 0
                self.count += 1
                dfs(grid, x-1, y, res)
                dfs(grid, x+1, y, res)
                dfs(grid, x, y+1, res)
                dfs(grid, x, y-1, res)
                return res
            return 
        
        maxarea = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    self.count = 0
                    area = dfs(grid, i, j, 0) 
                    maxarea = max(self.count, maxarea)
        
        return maxarea