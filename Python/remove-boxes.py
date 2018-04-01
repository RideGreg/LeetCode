# Time:  O(n^3) ~ O(n^4)
# Space: O(n^3)

# Given several boxes with different colors represented by different positive numbers. 
# You may experience several rounds to remove boxes until there is no box left.
# Each time you can choose some continuous boxes with the same color (composed of k boxes, k >= 1),
# remove them and get k*k points.
# Find the maximum points you can get.
#
# Example 1:
# Input:
#
# [1, 3, 2, 2, 2, 3, 4, 3, 1]
# Output:
# 23
# Explanation:
# [1, 3, 2, 2, 2, 3, 4, 3, 1] 
# ----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
# ----> [1, 3, 3, 3, 1] (1*1=1 points) 
# ----> [1, 1] (3*3=9 points) 
# ----> [] (2*2=4 points)
# Note: The number of boxes n would not exceed 100.

class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        def dfs(boxes, l, r, k, lookup):
            if l > r: return 0
            if lookup[l][r][k]: return lookup[l][r][k]

            ll, kk = l, k
            while l < r and boxes[l+1] == boxes[l]:
                l += 1
                k += 1
            result = dfs(boxes, l+1, r, 0, lookup) + (k+1) ** 2
            for i in xrange(l+1, r+1):
                if boxes[i] == boxes[l]:
                    result = max(result, dfs(boxes, l+1, i-1, 0, lookup) + dfs(boxes, i, r, k+1, lookup))
            lookup[ll][r][kk] = result
            return result

        lookup = [[[0]*len(boxes) for _ in xrange(len(boxes)) ] for _ in xrange(len(boxes)) ]
        return dfs(boxes, 0, len(boxes)-1, 0, lookup)

    # http://bookshadow.com/weblog/2017/03/26/leetcode-remove-boxes/
    def removeBoxes_best(self, boxes): # first compress input: save space, and no need to skip index in calc
        """
        :type boxes: List[int]
        :rtype: int
        """
        self.color, self.length = [], []
        for box in boxes:
            if self.color and self.color[-1] == box:
                self.length[-1] += 1
            else:
                self.color.append(box)
                self.length.append(1)
        M, N = len(self.color), len(boxes)
        self.dp = [[[0] * N for _ in range(M)] for _ in range(M)] # innest loop is k which go up to N

        def solve(l, r, k):
            if l > r: return 0
            if self.dp[l][r][k]: return self.dp[l][r][k]
            res = solve(l + 1, r, 0) + (self.length[l] + k) ** 2
            for m in range(l + 1, r + 1):
                if self.color[m] == self.color[l]:
                    res = max(res, solve(l + 1, m - 1, 0) + solve(m, r, self.length[l] + k))
            self.dp[l][r][k] = res
            return res

        return solve(0, M - 1, 0)

    def removeBoxes_iteration(self, boxes): #TLE, fill many values which are not needed
        n = len(boxes)
        dp = [[[0]*n for _ in xrange(n)] for _ in xrange(n)]
        for j in xrange(n):
            for i in reversed(xrange(j+1)):
                for k in reversed(xrange(i+1)):
                    if i == j:
                        dp[i][j][k] = (k+1)**2
                    else:
                        res = dp[i+1][j][0] + (k+1)**2
                        for m in xrange(i+1, j+1):
                            if boxes[m] == boxes[i]:
                                res = max(res, dp[i+1][m-1][0] + dp[m][j][k+1])
                        dp[i][j][k] = res
        return dp[0][n-1][0]

print Solution().removeBoxes([3,2,2,3]
'''
i j k  =>  dp[i][j][k]
3 3 0 => 1
1 3 0 => 5
1 2 0 => 4
3 3 1 => 4
0 3 0 => 8
'''
print Solution().removeBoxes_iteration([3,2,2,3])
'''
i j k  =>  dp[i][j][k]
0 0 0  =>  1
1 1 1  =>  4
1 1 0  =>  1
0 1 0  =>  2
2 2 2  =>  9
2 2 1  =>  4
2 2 0  =>  1
1 2 1  =>  9
1 2 0  =>  4
0 2 0  =>  5
3 3 3  =>  16
3 3 2  =>  9
3 3 1  =>  4
3 3 0  =>  1
2 3 2  =>  10
2 3 1  =>  5
2 3 0  =>  2
1 3 1  =>  10
1 3 0  =>  5
0 3 0  =>  8
'''
#print Solution().removeBoxes_iteration([1,3,2,2,2,3,4,3,1])