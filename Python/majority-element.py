# Time:  O(n)
# Space: O(1)
#
# 169
# Given an array of size n, find the majority element.
# The majority element is the element that appears more than floor(n/2) times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
import collections


class Solution:
    def majorityElement(self, nums): # USE THIS
        """
        :type nums: List[int]
        :rtype: int
        """
        # Boyer-Moore Voting Algorithm
        # Pick 1st elem as temporary answer, scan, when seeing same elem, count ++; when seeing
        # different elem, count --. When count is 0, pick the elem as new temporary answer and discard
        # all elems already scanned. Since it is impossible to discard more majority elements than minority elements,
        # we are safe in discarding the prefix and continuously look for majority elem in the suffix.
        # Eventually, count will not go to 0 and that answer is the same as answer for whole list.
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate


    def majorityElement2(self, nums):
        # HashMap. Time: O(n), Space: O(n)
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
        ''' # sorting is actually unnecessary
        return sorted(counts.items(), key=lambda a: a[1], reverse=True)[0][0]
        '''

    def majorityElement3(self, nums):
        # similar to solution majorityElement2
        return collections.Counter(nums).most_common(1)[0][0]

    def majorityElement_sorting(self, nums):
        # sorting original list, the majority elem always takes floor(n/2) position
        # Time: O(nlogn), Space: O(1)
        nums.sort()
        return nums[len(nums) // 2]

if __name__ == "__main__":
    print Solution().majorityElement([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6])
