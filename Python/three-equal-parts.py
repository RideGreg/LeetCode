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

        countOnes = total//3
        starts = [0]*3
        id = 0
        for i in xrange(len(A)):
            if A[i] == 1:
                if id % countOnes == 0:
                    starts[id//countOnes] = i
                id += 1

        i, j, k = starts
        while k < len(A):
            if not A[i] == A[j] == A[k]:
                return [-1, -1]
            i += 1
            j += 1
            k += 1
        return [i-1, j]

    # Time: O(n), WORSE Space: O(n) to store position of ones
    def threeEqualParts_ming(self, A):
        posOne = [i for i, x in enumerate(A) if x==1]
        m = len(posOne)
        if m % 3: return [-1, -1]
        if m == 0: return [0,len(A)-1]

        e1, e2 = posOne[m/3-1], posOne[m*2/3-1]
        endZero = len(A)-1-posOne[-1]   ## KENG: use end of 3 parts may miss the zeroes at the end of list
        if A[e1+1:e1+1+endZero] != [0]*endZero or A[e2+1:e2+1+endZero] != [0]*endZero:
            return [-1, -1]
        e1 += endZero
        e2 += endZero

        s1, s2, s3 = 0, e1+1, e2+1
        while A[s1] == 0:
            s1 += 1
        while A[s2] == 0:
            s2 += 1
        while A[s3] == 0:
            s3 += 1
        return [e1, e2+1] if A[s1:e1+1]==A[s2:e2+1]==A[s3:] else [-1, -1]


print(Solution().threeEqualParts([1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,0]))
# [15, 32]
print(Solution().threeEqualParts([0,1,1,0,1])) #[1,3]
print(Solution().threeEqualParts([0,1,0,1,1])) #[1,4]
print(Solution().threeEqualParts([1,0,1,0,1])) #[0,3]
print(Solution().threeEqualParts([1,1,0,1,1]))#[-1,-1]
print(Solution().threeEqualParts([1,0,1,1])) #[0,3]
print(Solution().threeEqualParts([0,0,0])) #[0,2]
