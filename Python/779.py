class Solution(object):
    def kthGrammar(self, N, K):
        def helper(N, K):
            l = pow(2, N-1)
            if l <= 4:
                a = [0,1,1,0]
                return a[K-1]
            if K <= l/2:
                return helper(N-1, K)
            if N % 2 == 1:
                return helper(N, l/2+1-(K-l/2))
            else:
                if K <= l*3/4:
                    return helper(N, K-l/4)
                else:
                    return helper(N, K-l*3/4)

        if N == 1:
            return 0
        return helper(N, K)

#            curr, l = [0,1], 2
#            while l < K:
#                curr.extend(curr[l/2:]+curr[:l/2])
#                l *= 2
#        return curr[K-1]



print Solution().kthGrammar(4,5)#1
print Solution().kthGrammar(6,9)#1
print Solution().kthGrammar(6,21)#0