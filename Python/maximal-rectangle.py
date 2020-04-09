# Time:  O(n^2)
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
            incStack, area, i, N = [], 0, 0, len(heights)
            while i <= N:
                # 压栈只在大数进来做。栈里不存相邻的相等数，因为没必要在弹栈时一个一个计算
                if not incStack or (i < N and heights[i] > heights[incStack[-1]]):
                    incStack.append(i)
                    i += 1
                else: # 弹栈：每个高度计算一次面积，栈里往回走高度递减
                    last = incStack.pop()
                    width = i - 1 - incStack[-1] if incStack else i
                    area = max(area, heights[last] * width)
            return area

        if not matrix:
            return 0

        result = 0
        heights = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            result = max(result, largestRectangleArea(heights))

        return result

# Time:  O(n^2)
# Space: O(n)
# DP solution.
class Solution2(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
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
    print(Solution().maximalRectangle(matrix)) # 9
