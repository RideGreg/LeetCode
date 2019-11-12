# Time:  O(n + logk)
# Space: O(1)

class Solution(object):
    def addToArrayForm(self, A, K): # USE THIS
        A = A[::-1]
        for i in range(len(A)):
            if K == 0: break
            A[i] += K
            K, A[i] = divmod(A[i], 10)
        while K:
            K, x = divmod(K, 10)
            A.append(x)
        return A[::-1]

    def addToArrayForm2(self, A, K): # convert to int calc may not allowed
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


    def addToArrayForm_LeetcodeOfficial(self, A, K): # same to solution 1, but use while
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

print(Solution().addToArrayForm([1,2,0,0], 34)) # [1,2,3,4]
print(Solution().addToArrayForm([2,7,4], 181)) # [4,5,5]
print(Solution().addToArrayForm([2,1,5], 806)) # [1,0,2,1]
print(Solution().addToArrayForm([9,9,9,9,9,9,9,9,9,9], 1)) # [1,0,0,0,0,0,0,0,0,0,0]
print(Solution().addToArrayForm([8], 3333)) # [3,3,4,1]
