# Time:  O(n + m + z), n is the total size of patterns (words)
#                    , m is the total size of query string (text)
#                    , z is the number of all matched strings
# Space: O(t), t is the total size of ac automata trie

# 1065
# Given a text string and words (a list of strings), return all index pairs [i, j] so that
# the substring text[i]...text[j] is in the list of words.

# Input: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
# Output: [[3,7],[9,13],[10,17]]

# Input: text = "ababa", words = ["aba","ab"]
# Output: [[0,1],[0,2],[2,3],[2,4]]

# It's guaranteed that all strings in words are different.
# 1 <= text.length <= 100
# 1 <= words.length <= 20
# 1 <= words[i].length <= 50
# Return the pairs [i,j] in sorted order

# Hint: For each string of the set, look for matches and store those matches indices.

import collections

class TrieNode(object):
    def __init__(self):
        self.is_string = False
        self.children = collections.defaultdict(TrieNode)

class Solution(object): # USE THIS
    def indexPairs(self, text, words):
        trie = TrieNode()
        for w in words:
            p = trie
            for c in w:
                p = p.children[c]
            p.is_string = True

        ans = []
        for i in range(len(text)):
            p = trie
            for j in range(i, len(text)):
                p = p.children.get(text[j], None)
                if p is None: break
                if p.is_string:
                    ans.append([i, j])
        return ans

class AhoNode(object):
    def __init__(self):
        self.children = collections.defaultdict(AhoNode)
        self.indices = []
        self.suffix = None
        self.output = None


class AhoTrie(object):

    def step(self, letter):
        while self.__node and letter not in self.__node.children:
            self.__node = self.__node.suffix
        self.__node = self.__node.children[letter] if self.__node else self.__root
        return self.__get_ac_node_outputs(self.__node)
    
    def __init__(self, patterns):
        self.__root = self.__create_ac_trie(patterns)
        self.__node = self.__create_ac_suffix_and_output_links(self.__root)
    
    def __create_ac_trie(self, patterns):  # Time:  O(n), Space: O(t)
        root = AhoNode()
        for i, pattern in enumerate(patterns):
            node = root
            for c in pattern:
                node = node.children[c]
            node.indices.append(i)
        return root

    def __create_ac_suffix_and_output_links(self, root):  # Time:  O(n), Space: O(t)
        queue = collections.deque()
        for node in root.children.values():
            queue.append(node)
            node.suffix = root

        while queue:
            node = queue.popleft()
            for c, child in node.children.items():
                queue.append(child)
                suffix = node.suffix
                while suffix and c not in suffix.children:
                    suffix = suffix.suffix
                child.suffix = suffix.children[c] if suffix else root
                child.output = child.suffix if child.suffix.indices else child.suffix.output
                
        return root

    def __get_ac_node_outputs(self, node):  # Time:  O(z)
        result = []
        for i in node.indices:
            result.append(i)
        output = node.output
        while output:
            for i in output.indices:
                result.append(i)
            output = output.output
        return result
    

class Solution2(object):
    def indexPairs(self, text, words):
        """
        :type text: str
        :type words: List[str]
        :rtype: List[List[int]]
        """
        result = []
        reversed_words = [w[::-1] for w in words]
        trie = AhoTrie(reversed_words)
        for i in reversed(range(len(text))):
            for j in trie.step(text[i]):
                result.append([i, i+len(reversed_words[j])-1])
        result.reverse()
        return result

print(Solution().indexPairs("thestoryofleetcodeandme", ["story","fleet","leetcode"])) # [[3,7],[9,13],[10,17]]
print(Solution().indexPairs("ababa", ["aba","ab"])) # [[0,1],[0,2],[2,3],[2,4]]