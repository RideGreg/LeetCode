# Time:  O(n^2)， n指的是 expression 的长度。每个表达式只计算一次，但在计算过程中可能要搜索整个范围。
# Space: O(n^2)，在进行中间求值时，我们可以将 O(N)个新字符串传递给 evaluate 函数，每个字符串的长度为 O(N)。通过优化，
# 可以将总空间复杂度降低到 O(N)。

# 736
# You are given a string expression representing a Lisp-like expression to return the integer value of.
#
# The syntax for these expressions is given as follows.
#
# An expression is either an integer, a let-expression,
# an add-expression, a mult-expression, or an assigned variable.
# Expressions always evaluate to a single integer.
# (An integer could be positive or negative.)
# A let-expression takes the form (let v1 e1 v2 e2 ... vn en expr),
# where let is always the string "let", then there are 1 or more pairs of alternating variables and expressions,
# meaning that the first variable v1 is assigned the value of the expression e1,
# the second variable v2 is assigned the value of the expression e2,
# and so on sequentially; and then the value of this let-expression is the value of the expression expr.
# An add-expression takes the form (add e1 e2) where add is always the string "add",
# there are always two expressions e1, e2,
# and this expression evaluates to the addition of the evaluation of e1 and the evaluation of e2.
# A mult-expression takes the form (mult e1 e2) where mult is always the string "mult",
# there are always two expressions e1, e2,
# and this expression evaluates to the multiplication of the evaluation of e1 and the evaluation of e2.
# For the purposes of this question, we will use a smaller subset of variable names.
# A variable starts with a lowercase letter, then zero or more lowercase letters or digits.
# Additionally for your convenience,
# the names "add", "let", or "mult" are protected and will never be used as variable names.
# Finally, there is the concept of scope.
# When an expression of a variable name is evaluated,
# within the context of that evaluation,
# the innermost scope (in terms of parentheses) is checked first for the value of that variable,
# and then outer scopes are checked sequentially. It is guaranteed that every expression is legal.
# Please see the examples for more details on scope.
#
# Evaluation Examples:
# Input: (add 1 2)
# Output: 3
#
# Input: (mult 3 (add 2 3))
# Output: 15
#
# Input: (let x 2 (mult x 5))
# Output: 10
#
# Input: (let x 2 (mult x (let x 3 y 4 (add x y))))
# Output: 14
# Explanation: In the expression (add x y), when checking for the value of the variable x,
# we check from the innermost scope to the outermost in the context of the variable we are trying to evaluate.
# Since x = 3 is found first, the value of x is 3.
#
# Input: (let x 3 x 2 x)
# Output: 2
# Explanation: Assignment in let statements is processed sequentially.
#
# Input: (let x 1 y 2 x (add x y) (add x y))
# Output: 5
# Explanation: The first (add x y) evaluates as 3, and is assigned to x.
# The second (add x y) evaluates as 3+2 = 5.
#
# Input: (let x 2 (add (let x 3 (let x 4 x)) x))
# Output: 6
# Explanation: Even though (let x 4 x) has a deeper scope, it is outside the context
# of the final x in the add-expression.  That final x will equal 2.
#
# Input: (let a1 3 b2 (add a1 1) b2)
# Output 4
# Explanation: Variable names can contain digits after the first character.
#
# Note:
# - The given string expression is well formatted:
#   There are no leading or trailing spaces,
#   there is only a single space separating different components of the string,
#   and no space between adjacent parentheses.
#   The expression is guaranteed to be legal and evaluate to an integer.
# - The length of expression is at most 2000. (It is also non-empty, as that would not be a legal expression.)
# - The answer and all intermediate calculations of that answer are guaranteed to fit in a 32-bit integer.


