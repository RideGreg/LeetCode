# Time:  O((n - m) * m), where M, N are the lengths of stamp, target
# Space: O((n - m) * m)

# 936
# You want to form a target string of lowercase letters.
#
# At the beginning, your sequence is target.length '?' marks.  You also have a stamp of lowercase letters.
#
# On each turn, you may place the stamp over the sequence, and replace every letter in the sequence with the
# corresponding letter from the stamp.  You can make up to 10 * target.length turns.
#
# For example, if the initial sequence is "?????", and your stamp is "abc",  then you may make "abc??",
# "?abc?", "??abc" in the first turn.  (Note that the stamp must be fully contained in the boundaries of
# the sequence in order to stamp.)
#
# If the sequence is possible to stamp, then return an array of the index of the left-most letter being
# stamped at each turn.  If the sequence is not possible to stamp, return an empty array.
#
# For example, if the sequence is "ababc", and the stamp is "abc", then we could return the answer [0, 2],
# corresponding to the moves "?????" -> "abc??" -> "ababc".
#
# Also, if the sequence is possible to stamp, it is guaranteed it is possible to stamp within 10 * target.length
# moves.  Any answers specifying more than this number of moves will not be accepted.
#
# Example 1:
# Input: stamp = "abc", target = "ababc"
# Output: [0,2]
# ([1,0,2] would also be accepted as an answer, as well as some other answers.)

# Solution: Work Backwards
# From the final position target, we will make those moves in reverse order.
#
# Let's call the ith window, a subarray of target of length stamp.length that starts at i. Each move at
# position i is possible if the ith window matches the stamp. After, every character in the window becomes
# a wildcard that can match any character in the stamp.
#
# For example, say we have stamp = "abca" and target = "aabcaca". Working backwards, we will reverse stamp
# at window 1 to get "a????ca", then reverse stamp at window 3 to get "a??????", and finally reverse stamp
# at position 0 to get "???????".
#
# Algorithm
# Keep track of *every window*. We want to know how many cells initially match the stamp (our "made" list),
# and which ones don't (our "todo" list). Any windows that are ready (ie. have no todo list), get enqueued.
#
# Specifically, we enqueue the positions of each character. (To save time, we enqueue by character,
# not by window.) This represents that the character is ready to turn into a "?" in our working target string.
#
# Now, how to process characters in our queue? For each character, let's look at all the windows that
# intersect it, and update their todo lists by removing the processed (queued) char from todo list.
# If any todo lists become empty in this manner (window.todo is empty),
# then we enqueue the characters in window.made that we haven't processed yet.

import collections


class Solution(object):
    def movesToStamp(self, stamp, target):
        def appendAndClean(i, made):
            ans.append(i)
            for m in made:
                if not done[m]:
                    q.append(m)
                    done[m] = True


        M, N = len(stamp), len(target)
        q = collections.deque()
        done = [False]*N
        ans = []
        A = [] # A[i] will contain info on what are matched and what are not for window i
        for i in xrange(N-M+1):
            # For each window [i, i+M),
            made, todo = set(), set()
            for j, c in enumerate(stamp):
                if c == target[i+j]:
                    made.add(i+j)
                else:
                    todo.add(i+j)
            A.append((made, todo))

            # If we can reverse stamp at i immediately,
            # enqueue letters from this window.
            if not todo:
                appendAndClean(i, made)

        # For each enqueued letter,
        while q:
            i = q.popleft()

            # For each window that is potentially affected,
            # j: start of window
            for j in xrange(max(0, i-M+1), min(N-M, i)+1):
                made, todo = A[j]
                if i in todo:  # This window needs update
                    todo.discard(i) # Remove it from todo list of this window
                    if not todo:  # Todo list of this window is empty
                        appendAndClean(j, made)

        return ans[::-1] if all(done) else []


print(Solution().movesToStamp("abc", "ababc")) # [0,2]
print(Solution().movesToStamp("abca", "aabcaca")) # [3,0,1]