# Time:  O(n)
# Space: O(1)

# 1359
# Given n orders, each order consist in pickup and delivery services.
#
# Count all valid pickup/delivery possible sequences such that
# delivery(i) is always after of pickup(i).
#
# Since the answer may be too large, return it modulo 10^9 + 7.

# Solution: find recursion function
# suppose f_i-1 is the # of possible sequences for i-1 order (2*(i-1) items),
# f_i needs to insert 1 new order:
# if Pi and Di are continuous, there are 2i-1 places to insert;
# if Pi and Di are separate, we find 2 places from 2i-1 = C(2i-1, 2) = (2i-1)*(i-1)
# so f_i = f_i-1 * (2i-1 + (2i-1)*(i-1)) = f_i-1 * (2i-1) * i

class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9+7
        result = 1
        for i in range(2, n+1):
            result = result * i*(2*i-1) % MOD
        return result

print(Solution().countOrders(1)) # 1 P1 D1
print(Solution().countOrders(2)) # 6 (P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) (P2,D2,P1,D1)
print(Solution().countOrders(3)) # 90
