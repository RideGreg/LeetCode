# Time:  O(n)
# Space: O(26) = O(1)

# 621
# Given a char array representing tasks CPU need to do.
# It contains capital letters A to Z where different letters represent
# different tasks.Tasks could be done without original order.
# Each task could be done in one interval.
# For each interval, CPU could finish one task or just be idle.
#
# However, there is a non-negative cooling interval n that
# means between two same tasks, there must be at least n intervals that
# CPU are doing different tasks or just be idle.
#
# You need to return the least number of intervals the CPU
# will take to finish all the given tasks.
#
# Example 1:
# Input: tasks = ['A','A','A','B','B','B'], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
# Note:
# The number of tasks is in the range [1, 10000].
# The integer n is in the range [0, 100].

import collections, heapq


class Solution(object):
# 贪心法：
# 先把出现次数最多(p)的任务安排上。以n+1为一轮，安排p次任务需要的时间为 (p-1) * (n+1) + 1，
# 最后再加上其它出现次数为p的任务数目。还有特殊情况：次数少的任务很多在前面循环中安排不下，这时答案就是len(tasks)，
# 相当于移除每轮n+1中的idle时间，换为这些次数少的任务。len(tasks)等同于没有任何idle时间。
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = collections.Counter(tasks)
        _, max_count = counter.most_common(1)[0]

        result = (max_count-1) * (n+1)
        for count in counter.values():
            if count == max_count:
                result += 1
        return max(result, len(tasks))



# 填充法：按出现次数从多到少填入n+1每轮，用堆自动每次排序。总体慢很多。
    def leastInterval2(self, tasks, n):
        counter = collections.Counter(tasks)
        hq = []
        for _, cnt in counter.items():
            heapq.heappush(hq, -cnt)

        slots = 0
        while hq:
            tmp = []
            for i in range(n+1):   # 每轮只填充up to n+1个任务
                slots += 1
                if hq:
                    cnt = - heapq.heappop(hq)
                    if cnt > 1:
                        tmp.append(cnt-1)
                if not hq and not tmp:
                    break

            for cnt in tmp:
                heapq.heappush(hq, -cnt)

        return slots



print(Solution().leastInterval(["A","A","A","B","B","B"], 2)) # 8
print(Solution().leastInterval(["A","A","A","B","B","B"], 0)) # 6
print(Solution().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2)) # 16
print(Solution().leastInterval(["A","A","B","C","D","E"], 3)) # 6, use len(tasks) which > (2-1)*(3+1) + 1