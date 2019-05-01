# Time:  O(n)
# Space: O(1)

# 1013
# Given an array A of integers, return true if and only if we can partition the array into
# three non-empty parts with equal sums.
#
# Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] +
# ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        total = sum(A)
        if total % 3 != 0:
            return False
        parts, curr = 0, 0
        for x in A:
            curr += x
            if curr == total//3:
                parts += 1
                curr = 0
                if parts == 2: return True
        return False

    def canThreePartsEqualSum_prefix(self, A):
        prefix = [A[0]]
        for a in A[1:]:
            prefix.append(prefix[-1] + a)
        ssum = prefix[-1]

        if ssum % 3: return False

        if ssum//3 in prefix:
            idx = prefix.index(ssum//3)
            if ssum*2//3 in prefix[idx+1:]:
                return True
        return False
