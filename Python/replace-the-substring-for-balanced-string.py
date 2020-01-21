# Time:  O(n)
# Space: O(1)

# 1234 weekly contest 159 10/19/2019

# You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.
#
# A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.
#
# Return the minimum length of the substring that can be replaced with any other string of the same length
# to make the original string s balanced. Return 0 if the string is already balanced.

# 1 <= s.length <= 10^5
# s.length is a multiple of 4. s contains only 'Q', 'W', 'E' and 'R'.

import collections


class Solution(object):
    def balancedString(self, s): # USE THIS
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        ans = len(s)
        left = 0
        for right in range(len(s)):
            count[s[right]] -= 1
            while left < len(s) and all(v <= len(s)//4 for v in count.values()): # while, not if
                ans = min(ans, right-left+1)
                if ans == 0: return ans
                count[s[left]] += 1
                left += 1
        return ans

    # O(nlogn) Binary Search
    def balancedString_ming(self, s: str) -> int:
        def ok(length):
            for i in range(sz+1-length):
                # char counts of substring s[i:i+length+1], faster using pre-computed counts
                delta = [a-b for a,b in zip(char_counts[i+length], char_counts[i])]
                # cover all which need replacement
                if all(a-b >= 0 for a,b in zip(delta, to_replace)):
                    return True
            return False

        char_counts = [[0,0,0,0]]
        for c in s:
            q,w,e,r = char_counts[-1]
            if c == 'Q': q += 1
            elif c == 'W': w += 1
            elif c == 'E': e += 1
            else: r += 1
            char_counts.append([q,w,e,r])
            ''' KENG: all items in list points to the same memory
            char_counts.append(char_counts[-1])
            char_counts[-1][pos[c]] += 1
            '''

        sz = len(s)
        to_replace = [max(0, x - sz//4) for x in char_counts[-1]]
        hi, lo = sz, sum(to_replace)

        if lo <= 1: return lo # no need to consider whether all to_replace is in a substring
        while lo < hi:
            mi = (lo+hi) // 2
            if ok(mi):
                hi = mi
            else:
                lo = mi + 1
        return lo

print(Solution().balancedString("QWER")) # 0
print(Solution().balancedString("QQWE")) # 1
print(Solution().balancedString("QQQW")) # 2
print(Solution().balancedString("QQQQ")) # 3
print(Solution().balancedString("QQQQWQQQ")) # 6 QxxxxxxQ
print(Solution().balancedString("QQQQWQRQ")) # 4 xxxxWQRQ
