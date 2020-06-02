# Time:  O(n)
# Space: O(1)

# 1431
# Given the array candies and the integer extraCandies, where candies[i] represents the # of candies
# that the ith kid has.
#
# For each kid check if there is a way to distribute extraCandies among the kids such that
# he or she can have the greatest number of candies among them. Notice that multiple kids can
# have the greatest number of candies.

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_num = max(candies)
        return [x + extraCandies >= max_num for x in candies]

print(Solution().kidsWithCandies([2,3,5,1,3], 3)) # [true,true,true,false,true] 