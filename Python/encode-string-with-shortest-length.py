# Time:  O(n^3) on average
# Space: O(n^2)

# 471
# Given a non-empty string, encode the string such that its encoded length is the shortest.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets
# is being repeated exactly k times.
#
# Note:
# 1. k will be a positive integer and encoded string will not be empty or have extra space.
# 2. You may assume that the input string contains only lowercase English letters. The string's
# length is at most 160.
# 3. If an encoding process does not make the string shorter, then do not encode it. If there
# are several solutions, return any of them is fine.

class Solution(object):
    def encode(self, s): # USE THIS
        """
        :type s: str
        :rtype: str
        """
        # 所有子串都会送进这个function，任何有循环节的子串都会被压缩编码
        def encode_substr(i, j):
            temp = s[i:j+1]
            pos = (temp + temp).find(temp, 1)  # O(n) on average
            if pos >= len(temp):
                return temp
            return str(len(temp)//pos) + '[' + dp[i][i + pos - 1] + ']'

        dp = [[""] * len(s) for _ in range(len(s))]
        for length in range(1, len(s)+1):
            for i in range(len(s)+1-length):
                j = i+length-1
                dp[i][j] = s[i:j+1]
                for k in range(i, j):
                    if len(dp[i][k]) + len(dp[k+1][j]) < len(dp[i][j]):
                        dp[i][j] = dp[i][k] + dp[k+1][j]
                encoded_string = encode_substr(i, j)
                if len(encoded_string) < len(dp[i][j]):
                    dp[i][j] = encoded_string
        return dp[0][len(s) - 1]

# 利用字典dp记录字符串的最优编码串
# 枚举分隔点p， 将字符串拆解为left, right左右两部分
# 尝试将left调用solve函数进行编码压缩，并对right递归调用encode函数进行搜索
# 将left和right组合的最短字符串返回，并更新dp
class Solution_bookshadow(object):
    def __init__(self):
        self.dp = dict()

    def encode(self, s):
        """
        :type s: str
        :rtype: str
        """
        size = len(s)
        if size <= 1: return s
        if s in self.dp: return self.dp[s]
        ans = s
        for p in range(1, size + 1):
            left, right = s[:p], s[p:]
            t = self.solve(left) + self.encode(right)
            if len(t) < len(ans): ans = t
        self.dp[s] = ans
        return ans

    def solve(self, s):
        ans = s
        size = len(s)
        for x in range(1, size / 2 + 1):
            if size % x or s[:x] * (size / x) != s: continue
            y = str(size / x) + '[' + self.encode(s[:x]) + ']'
            if len(y) < len(ans): ans = y
        return ans

print(Solution().encode("aaa")) # "aaa"
print(Solution().encode("aaaaa")) # "5[a]"
print(Solution().encode("aaaaaaaaaa")) # "10[a]", "a9[a]" or "9[a]a"
print(Solution().encode("aabcaabcd")) # "2[aabc]d"
print(Solution().encode("abbbabbbcabbbabbbc")) # "2[2[abbb]c]"

