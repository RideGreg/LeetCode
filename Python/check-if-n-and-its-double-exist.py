# Time:  O(n)
# Space: O(n)

# 1346 weekly contest 175 2/8/2020

# Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
#
# More formally check if there exists two indices i and j such that :
#
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        lookup = set()
        for x in arr:
            if 2*x in lookup or \
               (x%2 == 0 and x//2 in lookup):
                return True
            lookup.add(x)
        return False

print(Solution().checkIfExist([10,2,5,3])) # True
print(Solution().checkIfExist([3,1,7,11])) # False
