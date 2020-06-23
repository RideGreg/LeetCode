# Time:  O(n)
# Space: O(1)

# 1014
# Given an array A of positive integers, A[i] represents the value of the i-th
# sightseeing spot, and two sightseeing spots i and j have distance j - i between them.
#
# The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) :
# the sum of the values of the sightseeing spots, minus the distance between them.
#
# Return the maximum score of a pair of sightseeing spots.

class Solution(object):
    # DP: for each new element, count the current best score in all previous sightseeing spot.
    # 得分公式A[i] + A[j] + i - j 中：A[j]-j 是固定的，因此我们需要最大化 A[i]+i for all previous i.
    # maintain a previous best elem
    # Note that, as we go further, the score of previous spot decrement.
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mx, ans = A[0] + 0, 0
        for i in range(1, len(A)):
            ans = max(ans, mx+A[i]-i)
            mx = max(mx, A[i] + i)
        return ans

    def maxScoreSightseeingPair2(self, A):
        ans, i = 0, 0
        for j in range(1, len(A)):
            ans = max(ans, A[j] + A[i] - (j - i))
            if A[j] + (j - i) > A[i]:
                i = j
        return ans

    # encapsulate value & index in 'x'. hard to understand.
    def maxScoreSightseeingPair_lee215(self, A):
        result, curr = 0, 0
        for x in A:
            result = max(result, curr+x)
            curr = max(curr, x)-1
        return result


print(Solution().maxScoreSightseeingPair([8,1,5,2,6])) # 11
print(Solution().maxScoreSightseeingPair([1,3,5])) # 7