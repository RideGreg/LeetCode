# Time:  O(n)
# Space: O(n)
# 84
# Given n non-negative integers representing the histogram's bar
# height where the width of each bar is 1,
# find the area of largest rectangle in the histogram.
#
# For example,
# Given height = [2,1,5,6,2,3],
# return 10.
#

class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, heights):
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

if __name__ == "__main__":
    print(Solution().largestRectangleArea([2, 2, 2])) # 6
    print(Solution().largestRectangleArea([2, 1, 2])) # 3
    print(Solution().largestRectangleArea([2, 4, 1, 5, 6, 2, 3])) # 10

