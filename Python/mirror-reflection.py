# Time:  O(1)
# Space: O(1)

# There is a special square room with mirrors on each of the four walls.
# Except for the southwest corner, there are receptors on each of
# the remaining corners,
# numbered 0, 1, and 2.
#
# The square room has walls of length p,
# and a laser ray from the southwest corner first meets
# the east wall at a distance q from the 0th receptor.
#
# Return the number of the receptor that the ray meets first.
# (It is guaranteed that the ray will meet a receptor eventually.)
#
# Example 1:
#
# Input: p = 2, q = 1
# Output: 2
# Explanation: The ray meets receptor 2 the first time it gets reflected back
# to the left wall.
#
# Note:
# - 1 <= p <= 1000
# - 0 <= q <= p


class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        # p&-p gets the last-set-bit of p. The last-set-bit of odd number (xxx1) is less than than last-set-bit of even number
        # (p & -p) > (q & -q) means p even and q odd, thus gcd(p,q) odd, so p/gcd(p,q) even (# of reflections on p-axis) and q/gcd(p,q) odd
        # (p & -p) < (q & -q) means p odd and q even, thus gcd(p,q) odd, so q/gcd(p,q) even (# of reflections on q-axis) and p/gcd(p,q) odd
        # (p & -p) == (q & -q) means either both p and q odd, thus gcd(p,q) odd, so p/gcd(p,q) and q/gcd(p,q) both odd; or
        #                      p and q are the same even number, so arrive receptor #1.
        # ----------------
        # np\nq  odd  even
        #  odd    1     0
        #  even   2     N (stopped before reach this)
        # ------------------
        return 2 if (p & -p) > (q & -q) else 0 if (p & -p) < (q & -q) else 1


# Time:  O(log(max(p, q))) the complexity of gcd operation
# Space: O(1)
'''
Instead of modelling the ray as a bouncing line, model it as a straight line through reflections of the room.
For example, if p = 2, q = 1, then we can reflect the room horizontally, and draw a straight line from (0, 0)
to (4, 2). The ray meets the receptor 2, which was reflected from (0, 2) to (4, 2).
In general, the ray goes to the first integer point (kp, kq) where k is an integer, and kp and kq are multiples
of p. Thus, the goal is to find the smallest k for which kq is a multiple of p. k=p obviously makes the equation
but it is not the smallest. The mathematical answer is smallest k = p / gcd(p,q), so kq is a multiple of p.

Then # of reflection on p-axis np = kp/p = k = p /gcd(p,q); # of flection on q-axis is kq/p = q/gcd(p,q).
----------------
np\nq  odd  even
 odd    1     0
 even   2     N (stopped before reach this)
------------------

N---0---N---0---N
|   |   |   |   |
N---1---2---N---2
|   |   |   |   |
N---0---N---0---N
|   |   |   |   |
2---1---2---1---2
|   |   |   |   |
 ---0---N---N---N
'''
class Solution2(object):
    def mirrorReflection(self, p, q):  # USE THIS
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        g = gcd(p, q)
        np = (p / g) % 2   # k % 2
        nq = (q / g) % 2   # (kq / p) % 2 and k = p/g

        return 1 if np and nq else 0 if np else 2

'''
Time O(p) number of bounces is p/gcd(p,q) bounded by p.
Space O(1)

Intuition
The initial ray can be described as going from an origin (x, y) = (0, 0) in the direction (rx, ry) = (p, q).
From this, we can figure out which wall it will meet and where, and what the appropriate new ray will be
(based on reflection.) We keep simulating the ray until it finds it's destination.

Algorithm
The parameterized position of the laser after time t will be (x + rx * t, y + ry * t). From there,
we know when it will meet the east wall (if x + rx * t == p), and so on. For a positive (and nonnegligible)
time t, it meets the next wall.

We can then calculate how the ray reflects. If it hits an east or west wall, then rx *= -1, else ry *= -1.
'''
class Solution3(object):
    def mirrorReflection(self, p, q):
        from fractions import Fraction as F

        x = y = 0
        rx, ry = p, q
        targets = [(p, 0), (p, p), (0, p)]

        while (x, y) not in targets:
            #Want smallest t so that some x + rx, y + ry is 0 or p
            #x + rx*t = 0, then t = -x/rx etc.
            t = float('inf')
            for v in [F(-x,rx), F(-y,ry), F(p-x,rx), F(p-y,ry)]:
                if v > 0: t = min(t, v)

            x += rx * t
            y += ry * t

            #update rx, ry
            if x == p or x == 0: # bounced from east/west wall, so reflect on y axis
                rx *= -1
            if y == p or y == 0:
                ry *= -1

        return 1 if x==y==p else 0 if x==p else 2