# Time:  O(n)
# Space: O(1)

# 1111 weekly contest 144 7/6/2019

# A string is a valid parentheses string (denoted VPS) if and only if it consists of
# "(" and ")" characters only, and:
#
#   - It is the empty string, or
#   - It can be written as AB (A concatenated with B), where A and B are VPS's, or
#   - It can be written as (A), where A is a VPS.

# We can similarly define the nesting depth depth(S) of any VPS S as follows:
# - depth("") = 0
# - depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's
# - depth("(" + A + ")") = 1 + depth(A), where A is a VPS.

# For example,  "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2),
# and ")(" and "(()" are not VPS's.
#
# Given a VPS seq, split it into two disjoint subsequences A and B, such that A and B
# are VPS's (and A.length + B.length = seq.length).
# Now choose any such A and B such that max(depth(A), depth(B)) is the minimum possible value.
#
# Return an answer array (of length seq.length) that encodes such a choice of A and B: 
# answer[i] = 0 if seq[i] is part of A, else answer[i] = 1.  Note that even though
# multiple answers may exist, you may return any of them.

# Solution:
# 通过栈实现括号匹配来计算嵌套深度：
# 维护一个栈 s，从左至右遍历括号字符串中的每一个字符：
# 如果当前字符是 (，就把 ( 压入栈中，此时这个 ( 的嵌套深度为栈的高度；
# 如果当前字符是 )，此时这个 ) 的嵌套深度为栈的高度，随后再从栈中弹出一个 (。
#
# 下面给出了括号序列 (()(())()) 在每一个字符处的嵌套深度：
# 括号序列   ( ( ) ( ( ) ) ( ) )
# 下标编号   0 1 2 3 4 5 6 7 8 9
# 嵌套深度   1 2 2 2 3 3 2 2 2 1
#
# 保证栈内一半的括号属于序列 A，一半的括号属于序列 B，那么就能保证拆分后最大的嵌套深度最小，是当前最大嵌套
# 深度的一半。要实现这样的对半分配，我们只需要把奇数层的 ( 分配给 A，偶数层的 ( 分配给 B 即可。
#
# 由于在这个问题中，栈中只会存放 (，因此我们不需要维护一个真正的栈，只需要用一个变量模拟记录栈的大小。

class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        ans, d = [], 0
        for c in seq:
            if c == '(':
                d += 1
                ans.append(d % 2)
            else:
                ans.append(d % 2)
                d -= 1
        return ans

    # 使用上面的例子 (()(())())，但这里我们把 ( 和 ) 的嵌套深度分成两行：
    # 括号序列   ( ( ) ( ( ) ) ( ) )
    # 下标编号   0 1 2 3 4 5 6 7 8 9
    # 嵌套深度   1 2 - 2 3 - - 2 - -
    # 嵌套深度   - - 2 - - 3 2 - 2 1
    # 规律是:
    # 左括号 ( 的下标编号与嵌套深度的奇偶性相反，也就是说：
    # 下标编号为奇数的 (，其嵌套深度为偶数，分配给 B；
    # 下标编号为偶数的 (，其嵌套深度为奇数，分配给 A。
    #
    # 右括号 ) 的下标编号与嵌套深度的奇偶性相同，也就是说：
    # 下标编号为奇数的 )，其嵌套深度为奇数，分配给 A；
    # 下标编号为偶数的 )，其嵌套深度为偶数，分配给 B。
    #
    # 只需要根据每个位置是哪一种括号以及该位置的下标编号，就能确定将对应的对应的括号分到哪个组了。

    def maxDepthAfterSplit2(self, seq):
        return [(i & 1) ^ (seq[i] == '(') for i, c in enumerate(seq)]

print(Solution().maxDepthAfterSplit("(()())")) # [1, 0, 0, 0, 0, 1]
print(Solution().maxDepthAfterSplit("()(())()")) # [1, 1, 1, 0, 0, 1, 1, 1]

