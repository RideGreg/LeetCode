# Time:  O(n^3) ~ O(n^4)
# Space: O(n^3)

# 546
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


# DP: 首先把连续相同颜色的盒子进行合并，得到数组color以及数组length，分别表示合并后盒子的颜色和长度。
#
# dp[l][r][k]表示第l到第r个合并后的盒子，连同其后颜色为color[r]的长度k一并消去所能得到的最大得分。
#
# 状态转移方程：
# 1. 相邻盒子不会同色，移除最后一个盒子进行递归计算
# dp[l][r][k] = dp[l][r - 1][0] + (length[r] + k) ** 2
# 2. 不相邻盒子可能与最后一个盒子同色，先移除中间所有盒子
# dp[l][r][k] = max(dp[l][r][k], dp[l][i][length[r] + k] + dp[i + 1][r - 1][0])  其中 i ∈[l, r - 1]

class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        def dfs(l, r, k):
            if l > r: return 0
            if not dp[l][r][k]:
                # 因为已经事先合并，相邻盒子不会同色，移除最后一个盒子进行递归计算
                points = dfs(l, r - 1, 0) + (length[r] + k) ** 2

                # 检查不相邻盒子有否与最后一个盒子同色，就先移除中间所有盒子
                for i in range(l, r):
                    if color[i] == color[r]:
                        points = max(points, dfs(l, i, length[r] + k) + dfs(i + 1, r - 1, 0))
                dp[l][r][k] = points
            return dp[l][r][k]

        color, length = [], []
        for box in boxes:
            if color and color[-1] == box:
                length[-1] += 1
            else:
                color.append(box)
                length.append(1)
        M, N = len(color), len(boxes)
        # two outer loop indices are l, r which are less than M, most inner loop is k which can be up to N
        dp = [[[0] * N for _ in range(M)] for _ in range(M)]
        return dfs(0, M - 1, 0)


    # same algorithm as above, but don't pre-merge. Worse.
    def removeBoxes2(self, boxes):
        def dfs(l, r, k):
            if l > r: return 0
            if dp[l][r][k]: return dp[l][r][k]

            ll, kk = l, k
            while l < r and boxes[l+1] == boxes[l]:
                l += 1
                k += 1
            result = dfs(l+1, r, 0) + (k+1) ** 2
            for i in range(l+1, r+1):
                if boxes[i] == boxes[l]:
                    result = max(result, dfs(l+1, i-1, 0) + dfs(i, r, k+1))
            dp[ll][r][kk] = result
            return result

        dp = [[[0]*len(boxes) for _ in range(len(boxes)) ] for _ in range(len(boxes)) ]
        return dfs(0, len(boxes)-1, 0)


print(Solution().removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1])) # 23
print(Solution().removeBoxes([1] * 10 + [2,1,3] + [1] * 87))
# 9606. color = [1,2,1,3,1], length = [10,1,1,1,87]
