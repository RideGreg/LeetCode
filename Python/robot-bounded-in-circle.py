# Time:  O(n)
# Space: O(1)

# 1041
# On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of
# three instructions:
#
# "G": go straight 1 unit;
# "L": turn 90 degrees to the left;
# "R": turn 90 degress to the right.
# The robot performs the instructions given in order, and repeats them forever.
#
# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.
#
# "GGLLGG" => True
# "GG" => False
# "GL" => True


# Solution:
# Starting at the origin and face north (0,1),
# after ONE sequence of instructions,
# - if chopper has position shift AND face the same direction, he will continue the shift in subsequent iterations!
# - if chopper either has no shift OR face a different direction, he will be in a circle!
# 1. if chopper return to the origin, he's in an obvious circle.
# 2. if chopper finishes with face not towards north,
# it will get back to the initial status in another one or three sequences.

class Solution(object):
    def isRobotBounded_lee215(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        directions = [[0, 1], [ 1, 0], [0, -1], [-1, 0]]
        x, y, i = 0, 0, 0
        for instruction in instructions:
            if instruction == 'R':
                i = (i+1) % 4
            elif instruction == 'L':
                i = (i-1) % 4
            else:
                x += directions[i][0]
                y += directions[i][1]
        return (x == 0 and y == 0) or i > 0

    # Check after for 4 loops, whether it goes back to the origin (it always faces north after 4 loops)
    # proof:
    # If there exists a circle in the plane such that the robot never leaves the circle, the robot must return
    # to a point he stayed before w/ same facing direction. Let's say after N turns, robot gets back to the origin.
    #
    # 1. At least must N%4==0. This is because the robot can only turn left or right, so after each instruction,
    # it will be +90 degree, or +180 degree, or +270 degree. In order to face the original direction
    # after N turns, N90%360=0 and N180%360=0, and N*270%360=0. Thus, N%4=0.
    # 2. At most 4 is enough. The minimum N should be 4. If the minimum N is 8, let's assume the robot arrives a position
    # which is not origin after 4 turns (for example, northwest to the origin). Now the robot facing north
    # and start new move, after another 4 turns, it will go further (further northwest) from origin.
    # It can't get back to origin anymore. Thus the minimum N should be 4.
    #
    # So we only need to check 4 loops.
    def isRobotBounded(self, instructions):
        directions = [[0, 1], [ 1, 0], [0, -1], [-1, 0]]
        x, y, i = 0, 0, 0
        for instruction in instructions * 4:
            if instruction == 'R':
                i = (i+1) % 4
            elif instruction == 'L':
                i = (i-1) % 4
            else:
                dx, dy = directions[i]
                x += dx
                y += dy
        return x == 0 and y == 0

    # it is WRONG to use Set to check whether passing the same position with same direction
    # e.g. GLGLGGLGL will pass (0,0) with North direction in the middle.
    def isRobotBounded_wrong(self, instructions: str) -> bool:
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)] # NWSE
        x = y = d = 0
        seen = {(x,y,d)}
        for c in instructions * 4:
            if c == 'G':
                dx, dy = dirs[d]
                x, y = x + dx, y + dy
            elif c == 'L':
                d = (d+1) % 4
            else:
                d = (d-1) % 4
            if (x,y,d) in seen:
                return True
            seen.add((x,y,d))
        return False