# 括号套用栈来表示
# 变量表:用lookup表示从变量名到变量值之间的映射。考虑到变量作用域，栈中每一层的let函数都有个独立变量表lookup，查找时优先从内层查找。
#
# 词法分析和语法分析:
# 词法分析很简单，左括号和右括号是特殊符号，除此之外的字符都用括号或空格分隔成单词，一个单词可能是函数名、变量名或数字，
# 左括号后第一个单词是函数名，以数字或负号开头为数字。
#
# 每起一个左括号，就开始数这是第几个参数，参数可能是单词也可能是嵌套括号，那么在遇到单词时和遇到右括号（除了最后一个右括号）时
# 都应该填一个参数进来。
#
# 加法和乘法比较简单，数够两个参数就行。比较复杂的是let，他的参数比较特殊，第奇数个参数可能是变量名，也可能是最终返回值。
# 当第奇数个参数是变量名时，还应该注意变量名后是否还有参数，那么这个变量名其实是返回值。例如(let x 8 x)中最后一个x其实是返回值，
# 他和(let x 8 x 9 10)中第二个x的意义完全不同。
class Solution(object):
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        def getval(lookup, x): # if x is variable, return its value; otherwise x is an int, return int
            return lookup.get(x, x)

        def evaluate(tokens, lookup):
            if tokens[0] in ('add', 'mult'):
                a, b = map(int, map(lambda x: getval(lookup, x), tokens[1:]))
                return str(a+b if tokens[0] == 'add' else a*b)
            for i in range(1, len(tokens)-1, 2):
                if tokens[i+1]:
                    lookup[tokens[i]] = getval(lookup, tokens[i+1])
            return getval(lookup, tokens[-1])

        tokens, lookup, stk = [''], {}, []
        for c in expression:
            if c == '(': # push stack
                if tokens[0] == 'let':
                    evaluate(tokens, lookup)
                stk.append((tokens, dict(lookup)))
                tokens =  ['']
            elif c == ' ':
                tokens.append('')
            elif c == ')': # pop stack
                val = evaluate(tokens, lookup)
                tokens, lookup = stk.pop()
                tokens[-1] += val
            else:
                tokens[-1] += c
        return int(tokens[0])


# 难点是如何管理变量的正确范围。我们可以用栈来存放变量和值的对应关系，当进入变量作用的括号范围时，就将变量和值的哈希映射
# 添加到栈中，当出括号内时，就弹出栈顶元素。
#
# evaluate 方法会检查每个表达式 expression 采用的形式:
# 如果 expression 是数字开头，则它是一个整数：返回它。
# 如果 expression 以字母开头，则它是一个变量。则检查该变量的作用域。
# 否则我们将 expression 中的标记（变量或表达式）分组，通过计算 bal = '(' 的数量减去 ')' 的数量，当 bal 为零时，
# 则我们得到一个标记。举个例子：(add 1 (add 2 3)) 可以获得两个标记 '1' 和 '(add 2 3)'。
# 计算每个标记并返回它们的加法或乘法得结果。
# 对于 let 表达式，按顺序计算每个表达式并将其值分配给当前作用域中的变量，然后返回对最终表达式的求值。
#
def implicit_scope(func):
    def wrapper(*args):
        args[0].scope.append({})
        ans = func(*args)
        args[0].scope.pop()
        return ans
    return wrapper

class Solution_leetcode_cn_official(object):
    def __init__(self):
        self.scope = [{}]

    @implicit_scope
    def evaluate(self, expression):
        if not expression.startswith('('):
            if expression[0].isdigit() or expression[0] == '-':
                return int(expression)
            for local in reversed(self.scope):
                if expression in local: return local[expression]

        tokens = list(self.parse(expression[5 + (expression[1] == 'm'): -1]))
        if expression.startswith('(add'):
            return self.evaluate(tokens[0]) + self.evaluate(tokens[1])
        elif expression.startswith('(mult'):
            return self.evaluate(tokens[0]) * self.evaluate(tokens[1])
        else:
            for j in range(1, len(tokens), 2):
                self.scope[-1][tokens[j-1]] = self.evaluate(tokens[j])
            return self.evaluate(tokens[-1])

    def parse(self, expression):
        bal = 0
        buf = []
        for token in expression.split():
            bal += token.count('(') - token.count(')')
            buf.append(token)
            if bal == 0:
                yield " ".join(buf)
                buf = []
        if buf:
            yield " ".join(buf)

print(Solution().evaluate("(add 1 2)")) # 3
print(Solution().evaluate("(mult 3 (add 2 3))")) # 15
print(Solution().evaluate("(let x 2 (mult x 5))")) # 10
print(Solution().evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))")) # 14
print(Solution().evaluate("(let x 3 x 2 x)")) # 2
print(Solution().evaluate("(let x 1 y 2 x (add x y) (add x y))")) # 5
# The first (add x y) evaluates as 3, and is assigned to x.
# The second (add x y) evaluates as 3+2 = 5.
#
print(Solution().evaluate("(let x 2 (add (let x 3 (let x 4 x)) x))")) # 6
print(Solution().evaluate("(let x 2 (add (let x 3 4) x))")) # 6
# Even though (let x 4 x) has a deeper scope, it is outside the context
# of the final x in the add-expression.  That final x will equal 2. Ans = 4+x = 4+2

print(Solution().evaluate("(let a1 3 b2 (add a1 1) b2)")) # 4
