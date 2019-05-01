# Time:  O(nlogr)
# Space: O(1)

# 1011
# A conveyor belt has packages that must be shipped from one port to another within D days.
#
# The i-th package on the conveyor belt has a weight of weights[i].  Each day, we load the ship
# with packages on the conveyor belt (in the order given by weights). We may not load more weight
# than the maximum weight capacity of the ship.
#
# Return the least weight capacity of the ship that will result in all the packages
# on the conveyor belt being shipped within D days.

# Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
# Output: 15

# Input: weights = [3,2,2,4,1,4], D = 3
# Output: 6

# Input: weights = [1,2,3,1,1], D = 4
# Output: 3


# Solution:
# Given the number of bags,
# return the minimum capacity of each bag,
# so that we can put items one by one into all bags.
#
# Similar as
# 875. Koko Eating Bananas
# 774. Minimize Max Distance to Gas Station

class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        def possible(mid):
            need, curr = 1, 0
            for w in weights:
                if curr+w > mid:
                    need += 1
                    curr = w
                    if need > D: return False
                else:
                    curr += w
            return True
    
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right-left)//2
            if possible(mid):
                right = mid
            else:
                left = mid+1
        return left
