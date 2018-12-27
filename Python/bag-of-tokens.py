# Time:  O(nlogn)
# Space: O(1)

# You have an initial power P, an initial score of 0 points, and a bag of tokens.
#
# Each token can be used at most once, has a value token[i], and has potentially two ways to use it.
# If we have at least token[i] power, we may play the token face up, losing token[i] power, and gaining 1 point.
# If we have at least 1 point, we may play the token face down, gaining token[i] power, and losing 1 point.
#
# Return the largest number of points we can have after playing any number of tokens.

# Solution: Greedy:
# We want to collect points as much as possible, so we should always play tokens face up until power exhaustion,
# then play one token face down and continue. Final answer could be any of the intermediate answers we got
# after playing tokens face up (but before spending point to play them face down.)

class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        tokens.sort()
        result, points = 0, 0
        left, right = 0, len(tokens)-1
        while left <= right:
            if P >= tokens[left]:
                P -= tokens[left]
                left += 1
                points += 1
                result = max(result, points)
            elif points > 0:
                points -= 1
                P += tokens[right]
                right -= 1
            else:
                break
        return result

print(Solution().bagOfTokensScore([100], 50)) # 0
print(Solution().bagOfTokensScore([100, 200], 150)) # 1
print(Solution().bagOfTokensScore([100, 200, 300, 400], 200)) # 2
