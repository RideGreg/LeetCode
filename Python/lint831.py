class Solution:
    """
    @param n: an integer
    @return: the number of solutions
    """
    def threeSum2(self, n):
        nums, ans = range(int(n**0.5)+1), 0
        for i in nums:
            j, k = 0, i
            while j <= k:
                s = i**2+j**2+k**2
                if s == n:
                    ans += 1
                    j+=1
                    k-=1
                elif s < n:
                    j+=1
                else:
                    k-=1
        return ans

print Solution().threeSum2(0)#000
print Solution().threeSum2(1)#001
print Solution().threeSum2(2)#011
print Solution().threeSum2(3)#111
print Solution().threeSum2(4)#002
print Solution().threeSum2(5)#012
print Solution().threeSum2(6)#112
print Solution().threeSum2(7)#
print Solution().threeSum2(8)#220
print Solution().threeSum2(9)#221 003