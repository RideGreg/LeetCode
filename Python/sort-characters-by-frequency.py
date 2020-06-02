# Time:  O(n)
# Space: O(n)

# 451
# Given a string, sort it in decreasing order based on the frequency of characters.

# Input:
# "tree"
#
# Output:
# "eert"
#
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:
#
# Input:
# "cccaaa"
#
# Output:
# "cccaaa"
#
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:
#
# Input:
# "Aabb"
#
# Output:
# "bbAa"
#
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

import collections


class Solution(object):
    # Counter
    def frequencySort(self, s: str) -> str: # USE THIS
        """
        :type s: str
        :rtype: str
        """
        return ''.join([c * count for c, count in collections.Counter(s).most_common()])
        """OR
        cnt = collections.Counter(s)
        ans = []
        for c in sorted(cnt, key=cnt.get, reverse=True):
            ans.extend(c * cnt[c])
        return ''.join(ans)"""

    # bucket sort O(n)
    def frequencySort_bucket(self, s):
        freq = collections.Counter(s)

        buckets = [""] * (len(s)+1)
        for c in freq:
            buckets[freq[c]] += c
        # print(buckets) #['', 'Aa', 'b', '', '']

        ans = ""
        for count in reversed(range(len(buckets)-1)):
            for c in buckets[count]:
                ans += c * count
        return ans


    # max heap: not good, heap takes O(n) space
    def frequencySort_heap(self, s: str) -> str:
        import heapq
        countFrequency = collections.Counter(s)

        lst = []
        heapq.heapify(lst)
        for c in countFrequency:
            for _ in range(countFrequency[c]):
                heapq.heappush(lst, (-countFrequency[c], c))

        return ''.join([heapq.heappop(lst)[1] for _ in range(len(s))])


print(Solution().frequencySort_counter("Aabb")) # "bbAa"