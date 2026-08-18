class Solution:
    def fill(self, image, r, c, original_color, color, visited):
        # Row or column is out of bounds
        if min(r, c) < 0 or r == len(image) or c == len(image[r]):
            return
        
        # We've already visited this
        if (r, c) in visited:
            return

        # This is a different color
        if image[r][c] != original_color:
            return

        # Mark visited, and color it
        visited.add((r, c))
        image[r][c] = color

        # Visit all adjacent cells
        self.fill(image, r + 1, c, original_color, color, visited)
        self.fill(image, r - 1, c, original_color, color, visited)
        self.fill(image, r, c + 1, original_color, color, visited)
        self.fill(image, r, c - 1, original_color, color, visited)
        
        return
        

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        self.fill(image, sr, sc, image[sr][sc], color, set())

        return image

