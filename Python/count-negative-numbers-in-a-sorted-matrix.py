# Time:  O(m + n) at most move m+n steps
# Space: O(1)

# 1351 weekly contest 176 2/15/2020

# Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.
#
# Return the number of negative numbers in grid.

# intuition: the divide line is like a staircase. "Trace" the outline of the staircase.
# ++++--
# ++++--
# +++---
# +-----
# For # of negative numbers, traverse row 1->m, starting from col n
# For # of positive numbers, traverse row m->1, starting from col 1
# Also see 240. Search a 2D Matrix II

class Solution(object):
    def countNegatives(self, grid): # USE THIS: linear time
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # c: smallest col which is not valid (i.e. >=0) because cannot guarantee initial col is valid
        result, c = 0, len(grid[0])-1
        for row in grid:
            while c >= 0 and row[c] < 0:
                c -= 1
            result += len(grid[0])-1-c
        return result

    # Binary search: O(mlogn). bisect module not working in decreasing sequence.
    def countNegatives_ming(self, grid):
        def valid(row, m):
            return row[m] < 0

        ans = 0
        for row in grid:
            l, r = 0, len(row)
            while l < r:
                m = (l + r) // 2
                if valid(row, m):
                    r = m
                else:
                    l = m + 1
            ans += len(row)-l
        return ans

        # NOTE the below is O(mn) as it construct the rows
        # return sum(map(lambda x: bisect_left(x[::-1], 0), grid))

print(Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])) # 8
print(Solution().countNegatives([[3,2],[1,0]])) # 0
print(Solution().countNegatives([[1,-1],[-1,-1]])) # 3