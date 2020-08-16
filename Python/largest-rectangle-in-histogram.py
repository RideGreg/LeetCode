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

# 要点是如何确定每个高度值所在矩形的左右边界：左边界为上一个比自己小的数或数列起始段(记为-1)，
# 大数来，栈里数都保留，因为右边界还可延申
# 小数来或到达数列末端，栈里大数右边界确定，弹出并计算面积
class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, heights):  # USE THIS
        heights.append(0)   # KENG：一定要延申到数列末端之外 e.g. [2,4,5]
        stk, ans = [-1], 0
        for i, h in enumerate(heights):
            while len(stk) > 1 and h <= heights[stk[-1]]: # 右边界确定。相同高度值也弹出，只保留最后一个
                last = stk.pop()
                width =  i - 1 - stk[-1]
                ans = max(ans, heights[last] * width)
            stk.append(i)
        return ans


    def largestRectangleArea_kamyu(self, heights):
        incStack, area, i, N = [], 0, 0, len(heights)
        while i <= N: # KENG：一定要延申到数列末端之外
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
    print(Solution().largestRectangleArea([2, 4, 5])) # 8
    print(Solution().largestRectangleArea([2, 2, 2])) # 6
    print(Solution().largestRectangleArea([2, 1, 2])) # 3
    print(Solution().largestRectangleArea([2, 4, 1, 5, 6, 2, 3])) # 10

