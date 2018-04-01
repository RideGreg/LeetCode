from math import sqrt
class Solution:
    """
    @param n: the number
    @return: the rank of the number
    """
    def kthPrime(self, n):
        if n == 2: return 1
        p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307];
        ans = 2
        for i in xrange(3, n, 2):
            flag = True
            for j in p:
                if j >= i: break
                if i != j and i % j == 0:
                    flag = False
                    break

            if not flag: continue
            for j in xrange(311, int(sqrt(i))+1, 2):
                if i != j and i % j == 0:
                    flag = False
                    break

            if flag: ans += 1
        return ans

print Solution().kthPrime(2)
print Solution().kthPrime(3)
print Solution().kthPrime(5)
print Solution().kthPrime(7)
print Solution().kthPrime(11)
print Solution().kthPrime(13)
print Solution().kthPrime(17)
print Solution().kthPrime(19)
print Solution().kthPrime(23)

