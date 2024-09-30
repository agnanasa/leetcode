
from typing import List

grid = [[1, 2, 3], [2, 3, 4]]
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # Step 1: Sort each row in descending order
        for row in grid:
            row.sort(reverse=True)
        
        sum_value = 0
        # Step 2: Repeat the operation while columns are still left
        # Iterate as many times as the number of columns (len(grid[0]))
        while grid[0]:
            max_in_iteration = 0  # Store the max value deleted in this iteration
            for row in grid:
                # Remove the first (greatest) element in the row
                max_in_iteration = max(max_in_iteration, row.pop(0))  # pop the largest in each row
            # Add the largest element of the iteration to the total sum
            sum_value += max_in_iteration
        
        return sum_value
