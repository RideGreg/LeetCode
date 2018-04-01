class Solution:
    """
    @param n: the number n
    @return: the times n convert to 1
    """
    def digitConvert(self, n):
        ans = 0
        while n != 1:
            ans += 1
            n = 3*n+1 if n%2 else n/2
        return ans

print Solution().digitConvert(3)
print Solution().digitConvert(2)
