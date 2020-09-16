# Time:  O(n^2 ~ 2^n)
# Space: O(n^2)
# 131
# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# For example, given s = "aab",
# Return
#
#   [
#     ["aa","b"],
#     ["a","a","b"]
#   ]



# Time:  O(2^n)
# Space: O(n)
# backtracking solution
class Solution(object):   # USE THIS: backtracking + memorization
    def partition(self, s):
        n = len(s)
        lookup = [[False] * n for _ in xrange(n)]
        for i in reversed(range(n)):
            for j in range(i, n):
                lookup[i][j] = (s[i] == s[j] and (j - i < 2 or lookup[i + 1][j - 1]))

        def backtrack(start, cur):
            if start == len(s):
                ans.append(cur)
                return

            for j in range(start, len(s)):
                if lookup[start][j]:
                    backtrack(j + 1, cur + [s[start:j + 1]])

        ans = []
        backtrack(0, [])
        return ans


class Solution2:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        result = []
        self.backtrack(result, [], s, 0)
        return result

    def backtrack(self, result, cur, s, i):
        if i == len(s):
            result.append(list(cur))
        else:
            for j in xrange(i, len(s)):
                if self.isPalindrome(s[i: j + 1]):
                    cur.append(s[i: j + 1])
                    self.backtrack(result, cur, s, j + 1)
                    cur.pop()

    def isPalindrome(self, s):
        return all(s[i] != s[-(i + 1)] for i in xrange(len(s) // 2))


# Time:  O(n^2 ~ 2^n)
# Space: O(n^2)
# dynamic programming solution, hard to remember
class Solution3:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        n = len(s)

        is_palindrome = [[0 for j in xrange(n)] for i in xrange(n)]
        for i in reversed(xrange(n)):
            for j in xrange(i, n):
                is_palindrome[i][j] = s[i] == s[j] and ((j - i < 2 ) or is_palindrome[i + 1][j - 1])

        sub_partition = [[] for i in xrange(n)]
        for i in reversed(xrange(n)):
            for j in xrange(i, n):
                if is_palindrome[i][j]:
                    if j + 1 < n:
                        for p in sub_partition[j + 1]:
                            sub_partition[i].append([s[i:j + 1]] + p)
                    else:
                        sub_partition[i].append([s[i:j + 1]])

        return sub_partition[0]



if __name__ == "__main__":
    print Solution().partition("aab") # [["a","a","b"],["aa","b"]]
