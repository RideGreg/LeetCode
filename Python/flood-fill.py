# Time:  O(m * n)
# Space: O(m * n)

# An image is represented by a 2-D array of integers,
# each integer representing the pixel value of the image (from 0 to 65535).
#
# Given a coordinate (sr, sc) representing the starting pixel (row and column)
# of the flood fill, and a pixel value newColor, "flood fill" the image.
#
# To perform a "flood fill", consider the starting pixel,
# plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel,
# plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel),
# and so on. Replace the color of all of the aforementioned pixels with the newColor.
#
# At the end, return the modified image.
#
# Example 1:
# Input:
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation:
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
# by a path of the same color as the starting pixel are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected
# to the starting pixel.
#
# Note:
# - The length of image and image[0] will be in the range [1, 50].
# - The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
# - The value of each color in image[i][j] and newColor will be an integer in [0, 65535].

class Solution(object):
    def floodFill(self, image, sr, sc, newColor): # USE THIS
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        clr = image[sr][sc]
        if clr == newColor:
            return image

        m, n = len(image), len(image[0])
        stk = [(sr, sc)]
        image[sr][sc] = newColor
        while stk:
            r, c = stk.pop()
            for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                if 0<=nr<m and 0<=nc<n and image[nr][nc] == clr:
                    stk.append((nr, nc))
                    image[nr][nc] = newColor
        return image


    def floodFill_recur(self, image, sr, sc, newColor):
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def dfs(image, r, c, newColor, color):
            if not (0 <= r < len(image) and \
                    0 <= c < len(image[0]) and \
                    image[r][c] == color):
                return

            image[r][c] = newColor
            for d in directions:
                dfs(image, r+d[0], c+d[1], newColor, color)

        color = image[sr][sc]
        if color == newColor: return image
        dfs(image, sr, sc, newColor, color)
        return image
