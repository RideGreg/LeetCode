# Time:  O(m * n)
# Space: O(m + n)

# 1267 weekly contest 164 11/23/2019

# You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that
# on that cell there is a server and 0 means that it is no server. Two servers are said to communicate
# if they are on the same row or on the same column.
#
# Return the number of servers that communicate with any other server.


class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        rowCnts, colCnts = [0]*m, [0]*n
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    rowCnts[i] += 1
                    colCnts[j] += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                ans += int(grid[i][j] and (rowCnts[i] > 1 or colCnts[j] > 1) )
        return ans

print(Solution().countServers([[1,0],[0,1]])) # 0
print(Solution().countServers([[1,0],[1,1]])) # 3
print(Solution().countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]])) # 4