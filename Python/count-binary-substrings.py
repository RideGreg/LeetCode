# Time:  O(n)
# Space: O(1)

# Give a string s, count the number of non-empty (contiguous) substrings
# that have the same number of 0's and 1's, and all the 0's and all the 1's
# in these substrings are grouped consecutively.
#
# Substrings that occur multiple times are counted the number of times they occur.
#
# Example 1:
# Input: "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's:
#              "0011", "01", "1100", "10", "0011", and "01".
#
# Notice that some of these substrings repeat and are counted the number of times they occur.
#
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
# Example 2:
# Input: "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
#       
# Note:
# s.length will be between 1 and 50,000.
# s will only consist of "0" or "1" characters.

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        prev, curr = 0, 1 #for the first char case
        for i in xrange(1, len(s)):
            #each time alternating, add #of candidates from substring ending with last char
            if s[i-1] != s[i]:
                result += min(prev, curr)
                prev, curr = curr, 1
            else:
                curr += 1
        result += min(prev, curr)
        return result

    # return a list of counts of groups of 0 or 1
    def countBinarySubstrings2(self, s):
        result = []
        curr = 1
        for i in xrange(1, len(s)):
            if s[i] == s[i-1]:
                curr += 1
            else:
                result.append(curr)
                curr = 1
        result.append(curr)
        return result

    # Time O(n^2)
    def countBinarySubstrings3(self, s):
        res = 0
        for i in xrange(len(s) - 1):
            num0, num1 = 0, 0
            if s[i] == '0':
                num0 += 1
            else:
                num1 += 1
            j = i + 1
            while j < len(s):
                if num0 and num1 and s[j] != s[j-1]: #aba pattern
                    break
                if s[j] == '0':
                    num0 += 1
                else:
                    num1 += 1
                if num0 == num1: #for all substrings starting w/ s[i], zero or one result
                    res += 1
                    break
                j += 1
        return res

print Solution().countBinarySubstrings2('00110')
print Solution().countBinarySubstrings2('00110011')
print Solution().countBinarySubstrings2('10101')
