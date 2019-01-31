# Time:  O(1)
# Space: O(1)

# 957
# There are 8 prison cells in a row, and each cell is either occupied or vacant.
#
# Each day, whether the cell is occupied or vacant changes according to the following rules:
#
# If a cell has 2 adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
# Otherwise, it becomes vacant.
# (Note that because the prison is a row, the first/last cells in the row can't have two adjacent neighbors.)
#
# We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is
# occupied, else cells[i] == 0.
#
# Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

# cells.length == 8
# cells[i] is in {0, 1}
# 1 <= N <= 10^9

# Input: cells = [0,1,0,1,1,0,0,1], N = 7
# Output: [0,0,1,1,0,0,0,0]
# Explanation:
# The following table summarizes the state of the prison on each day:
# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

# Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
# Output: [0,0,1,1,1,1,1,0]


# Solution: there are at most 256 possible states for the prison, eventually the states repeat into
# a cycle rather quickly. Keep track of when the states repeat to find the period t of this cycle,
# and skip days in multiples of t.
class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        def nextday(cells):
            return [0] + [int(cells[i - 1] == cells[i + 1]) for i in xrange(1, 7)] + [0]

        seen = {}
        while N:
            c = tuple(cells)
            if c in seen:
                N %= seen[c] - N
            seen[c] = N

            if N:
                N -= 1
                cells = nextday(c)

        return cells

    def prisonAfterNDays_kamyu(self, cells, N):
        N -= max(N-1, 0) // 14 * 14  # 14 is got from Solution2
        for i in xrange(N):
            cells = [0] + [cells[i-1] ^ cells[i+1] ^ 1 for i in xrange(1, 7)] + [0]
        return cells


# Time:  O(1)
# Space: O(1)
class Solution2(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        cells = tuple(cells)
        lookup = {}
        while N:
            lookup[cells] = N
            N -= 1
            cells = tuple([0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in xrange(1, 7)] + [0])
            if cells in lookup:
                assert(lookup[cells] - N in (1, 7, 14))
                N %= lookup[cells] - N
                break

        while N:
            N -= 1
            cells = tuple([0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in xrange(1, 7)] + [0])
        return list(cells)
