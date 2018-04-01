class P(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Solution:
    """
    @param p: the point List
    @return: the numbers of pairs which meet the requirements
    """

    def pairNumbers(self, p):
        ee = eo = oe = oo = 0
        for pt in p:
            if pt.x % 2 and pt.y % 2:
                oo += 1
            elif pt.x % 2 and pt.y % 2 == 0:
                oe += 1
            elif pt.x % 2 == 0 and pt.y % 2:
                eo += 1
            else:
                ee += 1
        return sum(map(lambda a: a*(a-1)/2, [ee, eo, oe, oo]))

print Solution().pairNumbers([P(1,2), P(3,4), P(5,6)])