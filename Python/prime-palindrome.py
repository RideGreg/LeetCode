# Time:  O(n^(1/2) * (logn + n^(1/2)))
# Space: O(logn), space used by str(i)
# Remember: check whether is a palindrome O(logN) time, check whether it is prime O(sqrt(N)) time.
#           How to build a list of palindromes which has a certain # of digits

# 866
# Find the smallest prime palindrome greater than or equal to N.
# Recall that a number is prime if it's only divisors are 1 and itself,
# and it is greater than 1.
#
# For example, 2,3,5,7,11 and 13 are primes.
#
# Recall that a number is a palindrome if it reads the same from
# left to right as it does from right to left.
#
# For example, 12321 is a palindrome.
#
# Example 1:
#
# Input: 6
# Output: 7
# Example 2:
#
# Input: 8
# Output: 11
# Example 3:
#
# Input: 13
# Output: 101
#
# Note:
# - 1 <= N <= 10^8
# - The answer is guaranteed to exist and be less than 2 * 10^8.

try:
    xrange          # Python 2
except NameError:
    xrange = range  # Python 3


    def primePalindrome_TLE(self, N):
        def isPrime(N):
            if N == 1: return False
            if N == 2: return True
            if N % 2 == 0: return False

            return all(n % d for d in xrange(3, int(n ** .5) + 1, 2))

        def isPalindrome(N):
            s = str(N)
            return all(s[0 + k] == s[-1 - k] for k in xrange(len(s) / 2))

        if 8 <= N <= 11: return 11

        ans = N
        while len(str(ans)) % 2 == 0 or not isPalindrome(ans) or not isPrime(ans):
            ans += 1
        return ans

class Solution(object):
    '''
    we can check whether is a palindrome in O(logN) time (number of digits), and check whether it is prime in O(sqrt(N)) time.
    So we would do the palindrome check first (logN is less than sqrt(N)).

    A number is a palindrome or prime are negatively correlated! For example, 22, 33, 44 ... 99 are clearly not prime.

    Actually, all palindromes with an even number of digits (except for 11) are divisible by 11, and are not prime!
    e.g. 'abba' = a * ((11-1)^0+(11-1)^3) + b * ((11-1)^1+(11-1)^2) => a*((-1)^0+(-1)^3) + b*((-1)^1+(-1)^2) = 0 (mod 11)

    Build palindrome, instead check whether each number is a palindrome (TLE)
    '''
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        def is_prime(n):
            # O(sqrt(n)) testing whether every number less than or equal to sqrt(n) is a divisor of n
            if n == 1: return False
            if n == 2: return True
            if n % 2 == 0: return False

            return all(n % d for d in xrange(3, int(n**.5) + 1, 2))
        '''
        # alternative: a prime (except 2 and 3) is of form 6k - 1 or 6k + 1.
        # https://en.wikipedia.org/wiki/AKS_primality_test
        def is_prime(n):
            if n <= 1: return False
            if n == 2 or n == 3: return True
            if n % 2 == 0 or n % 3 == 0:
                return False

            # starting from n=25, for n <25 already be filtered by %2, %3
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i+2) == 0:
                    return False
                i += 6

            return True
        '''

        # Special handling, all even-digit palindromes are not prime except 11. The algorithm below produces 101 for 8<=N<=11.
        if 8 <= N <= 11:
            return 11

        power = len(str(N)) // 2
        for i in xrange(10**power, 10**5):
            # only check palindrome w/ odd numbers of digits
            j = int(str(i) + str(i)[-2::-1])
            if j >= N and is_prime(j):
                return j

    '''
    Even we don't know that palindromes (>11) with even # of digits are never prime, we can generate and scan all palindromes.
    Each palindrome of d digits has a palindromic root, it's first k= (d+1)/2 digits. The next palindrome is formed by 
    the incremental root. For example, if 123 is a root for the 5 digit palindrome 12321, then the next palindrome 
    is 12421 with root 124. Notice that roots and palindromes are not a bijection, as palindromes 123321 and 12321 have 
    the same root.
    '''
    def primePalindrome2(self, N):
        def is_prime(n):
            return n > 1 and all(n%d for d in xrange(2, int(n**.5) + 1))

        length = len(str(N))
        p = (length + 1) / 2
        for rootLen in xrange(p, 6):
            #Check for odd-length (1,3,5...) palindromes
            if length <= 2 * rootLen - 1:
                for root in xrange(10**(rootLen - 1), 10**rootLen): #(1,9), (10,99), (100, 999)
                    s = str(root)
                    x = int(s + s[-2::-1]) #eg. s = '123' to x = int('12321')
                    if x >= N and is_prime(x):
                        return x
                        #If we didn't check for even-length palindromes:
                        #return min(x, 11) if N <= 11 else x

            #Check for even-length (2,4,6...) palindromes
            for root in xrange(10**(rootLen - 1), 10**rootLen):
                s = str(root)
                x = int(s + s[-1::-1]) #eg. s = '123' to x = int('123321')
                if x >= N and is_prime(x):
                    return x



    def primePalindrome_TLE(self, N): # Brute Force scan: TLE
        def isPrime(N):
            if N == 1: return False
            if N == 2: return True
            if N % 2 == 0: return False

            return all(N % d for d in xrange(3, int(N ** .5) + 1, 2))

        def isPalindrome(N):
            s = str(N)
            return all(s[0 + k] == s[-1 - k] for k in xrange(len(s) / 2))

        if 8 <= N <= 11: return 11

        ans = N
        while len(str(ans)) % 2 == 0 or not isPalindrome(ans) or not isPrime(ans):
            ans += 1
        return ans


print(Solution().primePalindrome(12))  #101
print(Solution().primePalindrome(123))  #131
print(Solution().primePalindrome(1234))  #10301
print(Solution().primePalindrome(12345))  #12421
print(Solution().primePalindrome(123456))  #1003001