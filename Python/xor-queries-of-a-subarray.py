# Time:  O(n)
# Space: O(1)

# 1310 weekly contest 170 1/4/2020

# Given the array arr of positive integers and the array queries where queries[i] = [Li, Ri], for
# each query i compute the XOR of elements from Li to Ri (that is, arr[Li] xor arr[Li+1] xor ...
# xor arr[Ri] ). Return an array containing the result for the given queries.

class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        for i in xrange(1, len(arr)):
            arr[i] ^= arr[i-1]
        return [arr[right] ^ arr[left-1] if left else arr[right] for left, right in queries]

    def xorQueries_ming(self, arr, queries):
        prefix = [arr[0]]
        for a in arr[1:]:
            prefix.append(prefix[-1]^a)
        return [prefix[r] if l==0 else prefix[l-1]^prefix[r] for l,r in queries]

print(Solution().xorQueries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]]))
print(Solution().xorQueries([4,8,2,10], [[2,3],[1,3],[0,0],[0,3]]))
