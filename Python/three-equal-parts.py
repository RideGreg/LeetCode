# Time:  O(n)
# Space: O(1)

#927 contest 107 10/20/2018
#Given an array A of 0s and 1s, divide the array into 3 non-empty parts such that all of these parts represent the same binary value.
#If it is possible, return any [i, j] with i+1 < j, such that:

#A[0], A[1], ..., A[i] is the first part;
#A[i+1], A[i+2], ..., A[j-1] is the second part, and
#A[j], A[j+1], ..., A[A.length - 1] is the third part.
#All three parts have equal binary value.

#If it is not possible, return [-1, -1].

#Note that the entire part is used when considering what binary value it represents.  For example, 
#[1,1,0] represents 6 in decimal, not 3.  Also, leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.
#

#Example 1:
#Input: [1,0,1,0,1]
#Output: [0,3]#

#Example 2:
#Input: [1,1,0,1,1]
#Output: [-1,-1]#

#Note:
#3 <= A.length <= 30000
#A[i] == 0 or A[i] == 1

# Solution
# Intuition
# Each part has to have the same number of ones in their representation.

# Algorithm
# Say S is the number of ones in A. Since every part has the same number of ones, they all should have T = S / 3 ones.

# If S isn't divisible by 3, the task is impossible.

# We can find the position of the 1st, T-th, T+1-th, 2T-th, 2T+1-th, and 3T-th one. The positions of these ones form 
# 3 intervals: [i1, j1], [i2, j2], [i3, j3]. (If there are only 3 ones, then the intervals are each length 1.)

# Between them, there may be some number of zeros. The zeros after j3 must be included in each part: 
#say there are z of them (z = S.length - j3).

# So the first part, [i1, j1], is now [i1, j1+z]. Similarly, the second part, [i2, j2], is now [i2, j2+z].

# If all this is actually possible, then the final answer is [j1+z, j2+z+1].

class Solution(object):
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        total = sum(A)
        if total % 3 != 0:
            return [-1, -1]
        if total == 0:
            return [0, len(A)-1]

        count = total//3
        nums = [0]*3
        c = 0
        for i in xrange(len(A)):
            if A[i] == 1:
                if c % count == 0:
                    nums[c//count] = i
                c += 1

        while nums[2] != len(A):
            if not A[nums[0]] == A[nums[1]] == A[nums[2]]:
                return [-1, -1]
            nums[0] += 1
            nums[1] += 1
            nums[2] += 1
        return [nums[0]-1, nums[1]]

print(Solution().threeEqualParts([0,1,1,0,1])) #[1,3]
print(Solution().threeEqualParts([0,1,0,1,1])) #[1,4]
print(Solution().threeEqualParts([1,0,1,0,1])) #[0,3]
print(Solution().threeEqualParts([1,1,0,1,1]))#[-1,-1]
print(Solution().threeEqualParts([1,0,1,1])) #[0,3]
print(Solution().threeEqualParts([0,0,0])) #[0,2]
