class Solution:
    """
    @param arr: The 2-dimension array
    @return: Return the column the leftmost one is located
    """
    def getColumn(self, arr):
        for c, v in enumerate(zip(*arr)):
            if v.count(1) > 0:
                return c

print Solution().getColumn([[0,0,0,1],[1,1,1,1]])
print Solution().getColumn([[0,0,0,1],[0,1,1,1]])