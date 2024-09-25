class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows = len(grid)
        columns = len(grid[0])

        for row in range(rows):
            for island in range(columns):
                if grid[row][island] == 1:
                    perimeter += 4
                    # Check if there's land to the left
                    if island > 0 and grid[row][island-1] == 1:
                        perimeter -= 2
                    # Check if there's land above
                    if row > 0 and grid[row-1][island] == 1:
                        perimeter -= 2
        return perimeter