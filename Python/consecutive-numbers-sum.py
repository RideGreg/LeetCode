# Time:  O(sqrt(n))
# Space: O(1)

# Given a positive integer N,
# how many ways can we write it as a sum of
# consecutive positive integers?
#
# Example 1:
#
# Input: 5
# Output: 2
# Explanation: 5 = 5 = 2 + 3
# Example 2:
#
# Input: 9
# Output: 3
# Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
# Example 3:
#
# Input: 15
# Output: 4
# Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
# Note: 1 <= N <= 10 ^ 9.

import math
class Solution(object):
    # Math search in limited scope. Time O(sqrt(n))
    # Assume N = x + (x+1) + ... (x+l-1), the sequence has length l
    # N = x*l + l(l-1)//2. Check if N- l(l-1)//2 is divisible by l.
    #
    # The key is limit the scope of l. Note 2N = l * (2x + l - 1)
    # and l < 2x+l-1 => l < sqrt(2N)
    def consecutiveNumbersSum(self, N):      # USE THIS
        ans = 0
        for l in range(1, int(math.sqrt(2*N)) + 1):  # sequence length cannot be >= N
            if (N - l * (l - 1) // 2) % l == 0:
                ans += 1
        return ans


    # Fancy math, prime factorization. Need math expertise to get the solution.
    def consecutiveNumbersSum2(self, N):
        """
        :type N: int
        :rtype: int
        """
        # Get all 2 factors out from N: N = 2^k * M, where M is odd.
        # If N can be written as x + x+1 + x+2 + ... + x+l-1
        # => l*x + (l-1)*l/2 = 2^k * M
        # => x = (2^k * M -(l-1)*l/2)/l= 2^k * M/l - (l-1)/2 is integer
        # => l could be 2 or any odd factor of M (excluding M)
        #    s.t. x = 2^k * M/l - (l-1)/2 is integer, and also unique
        # => the answer is the number of all odd factors of M
        # More specific，
        # if prime factorization of N is 2^k * p1^a * p2^b * ..
        # => answer is the number of all odd factors = (a+1) * (b+1) * ...

        while N % 2 == 0: # remove factor 2
            N >>= 1

        result = 1
        i = 3            # check all odd factors
        while i*i <= N:
            count = 0
            while N % i == 0:
                N //= i
                count += 1
            result *= count+1
            i += 2
        if N > 1:
            result *= 2
        return result


    # brute force: TLE. Time O(N*sqrt(N)) Naive enumerate start integer
    def consecutiveNumbersSum_bruteForce(self, N):
        ans = 0
        for start in range(1, N+1):
            target = N
            while target > 0:
                target -= start
                start += 1
            if target == 0: ans += 1
        return ans

print(Solution().consecutiveNumbersSum(5)) # 2: 5 = 2 + 3
print(Solution().consecutiveNumbersSum(9)) # 3: 9 = 4 + 5 = 2 + 3 + 4
print(Solution().consecutiveNumbersSum(15)) # 4: 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5