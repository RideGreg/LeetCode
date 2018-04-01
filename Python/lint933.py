class Solution:
    """
    @param tuple: the tuple string
    @param n: an integer
    @return: the product of all the nth element in each array
    """
    def tupleMultiply(self, tuple, n):
        arr = tuple[1:-1].split('),(')
        import operator
        return reduce(operator.mul, [int(a.split(',')[n-1]) for a in arr])

print Solution().tupleMultiply("(1,2,3),(4,5,6),(7,8,9)", 2)
print Solution().tupleMultiply("(1,2,3),(4,5,6),(7,8,9)", 3)