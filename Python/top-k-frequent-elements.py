# Time:  O(n)
# Space: O(n)

# 347
# Given a non-empty array of integers,
# return the k most frequent elements.
#
# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].
#
# Note:
# You may assume k is always valid,
# 1 <= k <= number of unique elements.
# Your algorithm's time complexity must be better
# than O(n log n), where n is the array's size.

# REQUIRE NOT TO DO FULLY SORTING

# Bucket Sort Solution

import collections

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = collections.Counter(nums)
        buckets = [[] for _ in xrange(len(nums)+1)]
        for i, count in counts.iteritems():
            buckets[count].append(i)

        result = []
        for count in reversed(xrange(len(buckets))):
            for n in buckets[count]:
                result.append(n)
                if len(result) == k:
                    return result
        return result


# Time:  O(n) ~ O(n^2), O(n) on average.
# Space: O(n)
# Quick Select Solution
# if ask top k large nums, it is simply kthElement()
# now ask top k frequent, must get and sort by frequency, then apply kthElement()
import random
class Solution2(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        def kthElement(A, k):
            def partition(l, r, pivot):
                new_pivot = l
                A[pivot], A[r] = A[r], A[pivot]
                for i in range(l, r):
                    if A[i] < A[r]:
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

        counts = collections.Counter(nums)
        pairs = []
        for n, count in counts.items():
            pairs.append((-count, n))
        kthElement(pairs, k)
        return [x[1] for x in pairs[:k]]

# Time:  O(nlogk)
# Space: O(n)
class Solution3(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return [key for key, _ in collections.Counter(nums).most_common(k)]

# Heap solution
# If k = 1 the linear-time solution is quite simple. One could keep the frequency of elements appearance
# in a hash map and update the maximum element at each step.
#
# When k > 1 we need a data structure that has a fast access to the elements ordered by their frequencies.
# The idea here is to use the heap which is also known as priority queue.