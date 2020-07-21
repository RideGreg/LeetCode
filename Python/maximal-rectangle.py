# Time:  O(m*n)
# Space: O(n)

# 85
# Given a 2D binary matrix filled with 0's and 1's,
# find the largest rectangle containing all ones and return its area.

# Ascending stack solution.
class Solution(object):
    def maximalRectangle(self, matrix): # USE THIS
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def largestRectangleArea(heights):
            stk, ans = [-1], 0
            for i in range(len(heights)):
                while stk[-1] != -1 and heights[i] <= heights[stk[-1]]:  # 右边界确定
                    last = stk.pop()
                    if heights[i] < heights[last]:  # 相同高度值不重复计算，只计算最后一个
                        ans = max(ans, heights[last] * (i - 1 - stk[-1]))
                stk.append(i)

            while stk[-1] != -1:  # KENG：一定要延申到数列末端之外 e.g. [2,4,5]
                ans = max(ans, heights[stk.pop()] * (len(heights) - 1 - stk[-1]))

            return ans

        if not matrix:
            return 0

        result = 0
        heights = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            result = max(result, largestRectangleArea(heights))

        return result


# DP solution.
class Solution2(object):
    # Time:  O(m*n^2) Space: O(n)
    def maximalRectangle(self, A):    # DONT USE: time complexity
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not A: return 0
        m, n, ans = len(A), len(A[0]), 0
        dp = [(0,0)] * (n+1)           # number of consecutive 1s on left and top direction

        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1][j-1] == '1':
                    dp[j] = (1+dp[j-1][0], 1+dp[j][1])
                    minHght = float('inf')
                    for k in range(dp[j][0]):
                        minHght = min(minHght, dp[j-k][1])
                        ans = max(ans, (k+1)*minHght)
                else:
                    dp[j] = (0, 0)     # need to reset because we reuse the storage
        return ans

    # Time:  O(n^2) Space: O(n)
    def maximalRectangle2(self, matrix):  # hard to understand: 3 dp array L, H, R
        if not matrix: return 0
        result = 0
        m, n = len(matrix), len(matrix[0])
        L, H, R = [0] * n, [0] * n, [0] * n

        for i in range(m):
            left = 0
            for j in range(n):
                if matrix[i][j] == '1':
                    L[j] = max(L[j], left)
                    H[j] += 1
                else:
                    L[j] = 0
                    H[j] = 0
                    R[j] = n
                    left = j + 1

            right = n
            for j in reversed(range(n)):
                if matrix[i][j] == '1':
                    R[j] = min(R[j], right)
                    result = max(result, H[j] * (R[j] - L[j]))
                else:
                    right = j
        return result

if __name__ == "__main__":
    matrix = ["01101",
              "11010",
              "01110",
              "11110",
              "11111",
              "00000"]
    print(Solution2().maximalRectangle(matrix)) # 9
