class Solution:
    # @param m: An integer m denotes the size of a backpack
    # @param A: Given n items with size A[i]
    # @return: The maximum size

    def backPack(self, m, A):
        ans, dp = 0, [False for _ in xrange(m+1)]
        dp[0] = True
        for a in A:
            for i in reversed(xrange(a, m+1)):
                if dp[i-a]:
                    dp[i] = True
                    ans = max(ans, i)
        return ans

    def backPack_2(self, m, A):
        dp = [0 for _ in xrange(m+1)]
        for a in A:
            for i in reversed(xrange(a, m+1)):
                dp[i] = max(dp[i], a+dp[i-a])
        return dp[-1]

import timeit
# 4.27s
print timeit.timeit('Solution().backPack(80000, [81,112,609,341,164,601,97,709,944,828,627,730,460,523,643,901,602,508,401,442,738,443,555,471,97,644,184,964,418,492,920,897,99,711,916,178,189,202,72,692,86,716,588,297,512,605,209,100,107,938,246,251,921,767,825,133,465,224,807,455,179,436,201,842,325,694,132,891,973,107,284,203,272,538,137,248,329,234,175,108,745,708,453,101,823,937,639,485,524,660,873,367,153,191,756,162,50,267,166,996,552,675,383,615,985,339,868,393,178,932])',
              'from __main__ import Solution', number=5)
# 9.86s
print timeit.timeit('Solution().backPack_2(80000, [81,112,609,341,164,601,97,709,944,828,627,730,460,523,643,901,602,508,401,442,738,443,555,471,97,644,184,964,418,492,920,897,99,711,916,178,189,202,72,692,86,716,588,297,512,605,209,100,107,938,246,251,921,767,825,133,465,224,807,455,179,436,201,842,325,694,132,891,973,107,284,203,272,538,137,248,329,234,175,108,745,708,453,101,823,937,639,485,524,660,873,367,153,191,756,162,50,267,166,996,552,675,383,615,985,339,868,393,178,932])',
              'from __main__ import Solution', number=5)

#print Solution().backPack_2(90, [12,3,7,4,5,13,2,8,4,7,6,5,7])
#print Solution().backPack(10, [3,4,8,5])