# Time:  O(n)
# Space: O(1)

# 930 contest 108 10/27/2018
# In an array A of 0s and 1s, how many non-empty subarrays have sum S?# 

# Example 1:
# Input: A = [1,0,1,0,1], S = 2
# Output: 4

# Explanation: 
# The 4 subarrays are bolded below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]

# Note:
# A.length <= 30000
# 0 <= S <= A.length
# A[i] is either 0 or 1.

# Two pointers solution
class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        #Solution: Three Pointer
        #Intuition
        #For each j, let's try to count the number of i's that have the subarray [i, j] equal to S.
        #It is easy to see these i's form an interval [left, right], and each of left, right are increasing with respect to j. 
        #So we can use a "two pointer" style approach.

        #Algorithm
        #For each j (in increasing order), let's maintain 4 variables:
        #sum_left : the sum of subarray [i_left, j]
        #sum_right : the sum of subarray [i_right, j]
        #left : the smallest i so that sum_left <= S
        #right : the largest i so that sum_right <= S
        #Then, (provided that sum_left == S), the number of subarrays ending in j is right - left + 1.
        #As an example, with A = [1,0,0,1,0,1] and S = 2, when j = 5, we want left = 1 and right = 3.

        result = 0
        left, right, sum_left, sum_right = 0, 0, 0, 0
        for i, a in enumerate(A):
            # Maintain left, sum_left: while the sum is too big, left += 1
            sum_left += a
            while left < i and sum_left > S:
                sum_left -= A[left]
                left += 1

            # Maintain right, sum_right: while the sum is too big, or equal and we can move, right += 1
            sum_right += a
            while right < i and \
                  (sum_right > S or (sum_right == S and not A[right])):
                sum_right -= A[right]
                right += 1

            if sum_left == S:
                result += right-left+1
        return result

    # Time:  O(n)
    # Space: O(u), u is the number of unique numbers in A
    def numSubarraysWithSum_prefixSum(self, A, S): # USE THIS: easy to understand, worse space complexity
        import collections
        lookup = collections.defaultdict(int)
        lookup[0] = 1
        psum, ans = 0, 0
        for a in A:
            psum += a
            ans += lookup[psum-S]
            lookup[psum] += 1
        return ans

    def numSubarraysWithSum_prefixSumAnother(self, A, S): # count all prefix sum upfront, edge case of S=0: not very good
        import collections
        count = collections.Counter({0:1})
        psum = 0
        for a in A:
            psum += a
            count[psum] += 1
        ans = 0
        for k, v in count.iteritems():
            if S != 0:
                ans += v * (count[k+S])
            else:
                ans += v*(v-1)/2
        return ans

print(Solution().numSubarraysWithSum([1,0,1,0,1], 2)) # 4
print(Solution().numSubarraysWithSum([1,0,1,0,1], 4)) # 0
print(Solution().numSubarraysWithSum([0,0,0,0,0], 0)) # 15
print(Solution().numSubarraysWithSum([1,0,0,0,0], 2)) # 0
