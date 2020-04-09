# Time:  O(n)
# Space: O(n)
# 71
# Given an absolute path for a file (Unix-style), simplify it.
#
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# click to show corner cases.
#
# Corner Cases:
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".
#

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        stack, tokens = [], path.split("/")
        for token in tokens:
            if token == "..":
                if stack:
                    stack.pop()
            elif token != "." and token:
                stack.append(token)
        return "/" + "/".join(stack)

    # follow up: Given current directory and change directory path, return final path. E.g.
    # Curent                 Change            Output
    # ------------------------------------------------------------
    # /                    /facebook           /facebook
    # /facebook/anin       ../abc/def          /facebook/abc/def
    # /facebook/instagram   ../../../../.      /

    # EDGE CASE: 1. If change starts with a / (absolute path), current has to be emptied.
    # 2. if change is empty, ask interviewer what to do? Go to home directory or treat as no change?
    # 3. current may contain '.' and '..' and need simplification, don't use current to initialize stack.
    def changePath(self, current: str, changed: str) -> str:
        if not changed:
            return current
        if changed[0] == "/":
            current = ""

        stack = []
        for token in (current + "/" + changed).split("/"):
            if token == "..":
                if stack:
                    stack.pop()
            elif token and token != ".":
                stack.append(token)
        return "/" + "/".join(stack)

if __name__ == "__main__":
    print(Solution().simplifyPath("/../")) # /
    print(Solution().simplifyPath("/home//foo/")) # /home/foo
    print(Solution().changePath("/a", "/facebook/temp/../")) # /facebook
    print(Solution().changePath("/facebook/instagram", "../../../../.")) # /