class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        champion = 0
        for i in range(1,n):
            if grid[i][champion] == 1:
                champion = i
        for j in range(n):
            if j != champion and grid[champion][j] == 0:
                return -1

        return champion