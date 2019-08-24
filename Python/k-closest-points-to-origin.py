# Time:  O(n) on average
# Space: O(1)

# 973
# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
# (Here, the distance between two points on a plane is the Euclidean distance.)
#
# You may return the answer in any order.  The answer is guaranteed to be unique (except for
# the order that it is in.)


# Solution 1: quick select
# We want an algorithm faster than NlogN. Clearly, the only way to do this is to use the fact that
# the K elements returned can be in any order -- otherwise we would be sorting which is at least NlogN.
#
# Say we choose some random element x = A[i] and split the array into two buckets: one bucket of all
# the elements less than x, and another bucket of all the elements greater than or equal to x.
# This is known as "quickselecting by a pivot x".
#
# The idea is that if we quickselect by some pivot, on average in linear time we'll reduce the problem
# to a problem of half the size.
#
# Algorithm
# Let's do the work(i, j, K) of partially sorting the subarray (points[i], points[i+1], ..., points[j])
# so that the smallest K elements of this subarray occur in the first K positions (i, i+1, ..., i+K-1).
#
# First, we quickselect by a random pivot element from the subarray. To do this in place, we have two pointers
# i and j, and move these pointers to the elements that are in the wrong bucket -- then, we swap these elements.
#
# After, we have two buckets [oi, i] and [i+1, oj], where (oi, oj) are the original (i, j) values when
# calling work(i, j, K). Say the first bucket has 10 items and the second bucket has 15 items. If we were
# trying to partially sort say, K = 5 items, then we only need to partially sort the first bucket: work(oi, i, 5).
# Otherwise, if we were trying to partially sort say, K = 17 items, then the first 10 items are already
# partially sorted, and we only need to partially sort the next 7 items: work(i+1, oj, 7).

from random import randint


class Solution(object):
    def kClosest(self, points, K): # recursion, leetcodeOfficial: 1400 ms
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        dist = lambda i: points[i][0]**2 + points[i][1]**2

        def sort(i, j, K):
            # Partially sorts A[i:j+1] so the first K elements are
            # the smallest K elements.
            if i >= j: return

            # Put random element as A[i] - this is the pivot
            k = randint(i, j)
            points[i], points[k] = points[k], points[i]

            mid = partition(i, j)
            if K < mid - i + 1:
                sort(i, mid - 1, K)
            elif K > mid - i + 1:
                sort(mid + 1, j, K - (mid - i + 1))

        def partition(i, j):
            # Partition by pivot A[i], returning an index mid
            # such that A[i] <= A[mid] <= A[j] for i < mid < j.
            oi = i
            pivot = dist(i)
            i += 1

            while True:
                while i < j and dist(i) < pivot:
                    i += 1
                while i <= j and dist(j) >= pivot:
                    j -= 1
                if i >= j: break
                points[i], points[j] = points[j], points[i]

            points[oi], points[j] = points[j], points[oi] # points[j] always < pivot dist, so swap to the beginning
            return j

        sort(0, len(points) - 1, K)
        return points[:K]

    def kClosest_iteration(self, points, K):
        def dist(point):
            return point[0]**2 + point[1]**2
        
        def kthElement(k, compare):
            def PartitionAroundPivot(left, right, pivot_idx, compare):
                new_pivot_idx = left
                points[pivot_idx], points[right] = points[right], points[pivot_idx]
                for i in xrange(left, right):
                    if compare(points[i], points[right]):
                        points[i], points[new_pivot_idx] = points[new_pivot_idx], points[i]
                        new_pivot_idx += 1

                points[right], points[new_pivot_idx] = points[new_pivot_idx], points[right]
                return new_pivot_idx

            left, right = 0, len(points) - 1
            while left <= right:
                pivot_idx = randint(left, right)
                new_pivot_idx = PartitionAroundPivot(left, right, pivot_idx, compare)
                if new_pivot_idx == k:
                    return
                elif new_pivot_idx > k:
                    right = new_pivot_idx - 1
                else:  # new_pivot_idx < k.
                    left = new_pivot_idx + 1
                    
        kthElement(K, lambda a, b: dist(a) < dist(b))
        return points[:K]


# Time:  O(nlogk)
# Space: O(k)
import heapq


class Solution2(object): # USE THIS 400 ms
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        def dist(point):
            return point[0]**2 + point[1]**2
        
        max_heap = []
        for point in points:
            heapq.heappush(max_heap, (-dist(point), point))
            if len(max_heap) > K:
                heapq.heappop(max_heap)
        return [x[1] for x in max_heap]


# Time:  O(nlogn)
# Space: O(1)
class Solution3(object):
    def kClosest(self, points, K):
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        return points[:K]
