# Time:  O(n * l)
# Space: O(1)

# 1002
# Given an array A of strings made only from lowercase letters, return a list of all characters
# that show up in all strings within the list (including duplicates).  For example, if a character occurs
# 3 times in all strings but not 4 times, you need to include that character three times in the final answer.
#
# You may return the answer in any order.

# learn Counter usage

import collections
from functools import reduce

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        result = collections.Counter(A[0])
        for a in A:
            result &= collections.Counter(a) # Counter intersection (dict doesn't support)
        return list(result.elements())       # Counter.elements() NOTE: convert iterator to list!!
        # Return an iterator over elements repeating each as many times as its count.

    # one line solution
    def commonChars_oneLine(self, A):
        return list(reduce(collections.Counter.__and__, map(collections.Counter, A)).elements())

    def commonChars_ming(self, A): # don't know to use Counter & and Counter.elements()
        c1 = collections.Counter(A[0])
        for a in A[1:]:
            c2 = collections.Counter(a)
            for k in c1:
                c1[k] = min(c1[k], c2[k])
        ans = []
        for k,v in c1.items():
            ans.extend([k]*v)
        return ans

print(Solution().commonChars(["bella","label","roller"])) # ["e","l","l"]
