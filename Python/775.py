class Solution(object):
    def isIdealPermutation(self, A):
        def merge(a, b):
            c, inv = [], 0
            i, j = 0, 0
            while len(a) != i and len(b) != j:
                if a[i] < b[j]:
                    c.append(a[i])
                    i+=1
                else:
                    c.append(b[j])
                    j+=1
                    inv += len(a) - i
            if len(a) == i:
                c += b[j:]
            else:
                c += a[i:]
            return [c, inv]

        def mergesort(x):
            inv = 0
            if len(x) == 0 or len(x) == 1:
                return [x, inv, 0]
            else:
                middle = len(x) / 2
                l = 1 if x[middle-1]>x[middle] else 0
                [a, inv1, l1] = mergesort(x[:middle])
                [b, inv2, l2] = mergesort(x[middle:])
                [c, inv] = merge(a, b)
                return [c, inv+inv1+inv2, l+l1+l2]

        [c, g, l] = mergesort(A)
        print l, g, c
        return l==g

print Solution().isIdealPermutation([0,5,2,3,4,1,6])

print Solution().isIdealPermutation([1,0,2])
print Solution().isIdealPermutation([1,2,0])
