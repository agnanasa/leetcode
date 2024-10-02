class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def count_ways(n, limit):
            count = 0
            # Loop over the number of candies for the first child (x1)
            for x1 in range(0, min(n, limit) + 1):
                # Loop over the number of candies for the second child (x2)
                for x2 in range(0, min(n - x1, limit) + 1):
                    # The third child gets the remaining candies (x3)
                    x3 = n - x1 - x2
                    # Ensure the third child does not get more than the limit
                    if 0 <= x3 <= limit:
                        count += 1
            return count
        
        # Return the result of count_ways
        return count_ways(n, limit)
