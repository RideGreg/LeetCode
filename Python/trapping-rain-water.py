# Time:  O(n)
# Space: O(1)
#
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
#  compute how much water it is able to trap after raining.
#
# For example,
# Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped.
#

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):  # USE THIS
        result = 0
        topId = A.index(max(A)) # first peak is enough, even there are multiple highest bars

        leftH = 0
        for i in range(topId):
            if A[i] > leftH:
                leftH = A[i]
            else:
                result += leftH - A[i]

        rightH = 0
        for i in reversed(range(topId+1, len(A))):
            if A[i] > rightH:
                rightH = A[i]
            else:
                result += rightH - A[i]

        return result

# similar bad worse than Solution 1, but use two lists to store leftMax/rightMax (左右方向的peak)
# solution 1 is smart by finding the peak and divide array into two parts.

# Time O(n) Space O(n) 三次遍历
# 存储数组中从下标 i 到最左端最高的条形块高度 left_max。
# 存储数组中从下标 i 到最右端最高的条形块高度 right_max。
# 扫描数组height, 累加 min(max_left[i], max_right[i]) − height[i] 到 ans
class Solution2(object):
    def trap(self, height):
        N = len(height)
        if N == 0: return 0

        lMax, rMax = [0]*N, [0]*N
        lMax[0] = height[0]
        for i in range(1, N):
            lMax[i] = max(height[i], lMax[i-1])
        rMax[-1] = height[-1]
        for i in range(N-2, -1, -1):
            rMax[i] = max(height[i], rMax[i+1])
        return sum(min(lMax[i], rMax[i])-height[i] for i in range(1, N-1))


# Time:  O(n)
# Space: O(n)
# 不用像方法2那样存储最大高度，用栈来跟踪可能储水的最长的条形块。使用栈就可以在一次遍历内完成计算。
#
# 遍历数组时维护一个栈。如果当前的条形块小于或等于栈顶的条形块，我们将条形块的索引入栈，意思是
# 当前的条形块被栈中的前一个条形块界定。如果我们发现一个条形块长于栈顶，我们可以确定栈顶的条形块
# 被当前条形块和栈的前一个条形块界定，因此我们可以弹出栈顶元素并且累加答案到ans 。
#
# 算法
# - 使用栈来存储条形块的索引下标。
# - 遍历数组：
#   - 当栈非空且 height[current]>height[st.top()]
#     - 意味着栈中元素可以被弹出。弹出栈顶元素 \text{top}top。
#     - 计算当前元素和栈顶元素的距离，准备进行填充操作 distance=current−st.top()−1
#     - 找出界定高度 bounded_height=min(height[current],height[st.top()])−height[top]
#     - 往答案中累加积水量 ans+=distance×bounded_height
#   - 将当前索引下标入栈, 将current 移动到下个位置
#
class Solution3:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):  # THIS stack solution also worth to remember
        ans, i, decStk = 0, 0, []
        for i in range(len(A)):
            while decStk and A[i] > A[decStk[-1]]:
                last = decStk.pop()
                if decStk:   # 存在左边界
                    width = i - 1 - decStk[-1]
                    h = min(A[i], A[decStk[-1]]) - A[last]
                    ans += width * h
            decStk.append(i)
        return ans

    def trap_kamyu(self, A): # hard to understand, pop then push same item??
        result = 0
        stack = []

        for i in range(len(A)):
            mid_height = 0
            while stack:
                [pos, height] = stack.pop()
                result += (min(height, A[i]) - mid_height) * (i - pos - 1)
                mid_height = height

                if A[i] < height:
                    stack.append([pos, height])
                    break
            stack.append([i, A[i]])

        return result


if __name__ == "__main__":
    print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])) # 6 input has single peak
    print(Solution().trap([1,0,2,1,0,2,0,1])) # 5 input has multiple peaks
