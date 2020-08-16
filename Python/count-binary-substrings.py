# Time:  O(n)
# Space: O(1)

# 696
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
        s += '#' # add the last alternating char
        result = 0
        prev, curr = 0, 1 #for the first char case
        for i in range(1, len(s)):
            #each time alternating, add # of eligible substrings
            if s[i-1] != s[i]:
                result += min(prev, curr)
                prev, curr = curr, 1
            else:
                curr += 1
        return result

    # Time O(n) Space O(n)
    def countBinarySubstrings2(self, s):
        # build an array of continuous digits until this index
        cnt = [1]
        for i in range(1, len(s)):
            cnt.append(cnt[-1] + 1 if s[i] == s[i-1] else 1)
        # iterate the array to check if eligible substring exists at this index
        ans = 0
        for i, v in enumerate(cnt):
            if i >= v and cnt[i-v] >= v:
                ans += 1
        return ans


print(Solution().countBinarySubstrings('00110')) # 3
print(Solution().countBinarySubstrings('00110011')) # 6
print(Solution().countBinarySubstrings('10101')) # 4
