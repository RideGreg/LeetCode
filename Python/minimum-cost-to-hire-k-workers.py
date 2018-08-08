# Time:   O(nlogn)
# Space : O(n)

# There are N workers.
# The i-th worker has a quality[i] and a minimum wage expectation wage[i].
#
# Now we want to hire exactly K workers to form a paid group.
# When hiring a group of K workers, we must pay them according to
# the following rules:
#
# Every worker in the paid group should be paid in the ratio of
# their quality compared to other workers in the paid group.
# Every worker in the paid group must be paid at least their minimum wage
# expectation.
# Return the least amount of money needed to form a paid group satisfying
# the above conditions.
#
# Example 1:
#
# Input: quality = [10,20,5], wage = [70,50,30], K = 2
# Output: 105.00000
# Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
# Example 2:
#
# Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
# Output: 30.66667
# Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers
# seperately.
#
# Note:
# - 1 <= K <= N <= 10000, where N = quality.length = wage.length
# - 1 <= quality[i] <= 10000
# - 1 <= wage[i] <= 10000
# - Answers within 10^-5 of the correct answer will be considered correct.

import itertools
import heapq


class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float

        Every worker has some minimum ratio of "dollars to quality" that they demand. The key insight is to iterate over
        the ratio. For a given ratio R, we know the workers hired all have a ratio R or lower. Then, we want to keep
        the K workers with lowest quality. Use a heap to remove K+1-th workers in terms of high quality.
        """
        workers = [[float(w)/q, q] for w, q in itertools.izip(wage, quality)]
        # default sorting by 1st element, then 2nd element and so on. We need sorting by ratio then quality.
        workers.sort()

        max_heap = [-q for r, q in workers[:K]]
        qsum = -sum(max_heap)
        result = qsum * workers[K - 1][0]
        heapq.heapify(max_heap)
        for r, q in workers[K:]:
            z = - heapq.heappushpop(max_heap, -q)
            if z != q:
                qsum += q - z
                result = min(result, qsum*r)
        return result

    def mincostToHireWorkers_buteForceGreedy(self, quality, wage, K): # TLE
        '''
        Time O(n*nlogn), space O(n)

        Intuition
        At least one worker will be paid their minimum wage expectation. If not, we could scale all payments down
        and still keep everyone earning more than their wage expectation.

        Algorithm
        Loop all workers, take each as captain that will be paid their minimum wage expectation, calculate the cost of
        hiring K workers where each point of quality is worth wage[captain] / quality[captain] dollars.
        '''
        ans = float('inf')
        for i in xrange(len(wage)):
            factor = 1.0 * wage[i] / quality[i]
            prices = []
            for j in xrange(len(wage)):
                price = factor * quality[j]
                if price >= wage[j]:
                    prices.append(price)

            if len(prices) >= K:
                prices.sort()
                ans = min(ans, sum(prices[:K]))
        return ans
