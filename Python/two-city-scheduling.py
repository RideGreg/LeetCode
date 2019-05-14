# Time:  O(n) ~ O(n^2), O(n) on average.
# Space: O(1)

# 1029
# There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0],
# :and the cost of flying the i-th person to city B is costs[i][1].
#
# Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.
#
#
# Input: [[10,20],[30,200],[400,50],[30,20]]
# Output: 110

import random


# quick select solution
# we do not need to perfectly sort all cost differences, we just need the biggest savings
# (to fly to A) to be in the first half of the array. So, we can use the quick select algorithm
# (nth_element in C++) and use the middle of the array as a pivot.
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        def kthElement(A, k):
            def partition(l, r, pivot):
                new_pivot = l
                A[pivot], A[r] = A[r], A[pivot]
                for i in range(l, r):
                    if compare(A[i], A[r]):  # compare func can be hardcoded here
                        A[i], A[new_pivot] = A[new_pivot], A[i]
                        new_pivot += 1

                A[new_pivot], A[r] = A[r], A[new_pivot]
                return new_pivot

            l, r = 0, len(A) - 1
            while l <= r:
                pivot = random.randint(l, r)
                new_pivot = partition(l, r, pivot)
                if new_pivot == k - 1:
                    return
                elif new_pivot > k - 1:
                    r = new_pivot - 1
                else:
                    l = new_pivot + 1

        k = len(costs) // 2
        compare = lambda a, b: a[0] - a[1] < b[0] - b[1]
        kthElement(costs, k)  # O(n) on average
        return sum(x[0] for x in costs[:k]) + sum(x[1] for x in costs[k:])


    def twoCitySchedCost_sort(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[0]-x[1])  # less a is at front
        N = len(costs) // 2
        return sum(a for a, b in costs[:N]) + sum(b for a, b in costs[N:])

    # get the sum if all go to city A, then change half to go to city B based on cost savings
    # require extra space
    def twoCitySchedCost_delta(self, costs: List[List[int]]) -> int:
        delta = [b-a for a, b in costs]
        delta.sort()
        return sum(a for a, b in costs) + sum(delta[:len(costs)//2])

    # DP: time O(n^2), space O(n^2)
    # dp[i][j] is total i people, among them j people go to city B
    # 0
    # 1A 1B
    # 2A 1A1B 2B
    # 3A 2A1B 1A2B 3B
    # 4A 3A1B 2A2B 1A3B 4B
    def twoCitySchedCost_dp(self, costs: List[List[int]]) -> int:
        N = len(costs)
        dp = [[float('inf')] * (N+1) for _ in range(N+1)]
        dp[0][0] = 0
        for i in range(1, N+1):
            for j in range(i+1):
                if j < i:
                    dp[i][j] = min(dp[i][j], dp[i-1][j]+costs[i-1][0])
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1]+costs[i-1][1])
        return dp[N][N//2]

    # absolutely no need for 2 arrays, because they are just reversed.
    # actually a bug when 2 arrays (a-b, b-a) sort separately:
    # suppose #N-1 and #N is (115, 70) and (231, 186), their differences are same 45, and sorting
    # separately selects 115+231 (or 70+186). Should either 115+186 or 70+231.
    def twoCitySchedCost_wrong_2arrays(self, costs):
        import heapq
        N = len(costs)
        order1, order2 = [], []
        for a,b in costs:
            heapq.heappush(order1, (b-a, a))
            if len(order1) > N//2:
                heapq.heappop(order1)
            heapq.heappush(order2, (a-b, b))
            if len(order2) > N//2:
                heapq.heappop(order2)
        return sum(o[1] for o in order1+order2)
