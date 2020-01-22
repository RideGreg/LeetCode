# Time:  O(nlogn)
# Space: O(1)

# 1300 biweekly contest 16 12/28/2019

# Given an integer array arr and a target value target, return the integer value such that when we change all the
# integers larger than value in the given array to be equal to value, the sum of the array gets as close as possible (in absolute difference) to target.
#
# In case of a tie, return the minimum such integer.
#
# Notice that the answer is not neccesarilly a number from arr.

# Constraints:
# 1 <= arr.length <= 10^4
# 1 <= arr[i], target <= 10^5

class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        arr.sort(reverse=True)
        max_arr = arr[0]
        while arr and arr[-1]*len(arr) <= target:
            target -= arr.pop()
        # let x = ceil(t/n)-1
        # (1) (t/n-1/2) <= x:
        #    return x, which is equal to ceil(t/n)-1 = ceil(t/n-1/2) = (2t+n-1)//2n
        # (2) (t/n-1/2) > x:
        #    return x+1, which is equal to ceil(t/n) = ceil(t/n-1/2) = (2t+n-1)//2n
        # (1) + (2) => both return (2t+n-1)//2n
        return max_arr if not arr else (2*target+len(arr)-1)//(2*len(arr))


# Time:  O(nlogn)
# Space: O(1)
class Solution2(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        arr.sort(reverse=True)
        max_arr = arr[0]
        while arr and arr[-1]*len(arr) <= target:
            target -= arr.pop()
        if not arr:
            return max_arr
        x = (target-1)//len(arr)
        return x if target-x*len(arr) <= (x+1)*len(arr)-target else x+1


# Time:  O(nlogm), m is the max of arr, which may be larger than n
# Space: O(1)
class Solution3(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        def total(arr, v):
            result = 0
            for x in arr:
                result += min(v, x)
            return result

        def check(arr, v, target):
            return total(arr, v) >= target
        
        left, right = 1, max(arr)
        while left <= right:
            mid = left + (right-left)//2
            if check(arr, mid, target):
                right = mid-1
            else:
                left = mid+1
        return left-1 if target-total(arr, left-1) <= total(arr, left)-target else left

    def findBestValue_ming(self, arr: List[int], target: int) -> int:
        import operator
        def valid(m, func):
            total = sum(min(m, x) for x in arr)
            diff = abs(total - target)
            if func(total, target) and diff < self.mindiff or (diff == self.mindiff and m < self.minm):
                self.mindiff, self.minm = diff, m
                return True
            else:
                return False

        l, r = 0, max(arr)
        self.mindiff, self.minm = float('inf'), float('inf')
        while l < r:
            m = (l + r + 1) // 2
            if valid(m, operator.le):
                l = m
            else:
                r = m - 1

        l2, r2 = 0, max(arr)
        self.mindiff, self.minm = float('inf'), float('inf')
        while l2 < r2:
            m = (l2 + r2) // 2
            if valid(m, operator.ge):
                r2 = m
            else:
                l2 = m + 1
        return l if abs(target-sum(min(l, x) for x in arr)) <= abs(target-sum(min(l2, x) for x in arr)) else l2



print(Solution().findBestValue([2,3,5], 10)) # 5
print(Solution().findBestValue([4,9,3], 10)) # 3
print(Solution().findBestValue([60864,25176,27249,21296,20204], 56803)) # 11361
