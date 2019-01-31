# Time:  O(n), length of A
# Space: O(n)

# 945
# Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.
# Return the least number of moves to make every value in A unique.

# 0 <= A.length <= 40000
# 0 <= A[i] < 40000

class Solution(object):
    # Counting: count the quantity of each element. "brute force" solution of incrementing dup values
    # repeatedly until it is unique, which may be a lot work. Better to do
    # lazily increment: save duplicate values; when find empty slots, then calculate the increment.
    def minIncrementForUnique(self, A): # USE THIS
        """
        :type A: List[int]
        :rtype: int
        """
        if not A: return 0

        import collections
        cnt = collections.Counter(A)
        duplicate, ans = [], 0
        for x in xrange(max(A)+len(A)):
            if cnt[x] > 1:
                duplicate.extend([x] * (cnt[x]-1))
            elif cnt[x] == 0 and duplicate:
                ans += x - duplicate.pop()
        return ans

    # Maintain Duplicate Info and Release Later: sort the input then traverse:
    # - If A[i-1] == A[i], we have a duplicate to take.
    # - If A[i-1] < A[i], we place our dup values into those free positions. Specifically, we have
    #   give = min(taken, A[i] - A[i-1] - 1) possible values to release, and they will have final values
    #   A[i-1] + 1, A[i-1] + 2, ..., A[i-1] + give.

    # Time: O(nlogn), sorting
    def minIncrementForUnique2(self, A): # too many KENG, difficult to use
        A.sort()
        A.append(float("inf")) # may need to move to max(A)+1, max(A)+2 ...
        result, duplicate = 0, 0
        for i in xrange(1, len(A)):
            if A[i-1] == A[i]:
                duplicate += 1
                result -= A[i] # source of a move; increment = dest-source
            else:
                move = min(duplicate, A[i]-A[i-1]-1)
                duplicate -= move
                result += move*A[i-1] + move*(move+1)//2 # dest: A[i-1]+1,...A[i-1]+move
        return result

    # brute force
    def minIncrementForUnique_bruteForce(self, A):
        final, dup, ans = set(), [], 0
        for a in A:
            if a not in final:
                final.add(a)
            else:
                dup.append(a)
        if not dup: return ans
        dup.sort()
        start = min(dup)
        for n in dup:
            start = max(start, n) + 1
            while start in final:
                start += 1
            final.add(start)
            ans += start-n
        return ans

print(Solution().minIncrementForUnique([1,2,2])) # 1
print(Solution().minIncrementForUnique([3,2,1,2,1,7])) # 6
print Solution().minIncrementForUnique([14,4,5,14,13,14,10,17,2,12,2,14,7,13,14,13,4,16,4,10]) #41
