# Time:  O(n + klogk) on average, quick select O(n), output sort klogk
# Space: O(n)

# 692
# Given a non-empty list of words, return the k most frequent elements.
#
# Your answer should be sorted by frequency from highest to lowest.
# If two words have the same frequency, then the word with the lower alphabetical order comes first.
#
# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
#     with the number of occurrence being 4, 3, 2 and 1 respectively.
# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
#
# Follow up:
# Try to solve it in O(n log k) time and O(n) extra space.
# Can you solve it in O(n) time with only O(k) extra space?

# Quick Select Solution

import collections
import heapq
from random import randint


class Solution(object):
    def topKFrequent(self, words, k):  # USE THIS: Quick Select is best solution
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        def kthElement(A, k):
            import random
            def partition(l, r): # O(n) on average
                pivot = random.randint(l, r)
                A[pivot], A[r] = A[r], A[pivot]

                ans = l
                for i in range(l, r):
                    if A[i] < A[r]:
                        A[i], A[ans] = A[ans], A[i]
                        ans += 1
                A[ans], A[r] = A[r], A[ans]
                return ans

            l, r = 0, len(A)-1
            while l < r:
                new_pivot = partition(l, r)
                if new_pivot == k:
                    return
                elif new_pivot > k:
                    r = new_pivot - 1
                else:
                    l = new_pivot + 1
            return

        counts = collections.Counter(words)
        pairs = [(-c, w) for w, c in counts.items()]
        kthElement(pairs, k-1)
        return [x[1] for x in sorted(pairs[:k])]

# Time:  O(nlogk)
# Space: O(n)
# Heap Solution: need to build HeapObj
class Solution2(object):
    # O(n + klogn) heap contains all words, pop k times
    def topKFrequent(self, words, k): # VERY GOOD TOO
        counts = collections.Counter(words)          # O(n)
        heap = [(-c, w) for w, c in counts.items()]  # O(n)
        heapq.heapify(heap)                          # O(n)
        return [heapq.heappop(heap)[1] for _ in range(k)]  # O(klogn)

    # O(nlogk) keep k items in heap, need to write Comparator to pop "alphabetical larger word" from minHeap
    def topKFrequent2(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        class MinHeapObj(object):
            def __init__(self,val):
                self.val = val
            def __lt__(self,other):
                return self.val[1] > other.val[1] if self.val[0] == other.val[0] else \
                       self.val < other.val
            # the following can be removed
            '''
            def __eq__(self,other):
                return self.val == other.val
            def __str__(self):
                return str(self.val)
            '''

        counts = collections.Counter(words)
        min_heap = []
        for word, count in counts.items():
            heapq.heappush(min_heap, MinHeapObj((count, word)))
            if len(min_heap) == k+1:
                heapq.heappop(min_heap)
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap).val[1])
        return result[::-1]


# Time:  O(n + klogk) ~ O(n + nlogn)
# Space: O(n)
# Bucket Sort Solution
class Solution3(object):
    def topKFrequent_ming(self, words, k):
        import bisect
        counts = collections.Counter(words)
        N = len(words)
        buckets = [[] for _ in range(N + 1)]
        for w, c in counts.items():
            bisect.insort(buckets[c], w)   # sort takes extra time on top of O(n)

        ans = []
        for count in reversed(range(len(buckets))):
            for w in buckets[count]:
                ans.append(w)
                if len(ans) == k:
                    return ans


    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counts = collections.Counter(words)
        buckets = [[] for _ in range(len(words)+1)]
        for word, count in counts.items():
            buckets[count].append(word)
        pairs = []
        for i in reversed(range(len(buckets))):
            for word in buckets[i]:
                pairs.append((-i, word))
            if len(pairs) >= k:
                break
        pairs.sort()
        return [pair[1] for pair in pairs[:k]]


# time: O(nlogn)
# space: O(n)
# Full Sort
from collections import Counter


class Solution4(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter = Counter(words)
        candidates = counter.keys()
        candidates.sort(key=lambda w: (-counter[w], w))
        return candidates[:k]
