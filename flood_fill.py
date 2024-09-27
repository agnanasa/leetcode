class Solution:
    def floodFill(self, image, sr, sc, color):
        # Get the original color of the starting pixel
        original_color = image[sr][sc]

        # If the new color is the same as the original color, no need to proceed
        if original_color == color:
            return image

        # Define the directions (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # DFS function to fill the image
        def dfs(x, y):
            # Check bounds and if the current pixel is of the original color
            if x < 0 or x >= len(image) or y < 0 or y >= len(image[0]) or image[x][y] != original_color:
                return
            # Change the color of the current pixel
            image[x][y] = color
            # Recursively check the adjacent pixels
            for dx, dy in directions:
                dfs(x + dx, y + dy)

        # Start the flood fill from the given pixel
        dfs(sr, sc)

        # Return the modified image
        return image
