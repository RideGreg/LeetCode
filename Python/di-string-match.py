# Time:  O(n)
# Space: O(1)

# 942
# Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
# Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
# - If S[i] == "I", then A[i] < A[i+1]
# - If S[i] == "D", then A[i] > A[i+1]

# solution:
# If we see S[0] == 'I', always put 0 as the first element; if we see S[0] == 'D', always put N as the first element.
#
# Why this works? Say we have a match for the rest of the string S[1], S[2], ... using N distinct elements. Notice
# it doesn't matter what the sequence is, only that they are distinct and totally ordered. Then, putting 0 or N at the
# first character will match, and the rest of the elements (1, 2, ..., N or 0, 1, ..., N-1) can use for the sub-problem.
#
# Algorithm
# Keep track of the smallest and largest element we haven't placed. If we see an 'I', place the small element;
# otherwise place the large element.

class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        result = []
        left, right = 0, len(S)
        for c in S:
            if c == 'I':
                result.append(left)
                left += 1
            else:
                result.append(right)
                right -= 1
        result.append(left) # we have left == right now
        return result

print(Solution().diStringMatch("IDID")) # [0, 4, 1, 3, 2]
print(Solution().diStringMatch("III")) # [0, 1, 2, 3]
print(Solution().diStringMatch("DDI")) # [3, 2, 0, 1]
