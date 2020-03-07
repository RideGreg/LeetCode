# Time:  O(log(min(m, n)))
# Space: O(1)

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Follow up: find the kth largest number of the two sorted arrays.

class Solution(object):
    '''
          left_part          |        right_part
    A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
    B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]
    '''
    # this solution is good for understand the idea, but it cannot be directly used to getKth (need some boundary check)
    def findMedianSortedArrays_leetcodeOfficial(self, nums1, nums2):
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            nums1, nums2, len1, len2 = nums2, nums1, len2, len1

        # The key point is to find a proper i, such that max_in_left <= min_in_right.
        # How to decide left? if len1+len2 is odd e.g 11, get left = 6th num; if len1+len2 is even e.g 10, get left = 5th num.
        # How to decide i? r needs to be the total # of nums1, so i is initialized as half of nums1, although i can start anywhere.
        l, r, left = 0, len1, (len1 + len2 + 1) / 2
        while l <= r:
            i = (r - l) / 2 + l
            j = left - i
            if i < len1 and nums2[j - 1] > nums1[i]:
                l = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                r = i - 1
            else:
                maxLeft = nums2[j - 1] if i < 1 else nums1[i - 1] if j < 1 else max(nums1[i - 1], nums2[j - 1])
                if (len1 + len2) % 2:
                    return maxLeft / 1.0
                minRight = nums2[j] if i >= len1 else nums1[i] if j >= len2 else min(nums1[i], nums2[j])
                return (maxLeft + minRight) / 2.0

    def findMedianSortedArrays(self, nums1, nums2): # USE THIS
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def getKth(A, B, k):
            m, n = len(A), len(B)
            l, r = 0, m
            while l <= r:
                i = l + (r-l)//2
                j = k - i
                if j < 0 or (i>0 and 0<=j<n and A[i-1] > B[j]): # boundary check for general k
                    r = i - 1
                elif j > n or (i<m and j>0 and A[i] < B[j-1]):
                    l = i + 1
                else:
                    return A[i-1] if j<1 else B[j-1] if i<1 else max(A[i-1], B[j-1])

        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)

        if (len1 + len2) % 2 == 1:
            return getKth(nums1, nums2, (len1 + len2)/2 + 1)
        else:
            return (getKth(nums1, nums2, (len1 + len2)/2) +
                    getKth(nums1, nums2, (len1 + len2)/2 + 1)) * 0.5


    def getKth_kamyu(self, A, B, k): # hard to understand
        m, n = len(A), len(B)
        left, right = 0, m
        while left < right:
            i = left + (right - left) / 2
            j = k - 1 - i
            if 0 <= j < n and A[i] >= B[j]:
                right = i
            else:
                left = i + 1

        Ai_minus_1 = A[left - 1] if left - 1 >= 0 else float("-inf")
        Bj = B[k - 1 - left] if k - 1 - left >= 0 else float("-inf")

        return max(Ai_minus_1, Bj)


# Time:  O(log(max(m, n)) * log(max_val - min_val))
# Space: O(1)
# Generic solution.
class Solution_Generic(object):
    def findMedianSortedArrays(self, nums1, nums2): # too complex
        len1, len2 = len(nums1), len(nums2)
        if (len1 + len2) % 2 == 1:
            return self.getKth([nums1, nums2], (len1 + len2)/2 + 1)
        else:
            return (self.getKth([nums1, nums2], (len1 + len2)/2) +
                    self.getKth([nums1, nums2], (len1 + len2)/2 + 1)) * 0.5

    def getKth(self, arrays, k):
        def binary_search(array, left, right, target, compare):
            while left <= right:
                mid = left + (right - left) / 2
                if compare(array, mid, target):
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        def match(arrays, num, target):
            res = 0
            for array in arrays:
                if array:
                    res += binary_search(array, 0, len(array) - 1, num, \
                                         lambda array, x, y: array[x] > y)
            return res >= target

        left, right = float("inf"), float("-inf")
        for array in arrays:
            if array:
                left = min(left, array[0])
                right = max(right, array[-1])

        return binary_search(arrays, left, right, k, match)

class Solution_3(object): # good to get median from MORE THAN 2 sorted lists
    def findMedianSortedArrays(self, A, B):

        if A is None and B is None:
            return -1.0
        lenA = len(A)
        lenB = len(B)
        lenn = lenA + lenB;

        indexA,indexB,indexC = 0,0,0
        C = [False for i in xrange(lenn)]
        while indexA < lenA and indexB < lenB:
            if A[indexA] < B[indexB]:
                C[indexC] = A[indexA]
                indexC += 1
                indexA += 1
            else:
                C[indexC] = B[indexB]
                indexC += 1
                indexB += 1

        while indexA < lenA:
            C[indexC] = A[indexA]
            indexC += 1
            indexA += 1

        while indexB < lenB:
            C[indexC] = B[indexB]
            indexC += 1
            indexB += 1

        indexM1 = (lenn - 1) / 2
        indexM2 = lenn / 2

        if (lenn % 2 == 0):
            return (C[indexM1] + C[indexM2]) / 2.0
        else:
            return C[indexM2] / 1.0

if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([3], [4]))
    print Solution().findMedianSortedArrays([], [2, 3])
    print Solution().findMedianSortedArrays([2], [1, 3])
    print Solution().findMedianSortedArrays([1, 2], [3, 4])

    print Solution().findMedianSortedArrays([1, 3, 5, 7], [2, 4, 6])
    print Solution().findMedianSortedArrays([1, 3, 5], [2, 4, 6])
    print Solution().findMedianSortedArrays([1, 3, 5], [2, 4, 6])

