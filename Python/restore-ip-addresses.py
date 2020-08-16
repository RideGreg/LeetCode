# Time:  O(n^m) = O(3^4)
# Space: O(n * m) = O(3 * 4)
# 93
# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# For example:
# Given "25525511135",
#
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
#

class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):  # USE THIS: maintain array then join is better than maintian a str
        def dfs(start, cur, parts):
            if start == len(s) or parts == 4:
                if start == len(s) and parts == 4:
                    ans.append('.'.join(cur))
                return

            for i in range(start, len(s)):
                p = s[start:i+1]
                if int(p) > 255 or (s[start] == '0' and i > start):
                    return
                cur.append(p)
                dfs(i+1, cur, parts+1)
                cur.pop()

        ans = []
        dfs(0, [], 0)
        return ans


    def restoreIpAddresses_kamyu(self, s):
        result = []
        self.restoreIpAddressesRecur(result, s, 0, "", 0)
        return result

    def restoreIpAddressesRecur(self, result, s, start, current, dots):
        # pruning to improve performance
        if (4 - dots) * 3 < len(s) - start or (4 - dots) > len(s) - start:
            return

        if start == len(s) and dots == 4:
            result.append(current[:-1])
        else:
            for i in xrange(start, start + 3):
                if len(s) > i and self.isValid(s[start:i + 1]):
                    current += s[start:i + 1] + '.'
                    self.restoreIpAddressesRecur(result, s, i + 1, current, dots + 1)
                    current = current[:-(i - start + 2)]

    def isValid(self, s):
        if len(s) == 0 or (s[0] == '0' and s != "0"):
            return False
        return int(s) < 256

if __name__ == "__main__":
    print Solution().restoreIpAddresses("0000")
