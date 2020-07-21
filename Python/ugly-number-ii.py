# Time:  O(n)
# Space: O(n)

# 264
# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors
# only include 2, 3, 5. For example,
# 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the
# first 10 ugly numbers.
#
# Note that 1 is typically treated as an ugly number. n does not exceed 1690.
#
# Hint:
# 1. The naive approach is to call isUgly() for every number O(n).
# Most numbers are not ugly. Should limit to the ugly ones only.

# 2. An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.

# 3. The key is how to maintain the order of the ugly numbers. Idea: merging from 3 sorted lists.

import heapq

class Solution:
    # @param {integer} n
    # @return {integer}
    def nthUglyNumber(self, n): # USE THIS: heap to sort, set to filter duplicate
        seen = {1}
        heap = [1]
        for _ in range(n):
            ans = heapq.heappop(heap)
            for k in [2,3,5]:
                nxt = ans * k
                if nxt not in seen:
                    seen.add(nxt)
                    heapq.heappush(heap, nxt)
        return ans

    # this heap solution can filter duplicate but hard to get this idea.
    def nthUglyNumber_anotherHeap(self, n):
        ugly_number = 0
        heap = []
        heapq.heappush(heap, 1)
        for _ in range(n):
            ugly_number = heapq.heappop(heap)
            if ugly_number % 2 == 0:
                heapq.heappush(heap, ugly_number * 2)
            elif ugly_number % 3 == 0:
                heapq.heappush(heap, ugly_number * 2)
                heapq.heappush(heap, ugly_number * 3)
            else:
                heapq.heappush(heap, ugly_number * 2)
                heapq.heappush(heap, ugly_number * 3)
                heapq.heappush(heap, ugly_number * 5)

        return ugly_number

    # Dynamic programming Time O(n), Space(n)
    def nthUglyNumber2(self, n):  # THIS IS ALSO GOOD
        ans = [1]
        i2 = i3 = i5 = 0  # 指针指向丑数要乘以的因子
        for _ in range(n-1):
            a2, a3, a5 = ans[i2] * 2, ans[i3] * 3, ans[i5] * 5
            ans.append(min(a2, a3, a5))

            if a2 == ans[-1]: i2 += 1  # 丑数对应的因子指针往前走一步
            if a3 == ans[-1]: i3 += 1
            if a5 == ans[-1]: i5 += 1
        return ans[-1]

    def nthUglyNumber3(self, n):
        q2, q3, q5 = [2], [3], [5]
        ugly = 1
        for u in heapq.merge(q2, q3, q5):
            if n == 1:
                return ugly
            if u > ugly:
                ugly = u
                n -= 1
                q2 += 2 * u,
                q3 += 3 * u,
                q5 += 5 * u,


class Solution2:
    ugly = sorted(2**a * 3**b * 5**c
                  for a in range(32) for b in range(20) for c in range(14))

    def nthUglyNumber(self, n):
        return self.ugly[n-1]

print(Solution().nthUglyNumber(20))