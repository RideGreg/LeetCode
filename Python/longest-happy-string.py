# Time:  O(n)
# Space: O(1)

# 1405
# A string s is called happy if it satisfies the following conditions:
#
# s only contains the letters 'a', 'b', and 'c'.
# s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# s contains at most a occurrences of the letter 'a'.
# s contains at most b occurrences of the letter 'b'.
# s contains at most c occurrences of the letter 'c'.
# Given three integers a, b, and c, return the longest possible happy string.
# If there are multiple longest happy strings, return any of them. If there is
# no such string, return the empty string "".
#
# A substring is a contiguous sequence of characters within a string.

import heapq
from math import gcd

class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        max_heap = []
        if a:
            heapq.heappush(max_heap, (-a, 'a'))
        if b:
            heapq.heappush(max_heap, (-b, 'b'))
        if c:
            heapq.heappush(max_heap, (-c, 'c'))
        result = []
        while max_heap:
            count1, c1 = heapq.heappop(max_heap)
            if len(result) >= 2 and result[-1] == result[-2] == c1:  # need different char
                if not max_heap:  # no other chars, return
                    return "".join(result)
                count2, c2 = heapq.heappop(max_heap)
                result.append(c2)
                count2 += 1
                if count2:
                    heapq.heappush(max_heap, (count2, c2))
                heapq.heappush(max_heap, (count1, c1))
                continue

            # directly add the most char
            result.append(c1)
            count1 += 1
            if count1 != 0:
                heapq.heappush(max_heap, (count1, c1))
        return "".join(result)


# Time:  O(n)
# Space: O(1)
class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        choices = [[a, 'a'], [b, 'b'], [c, 'c']]
        result = []
        for _ in range(a+b+c):
            choices.sort(reverse=True)  # 每次重新洗牌
            for i, (x, c) in enumerate(choices):
                if x and result[-2:] != [c, c]:
                    result.append(c)
                    choices[i][0] -= 1
                    break
            else:
                break
        return "".join(result)

print(Solution().longestDiverseString(1, 1, 7))  # "ccaccbcc"
print(Solution().longestDiverseString(7, 1, 0))  # "aabaa"