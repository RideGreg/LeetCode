import collections


class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        clr = image[sr][sc]
        if clr == newColor:
            return image
        image[sr][sc] = newColor
        queue = collections.deque([])
        queue.append((sr, sc))

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            x, y = queue.popleft()
            for dx, dy in dirs:
                i, j = x + dx, y + dy
                if (0 <= i < len(image)) and (0 <= j < len(image[0])) and image[i][j] == clr:
                    queue.append((i, j))
                    image[i][j] = newColor

        return image

print Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)


