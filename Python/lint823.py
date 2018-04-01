class Solution:
    """
    @param inputA: Input stream A
    @param inputB: Input stream B
    @return: The answer
    """
    def inputStream(self, inputA, inputB):
        A,B = [], []
        for a in inputA:
            if a != '<':
                A.append(a)
            else:
                if A:
                    A.pop()
        for b in inputB:
            if b != '<':
                B.append(b)
            else:
                if B:
                    B.pop()
        return 'YES' if A==B else 'NO'

print Solution().inputStream("abcde<<", "abcd<e<")
print Solution().inputStream("a<<bc", "abc<<")