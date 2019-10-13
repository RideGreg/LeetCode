# Time:  O(n)
# Space: O(1)

# 1208
# You are given two strings s and t of the same length. You want to change s to t. Changing the i-th character of s to
# i-th character of t costs |s[i] - t[i]| that is, the absolute difference between the ASCII values of the characters.
#
# You are also given an integer maxCost.
#
# Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of
# twith a cost less than or equal to maxCost.
#
# If there is no substring from s that can be changed to its corresponding substring from t, return 0.

# 1 <= s.length, t.length <= 10^5
# 0 <= maxCost <= 10^6
# s and t only contain lower case English letters.

class Solution(object):
    def equalSubstring(self, S, T, maxCost): # USE THIS awice
        N = len(S)
        A = [abs(ord(S[i]) - ord(T[i])) for i in xrange(N)]
        left = 0
        windowsum = 0
        ans = 0
        for right, x in enumerate(A):
            windowsum += x
            while windowsum > maxCost and left < N:
                windowsum -= A[left]
                left += 1
            cand = right - left + 1
            if cand > ans: ans = cand
        return ans

    def equalSubstring_ming(self, s, t, maxCost):
        psum = [0]
        for i in range(len(s)):
            psum.append(psum[-1] + abs(ord(s[i])-ord(t[i])))
        b, e, ans = 0, 0, 0
        while b <= len(s):
            while e+1 <= len(s) and psum[e+1]-psum[b] <= maxCost:
                e += 1
            ans = max(ans, e-b)
            b += 1
        return ans

    def equalSubstring_kamyu(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        left = 0
        for right in xrange(len(s)):
            maxCost -= abs(ord(s[right])-ord(t[right]))
            if maxCost < 0:
                maxCost += abs(ord(s[left])-ord(t[left]))
                left += 1
        return (right+1)-left

print(Solution().equalSubstring("abcd", "bcdf", 3))
print(Solution().equalSubstring("abcd", "cdef", 3))
print(Solution().equalSubstring("abcd", "acde", 0))
