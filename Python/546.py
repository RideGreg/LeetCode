class Solution(object):
    def removeBoxes(self, boxes):
        self.ans = 0

        def recur(A, pts):
            if not A:
                self.ans = max(self.ans, pts)
                return

            i = 0
            while i != len(A):
                j = i
                while j+1 < len(A) and A[j] == A[j+1]:
                    j += 1
                recur(A[:i]+A[j+1:], pts+(j-i+1)*(j-i+1))
                i = j+1

        recur(boxes, 0)
        return self.ans

print Solution().removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1])