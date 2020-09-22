# Time:  O(n * 2^(n - 1))
# Space: O(n)

# 1593
# Given a string s, return the maximum number of unique substrings that the given string can be split into.
#
# You can split string s into any list of non-empty substrings, where the concatenation of the substrings
# forms the original string. However, you must split the substrings such that all of them are unique.
#
# A substring is a contiguous sequence of characters within a string.

class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        def popcount(n):
            count = 0
            while n:
                n &= n-1
                count += 1
            return count
    
        result = 1
        total = 2**(len(s)-1)
        mask = 0
        while mask < total:
            if popcount(mask) < result:
                mask += 1
                continue
            lookup, curr, base = set(), [], total//2
            for i in range(len(s)):
                curr.append(s[i])
                if (mask&base) or base == 0:
                    if "".join(curr) in lookup:
                        mask = (mask | (base-1)) + 1 if base else mask+1  # pruning, try next mask without base
                        break
                    lookup.add("".join(curr))
                    curr = []
                base >>= 1
            else:
                result = max(result, len(lookup))
                mask += 1
        return result

    # Always extend right to resolve duplicate. backtrack to search for a better answer.
    # Since we do backtrack, it is ok for some path to have no answer when reaching the end of string.
    def maxUniqueSplit(self, s): # USE THIS: from awice
        seen = set()
        n = len(s)

        def search(i):
            if i == n:
                self.ans = max(self.ans, len(seen))
                return

            for j in range(i, n):
                w = s[i:j + 1]
                if w not in seen:
                    seen.add(w)
                    search(j + 1)
                    seen.discard(w)

        self.ans = 0
        search(0)
        return self.ans

    # Wrong for 'gahbag'. Use stack to go back left to resolve duplicate.
    def maxUniqueSplit_goLeft(self, s: str) -> int:
        lookup, stk = set(), []
        for i, c in enumerate(s):
            while c in lookup:
                last = stk.pop()
                lookup.discard(last)
                c = last + c

            lookup.add(c)
            stk.append(c)
        return len(lookup)

    # Wrong for 'addbsd'. First extend to right to resolve duplicate;
    # if at the end and cannot extend right, use stack to go back left to resolve duplicate.
    def maxUniqueSplit_extendRight(self, s: str) -> int:
        lookup, stk, curStr, done = set(), [], '', False
        for i, c in enumerate(s):
            done = False
            c = curStr + c
            if c not in lookup:
                lookup.add(c)
                stk.append(c)
                curStr = ''
                done = True
            else:
                curStr = c
        if not done:
            while c in lookup:
                last = stk.pop()
                lookup.discard(last)
                c = last + c

            lookup.add(c)
            stk.append(c)
        return len(lookup)

print(Solution().maxUniqueSplit("gahbag")) # 5 g a h b ag
print(Solution().maxUniqueSplit("addbsd")) # 5 a dd b s d
print(Solution().maxUniqueSplit("ababccc")) # 5