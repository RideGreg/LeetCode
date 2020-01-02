# Time:  O(n)
# Space: O(n)

# 1073  weekly contest 139 6/1/2019
# Given two numbers arr1 and arr2 in base -2, return the result of adding them together.
#
# Each number is given in array format:  as an array of 0s and 1s, from most significant bit to least significant bit.
# For example, arr = [1,1,0,1] represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3.  A number arr in array format
# is also guaranteed to have no leading zeros: either arr == [0] or arr[0] == 1.
#
# Return the result of adding arr1 and arr2 in the same format: as an array of 0s and 1s with no leading zeros.
class Solution(object):
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        result = []
        carry = 0
        while arr1 or arr2 or carry:
            if arr1:
                carry += arr1.pop()
            if arr2:
                carry += arr2.pop()
            result.append(carry & 1)  # carry % -2. Same to (-carry) & 1
            carry = -(carry >> 1)  # carry //= -2
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return result[::-1]

    def addNegabinary2(self, arr1, arr2):
        S = 0
        for a in [arr1, arr2]:
            for i, n in enumerate(reversed(a)):
                S += (-2)**i * n

        if S == 0: return [0]
        ans = []
        while S:
            ans.append((-S) & 1)  # N % -2. Same to S&1
            S = - (S >> 1)  # N //= -2
        return ans[::-1]

print(Solution().addNegabinary([1,1,1,1,1], [1,0,1])) # [1,0,0,0,0]