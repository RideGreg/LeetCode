# Time:  O(n + logk)
# Space: O(1)

class Solution(object):
    def addToArrayForm(self, A, K): # USE THIS O(n) where n is length of A
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        n = 0
        for x in A:
            n = n *10 + x
        n += K

        if n == 0: return [0]
        ans = []
        while n:
            n, r = divmod(n, 10)
            ans.append(r)
        return reversed(ans)
        # or return map(int, str(n))


    def addToArrayForm_LeetcodeOfficial(self, A, K):
        A.reverse()
        carry, i = K, 0
        A[i] += carry
        carry, A[i] = divmod(A[i], 10)
        while carry:
            i += 1
            if i < len(A):
                A[i] += carry
            else:
                A.append(carry)
            carry, A[i] = divmod(A[i], 10)
        A.reverse()
        return A
