class Solution(object):
    def countPrimeSetBits(self, L, R):
        plist = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199])
        ans = 0
        for i in xrange(L, R+1):
            cnt = 0
            while i > 0:
                if i%2 == 1:
                    cnt += 1
                i = i / 2
            if cnt in plist:
                ans += 1
        return ans

print Solution().countPrimeSetBits(6,10)
print Solution().countPrimeSetBits(10,15)