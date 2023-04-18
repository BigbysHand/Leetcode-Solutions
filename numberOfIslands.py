class Solution(object):
    def sink(self, grid, x, y):
        #set boundaries
        if (x<0 or x>=len(grid)) or \
        (y<0 or y>=len(grid[0])) or \
        (grid[x][y] == "0"):
            return
        #set current point to "0"
        grid[x][y] = "0"

        #sink any adjacent recur
        self.sink(grid, x-1, y)
        self.sink(grid, x+1, y)
        self.sink(grid, x, y-1)
        self.sink(grid, x, y+1)

    def numIslands(self, grid):
        islands = 0
        #scan over the grid and find a 1
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                #inc and sink island
                if grid[x][y] == "1":
                    islands += 1
                    self.sink(grid, x, y)
        #ret islands sunk
        return islands