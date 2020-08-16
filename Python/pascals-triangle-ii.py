# Time:  O(n^2)
# Space: O(1)

# Given an index k, return the kth row of the Pascal's triangle.
#
# For example, given k = 3,
# Return [1,3,3,1].
#
#    1
#   1 1
#  1 2 1
# 1 3 3 1
# Note:
# Could you optimize your algorithm to use only O(k) extra space?
#

class Solution:
    # each iteration we have 1 more column
    # keep 1st column, accumulate middle columns, add last column
    def getRow(self, rowIndex):    # USE THIS, in place change doesn't need extra space
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = [1]
        for _ in range(rowIndex):
            for i in reversed(range(1, len(ans))):
                ans[i] += ans[i-1]
            ans.append(1)
        return ans

    def getRow2(self, rowIndex):   # creative but need double space in each iteration
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row


# Time:  O(n^2)
# Space: O(n), each iteration allocates a new array (may reuse but need at least n more space)
class Solution2:
    # @return a list of integers
    def getRow(self, rowIndex):
        result = [1]
        for i in range(1, rowIndex + 1):
            result = [1] + [result[j - 1] + result[j] for j in range(1, i)] + [1]
        return result


if __name__ == "__main__":
    print(Solution2().getRow(10))
