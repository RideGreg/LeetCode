# Time:  O(a + b)
# Space: O(1)

# 984
# Given two integers A and B, return any string S such that:
#
# S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
# The substring 'aaa' does not occur in S;
# The substring 'bbb' does not occur in S.

# Input: A = 4, B = 1
# Output: "aabaa"

class Solution(object):
    # greedy
    # Intuitively, we should write the most common letter first. For example, if we have A = 6, B = 2, 
    # we want to write 'aabaabaa'. The only time we don't write the most common letter is 
    # if the last two letters we have written are also the most common letter
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        result = []
        while A or B:
            if len(result) >= 2 and result[-1] == result[-2]:
                writeA = result[-1] == 'b'
            else:
                writeA = A >= B

            if writeA:
                A -= 1
                result.append('a')
            else:
                B -= 1
                result.append('b')
        return "".join(result)

    # stars and bars construction
    # suppose we write the most common char in a string, use less common char as bar to divide
    # the string every 2 most common chars. End of string needs special handling.
    def strWithout3a3b(self, A, B):
        if A >= B:
            aChar, bChar = 'a', 'b'
        else:
            aChar, bChar = 'b', 'a'
            A, B = B, A

        bars = (A + 1) / 2
        doubleB = B - bars
        ans = []
        for i in xrange(bars - 1):
            ans.append(aChar * 2)
            A -= 2
            ans.append(bChar * 2 if i < doubleB else bChar)
            B -= 2 if i < doubleB else 1

        ans.append(aChar * A + bChar * B) # A may be 1 or 2, B may be 0, 1 or 2
        return ''.join(ans)