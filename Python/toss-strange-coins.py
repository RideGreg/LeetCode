# Time:  O(n^2)
# Space: O(n)

# 1230 biweekly contest 11 10/19/2019
# You have some coins.  The i-th coin has a probability prob[i] of facing heads when tossed.
#
# Return the probability that the number of coins facing heads equals target if you toss every coin exactly once.
#
# Constraints:
#
# 1 <= prob.length <= 1000
# 0 <= prob[i] <= 1
# 0 <= target <= prob.length
# Answers will be accepted as correct if they are within 10^-5 of the correct answer.

class Solution(object):
    def probabilityOfHeads(self, prob, target):
        """
        :type prob: List[float]
        :type target: int
        :rtype: float
        """
        dp = [1.0] + [0] * target #dp[heads] = prob, when 0 coin, only 0 head has 100% chance
        for k, p in enumerate(prob):
            for i in range(min(len(dp)-1, k+1), -1, -1):
                dp[i] *= (1 - p)
                if i > 0:
                    dp[i] += p * dp[i-1]
        return dp[target]

print(Solution().probabilityOfHeads([0.4], 1)) # 0.40000
print(Solution().probabilityOfHeads([0.4, 0.4], 2)) # 0.16000 = 0.4 * 0.4
print(Solution().probabilityOfHeads([0.4, 0.4], 1)) # 0.48000 = 0.4*0.6 + 0.6*0.4
print(Solution().probabilityOfHeads([0.4, 0.4], 0)) # 0.36000 = 0.6 * 0.6
print(Solution().probabilityOfHeads([0.4] * 5, 0)) # 0.07776 = 0.6**5
print(Solution().probabilityOfHeads([0.4] * 50, 3)) # 4.694e-8
