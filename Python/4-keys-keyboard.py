#-*- coding: UTF-8 -*- 
# LeetCode 651. 4 Keys Keyboard# 
# Imagine you have a special keyboard with the following keys:# 
# Key 1: (A): Prints one 'A' on screen.# 
# Key 2: (Ctrl-A): Select the whole screen.# 
# Key 3: (Ctrl-C): Copy selection to buffer.# 
# Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.# 
# Now, you can only press the keyboard for N times (with the above four keys), find out the maximum numbers of 'A' you can print on screen.


# Time:  O(1)
# Space: O(1)
#https://discuss.leetcode.com/topic/97764/o-1-time-o-1-space-c-solution-possibly-shortest-and-fastest
#Pure math. This problem is to partition number N into 3's and 4's and get their
#product. n = N / 5 + 1 is to compute the number of factors(the total number of
#    3's and 4's). With n, it's easy to know how many out of them are 3's by
#computing n3 = n * 5 - 1 - N. We minus 1 here because adding a single factor
#requires one step more than the factor itself, e.g. x4 takes 5 steps
#(select all, copy, paste, paste, paste). 10 is special here because it's the
#only > 6 number where there is no enough factors to share cuts from decrement
#of the number of 3's which means a 5 has to be introduced.

class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 7: return N
        if N == 10: return 20  # the following rule doesn't hold when N = 10

        n  = N // 5 + 1  # n3 + n4 increases one every 5 keys 
        # (1) n     =     n3 +     n4
        # (2) N + 1 = 4 * n3 + 5 * n4
        #     5 x (1) - (2) => 5*n - N - 1 = n3
        n3 = 5*n - N - 1  
        n4 = n - n3
        return 3**n3 * 4**n4


# Time:  O(n) DP but inner loop doesn't iterate all
# Space: O(1) %6 is to reuse space, can remove %6 fo easier understanding
# https://discuss.leetcode.com/topic/97628/java-4-lines-recursion-with-step-by-step-explanation-to-derive-dp/2
class Solution2(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 7: return N
        dp = range(N+1) # can be dp = range(7)
        for i in xrange(7, N+1):
            dp[i % 6] = max(dp[(i-4) % 6]*3, dp[(i-5) % 6]*4)
#            dp[i % 6] = max(dp[(i-3) % 6]*2, dp[(i-4) % 6]*3, dp[(i-5) % 6]*4, dp[(i-6) % 6]*5)
        return dp[N % 6]

# Time: O(n^2) DP 用一个一维数组dp,其中dp[i]表示步骤总数为i时
# 能打印出的最多A的个数,初始化为N+1个,遍历所有打印A的个数,然后乘以粘贴的次数加1,用来更新dp[i]
# Space: O(n)
class Solution3(object):
    def maxA(self, N):
        dp = range(N+1)
        for i in xrange(7, N+1):
            for j in xrange(1, i-2):
                dp[i] = max(dp[i], dp[j] * (i-j-1))
        return dp[N]
# class Solution2 {
# public:
#     int maxA(int N) {
#         vector<int> dp(N + 1, 0);
#         for (int i = 0; i <= N; ++i) {
#             dp[i] = i;
#             for (int j = 1; j < i - 2; ++j) {
#                 dp[i] = max(dp[i], dp[j] * (i - j - 1));
#             }
#         }
#         return dp[N];
#     }
# };

print Solution2().maxA(7) #9
print Solution2().maxA(8) #12
print Solution2().maxA(9) #16
print Solution2().maxA(10) #20
print Solution2().maxA(11) #27
print Solution2().maxA(12) #36

 