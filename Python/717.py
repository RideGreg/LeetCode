class Solution(object):
    def isOneBitCharacter(self, bits):
        def valid(s):
            print s
            if len(s) == 0:
                return True
            if s[-1] == 0 and valid(s[:-1]):
                return True
            if (s[-2:] == [1,0] or s[-2:] == [1,1]) \
                and valid(s[0:-2]):
                return True
            return False

        if len(bits) == 0 or bits[-1] == [1]:
            return False
        if len(bits) == 1:
            return True
        if bits[-2:] == [0,0]:
            return True
        return not valid(bits[:-2])

print Solution().isOneBitCharacter([1, 0, 0]) #true
print Solution().isOneBitCharacter([1, 1, 1, 0]) #false
print Solution().isOneBitCharacter([0, 1, 0]) #false

