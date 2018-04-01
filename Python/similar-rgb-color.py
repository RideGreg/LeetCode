# Time:  O(1)
# Space: O(1)

'''
In the following, every capital letter represents some hexadecimal digit from 0 to f.

The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand.  For example, "#15c" is shorthand for the color "#1155cc".

Now, say the similarity between two colors "#ABCDEF" and "#UVWXYZ" is -(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2.

Given the color "#ABCDEF", return a 7 character color that is most similar to #ABCDEF,
and has a shorthand (that is, it can be represented as some "#XYZ"
'''
class Solution(object):
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        def rounding(color):
            q, r = divmod(int(color, 16), 17) #'11','22','33'... = 17*1, 17*2, 17*3...
            if r > 8: q += 1
            return '{:0>2x}'.format(17*q) # :>02 means right aligned, use '0' padding to length 2. https://pyformat.info/

        return '#' + \
                rounding(color[1:3]) + \
                rounding(color[3:5]) + \
                rounding(color[5:7])


    def similarRGB_ming(self, color):
        def getClosest(s):
            # can only be one of the strings less, equal, more than the MSB char
            if s[0]=='0':
                pool = ['ff','00','11']
            elif s[0]=='f':
                pool = ['ff','00','ee']
            else:
                pool = [s[0]*2]
                c = hex(int(s[0],16)-1)[2]
                pool.append(c*2)
                c = hex(int(s[0],16)+1)[2]
                pool.append(c*2)

            ret, minDiff = '', float('inf')
            for p in pool:
                diff = abs(int(s,16)-int(p,16))
                if diff < minDiff:
                    ret, minDiff = p, diff
            return ret

        return '#'+''.join(getClosest(color[x:x+2]) for x in range(1,7,2))

print Solution().similarRGB("#09f166") #11ee66
print Solution().similarRGB("#f0121f") #ee1122