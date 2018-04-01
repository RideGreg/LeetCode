class Solution(object):
    def numJewelsInStones(self, J, S):
        d, ans = {}, 0
        for j in J:
            d[j] = 1
        for s in S:
            if s in d:
                ans += 1
        return ans

print Solution().numJewelsInStones('aA', "aAAbbbb")
print Solution().numJewelsInStones('A', "aAAbbbb")