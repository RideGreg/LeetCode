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
        count, ans = 0, None
        for num in nums:
            if count == 0:
                ans = num

            if num == ans:
                count += 1
            else:
                count -= 1
        return ans

    # HashMap. Time: O(n), Space: O(n). Scan once by MAINTAIN MAX during scan
    def majorityElement2(self, nums):
        ans, maxCnt = None, 0
        cnt = collections.defaultdict(int)
        for x in nums:
            cnt[x] += 1
            if cnt[x] > maxCnt:
                ans, maxCnt= x, cnt[x]
        return ans

    # HashMap. Time: O(n), Space: O(n)
    def majorityElement_sacnTwice(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

        # sorting is unnecessary, directly get max
        # return sorted(counts.items(), key=lambda a: a[1], reverse=True)[0][0]

        # OR: return collections.Counter(nums).most_common(1)[0][0]

    def majorityElement_sorting(self, nums):
        # sorting original list, the majority elem always takes floor(n/2) position
        # Time: O(nlogn), Space: O(1)
        nums.sort()
        return nums[len(nums) // 2]

if __name__ == "__main__":
    print Solution().majorityElement([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6])
