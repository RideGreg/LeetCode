# Time:  O(n)
# Space: O(1)

# Given a list of positive integers, the adjacent integers will perform the float division.
# For example, [2,3,4] -> 2 / 3 / 4.
#
# However, you can add any number of parenthesis at any position to change the priority of operations.
# You should find out how to add parenthesis to get the maximum result,
# and return the corresponding expression in string format. Your expression should NOT contain redundant parenthesis.
#
# Example:
# Input: [1000,100,10,2]
# Output: "1000/(100/10/2)"
# Explanation:
# 1000/(100/10/2) = 1000/((100/10)/2) = 200
# However, the bold parenthesis in "1000/((100/10)/2)" are redundant, 
# since they don't influence the operation priority. So you should return "1000/(100/10/2)". 
#
# Other cases:
# 1000/(100/10)/2 = 50
# 1000/(100/(10/2)) = 50
# 1000/100/10/2 = 0.5
# 1000/100/(10/2) = 2
# Note:
#
# The length of the input array is [1, 10].
# Elements in the given array will be in range [2, 1000].
# There is only one optimal division for each test case.

class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])
        result = [str(nums[0]) + "/(" + str(nums[1])]
        for i in xrange(2, len(nums)):
            result += "/" + str(nums[i])
        result += ")"
        return "".join(result)

    def optimalDivision_awice(selfself, nums):
        A = map(str, nums)
        if len(A) <= 2: return '/'.join(A)
        return '{}/({})'.format(A[0], '/'.join(A[1:]))

    def optimalDivision_divide_conqure(self, nums):
        def find(l, r, nums):
            key = str(l) + '-' + str(r)
            if key in self.lookup:
                return self.lookup[key]

            if l == r: return [nums[l], nums[l], str(nums[l]), str(nums[l])]

            res = [0, 0, '', '']
            for m in xrange(l,r):
                left, right = find(l,m, nums), find(m+1, r, nums)
                mmin, mmax = 1.0*left[0]/right[1], 1.0*left[1]/right[0]
                if res[0] == 0 or mmin < res[0]:
                    res[0], res[2] = mmin, left[2]+'/'+(right[3] if m+1==r else '('+right[3]+')')
                if mmax > res[1]:
                    res[1], res[3] = mmax, left[3]+'/'+(right[2] if m+1==r else '('+right[2]+')')
            self.lookup[key] = res
            return res

        self.lookup = {}
        ans = find(0, len(nums)-1, nums)
        return ans[3]

print Solution().optimalDivision_awice([1000,100,10,2,5,7])
print Solution().optimalDivision_divide_conqure([1000,100,10,2,5,7])
