# Time:  O(n^2)
# Space: O(1)
# 118
# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows): # USE THIS: very elegant
        res = []
        for i in range(numRows):
            if i == 0:
                res.append([1])
            else:
                res.append([x+y for x,y in zip([0]+res[-1], res[-1]+[0])])
                # OR res += list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1]))
        return res

    def generate2(self, numRows): # also ok
        ans = []
        for i in range(numRows):
            if i == 0:
                ans.append([1])
            else:
                ans.append([1] +
                           [ans[-1][i]+ans[-1][i-1] for i in range(1, len(ans[-1]))] +
                           [1])
        return ans

if __name__ == "__main__":
    print Solution().generate(5)
