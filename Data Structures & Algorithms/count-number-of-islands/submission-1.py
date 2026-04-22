class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #search through graph for all 1s == islands
        # i want to ALSO check up down and left right neighbor 
        # keep track of the islands i have gone too

        rows = len(grid)
        cols = len(grid[0])

        isles = 0

        def dfs(x, y):
            if x >= rows or y >= cols or x < 0 or y < 0 or grid[x][y] == "0":
                return
            
            grid[x][y] = "0"

            dfs(x + 1, y)
            dfs(x -1, y)
            dfs(x, y + 1)
            dfs(x, y -1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    isles += 1
                    dfs(r, c)
        return isles
        