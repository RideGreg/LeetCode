# Time:  O(n)
# Space: O(1)

# 995
# In an array A containing only 0s and 1s, a K-bit flip consists of choosing a (contiguous) subarray
# of length K and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.
#
# Return the minimum number of K-bit flips required so that there is no 0 in the array.  If it is not possible,
# return -1.

class Solution(object):
    # When we flip a subarray like A[i], A[i+1], ..., A[i+K-1]
    # we can instead flip our target. This is critical to avoid O(n*K) time complexity,
    # (swap K items for every eligible i).
    # And at position i+K, flip back our target.
    def minKBitFlips(self, A, K): # USE THIS
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        n = len(A)
        flip, ans = [False]*n, 0 # flip array stores whether this elem will flip
        target = 0  # when target is encoutered, we must flip
        for i in xrange(n):
            if i>=K and flip[i-K]:
                target = 1 - target # compensate and change target back

            if A[i] == target: # or A[i] ^ target == 0
                if i > n-K:
                    return -1
                flip[i] = True
                ans += 1
                target = 1 - target # for next K-1 elems, will flip 1 to 0,
                                    # so next 1 is bad and needs flip
        return ans

    def minKBitFlips_kamyu(self, A, K): # not understand
        result, curr = 0, 0
        for i in xrange(len(A)):
            if i >= K:
                curr -= A[i-K]//2
            if curr & 1 ^ A[i] == 0: # bit and > bit xor > bit or
                if i+K > len(A):
                    return -1
                A[i] += 2
                curr, result = curr+1, result+1
        return result


print(Solution().minKBitFlips([0,0,0,1,0,1,1,0], 3)) # 3
print(Solution().minKBitFlips([0, 1, 0], 1)) # 2
print(Solution().minKBitFlips([1, 1, 0], 2)) # -1
