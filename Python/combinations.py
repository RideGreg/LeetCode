# Time:  O(k * C(n, k))
# Space: O(k)

# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# For example,
# If n = 4 and k = 2, a solution is:
#
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n:
            return []
        nums, idxs = range(1, n+1), range(k)
        result = [[nums[i] for i in idxs]]
        while True:
            for i in reversed(xrange(k)):
                if idxs[i] != i+n-k:
                    break
            else:
                break
            idxs[i] += 1
            for j in xrange(i+1, k):
                idxs[j] = idxs[j-1] + 1
            result.append([nums[i] for i in idxs])
        return result


# Time:  O(k * C(n, k))
# Space: O(k)
class Solution2(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result, combination = [], []
        i = 1
        while True:
            if len(combination) == k:
                result.append(combination[:])
            if len(combination) == k or \
               len(combination)+(n-i+1) < k:
                if not combination:
                    break
                i = combination.pop()+1
            else:
                combination.append(i)
                i += 1
        return result


class Solution2(object):
    def combine_ming(self, n, k):  # USE THIS
        def dfs(start, cur, k, n):
            if len(cur) == k:
                ans.append(cur[:])
                return

            for i in xrange(start, n + 1 - (k - len(cur)) + 1):
            # this is optmization of: for i in xrange(start, n + 1):
                cur.append(i)
                dfs(i + 1, cur, k, n)
                cur.pop()

        ans = []
        dfs(1, [], k, n)
        return ans


if __name__ == "__main__":
    result = Solution().combine(4, 2)
    print result
