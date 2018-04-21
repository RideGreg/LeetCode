# Time:  O(n*2^n)
# Space: O(2^n)

# Given an array of integers nums and a positive integer k,
# find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.
#
# Example 1:
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
# Note:
#
# 1 <= k <= len(nums) <= 16.
# 0 < nums[i] < 10000.

# Memoization solution.
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def dfs(nums, target, used, todo, lookup):
            if lookup[used] is None:
                targ = (todo-1)%target + 1
                lookup[used] = any(dfs(nums, target, used | (1<<i), todo-num, lookup) \
                                   for i, num in enumerate(nums) \
                                   if ((used>>i) & 1) == 0 and num <= targ)
            return lookup[used]

        total = sum(nums)
        if total%k or max(nums) > total//k:
            return False
        lookup = [None] * (1 << len(nums))
        lookup[-1] = True
        return dfs(nums, total//k, 0, total, lookup)

    
# Time:  O(k^(n-k) * k!) tree is n-k level, k vertex per level; 
# Space: O(n)
# DFS solution with pruning.
class Solution2(object): ######### use this
    def canPartitionKSubsets(self, nums, k):
        def dfs(nums, target, i, subset_sums):
#            print subset_sums
            if i == len(nums):
                return True
            for k in xrange(len(subset_sums)):
                if subset_sums[k]+nums[i] > target:
                    continue
                subset_sums[k] += nums[i]
                if dfs(nums, target, i+1, subset_sums):
                    return True
                subset_sums[k] -= nums[i]
                if not subset_sums[k]:
                    break
            return False

        total = sum(nums)
        if total%k != 0 or max(nums) > total//k:
            return False
        nums.sort(reverse=True)
        subset_sums = [0] * k
        return dfs(nums, total//k, 0, subset_sums)

print Solution2().canPartitionKSubsets([3]*4, 3)
print Solution2().canPartitionKSubsets([2, 2, 10, 5, 2,7,2,2,13], 3)

class Solution_voyageck(object): #similar to Solution2 but dfs not return value
    def canPartitionKSubsets(self, nums, k):
        n = len(nums)
        sumN = sum(nums)
        if sumN%k!=0: return False
        avg = sumN / k
        nums.sort(reverse = True)              
        
        p = [0] * k        
        self.flag = False        
        def dfs(i):
            if i==n or self.flag:
                self.flag = True
                return
            for j in range(k):
                if (j==0 or p[j]!=p[j-1]) and  p[j]+nums[i]<=avg:
                    p[j] += nums[i]
                    dfs(i+1)
                    p[j] -= nums[i]
        dfs(0)
        return self.flag

class Solution_ming(object):
    def dfs(self, nums, sums, taken, goal, k, N, curIdx, limitIdx):
        if sums == goal:
            if curIdx == k - 2:
                return True
            return self.dfs(nums, 0, taken, goal, k, N, curIdx+1, N-1)
        i = limitIdx
        while i >= 0:
            if taken[i] == 0 and sums+nums[i] <= goal:
                taken[i] = 1
                if self.dfs(nums, sums+nums[i], taken, goal, k, N, curIdx, i-1):
                    return True
                taken[i] = 0
            i -= 1
        return False

    def canPartitionKSubsets(self, nums, k):
        if k == 1:
            return True
        if len(nums) < k or sum(nums) % k != 0:
            return False
        goal = sum(nums) / k
        taken = [0] * len(nums)
        taken[-1] = 1
        sums = nums[-1]
        return self.dfs(nums, sums, taken, goal, k, len(nums), 0, len(nums)-1) 