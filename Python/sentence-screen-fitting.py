# Time:  O(r + n * c)
# Space: O(n)

# 418
# Given a rows x cols screen and a sentence represented by a list of words, find how many times
# the given sentence can be fitted on the screen.
#
# Note:
#
# A word cannot be split into two lines.
# The order of words in the sentence must remain unchanged.
# Two consecutive words in a line must be separated by a single space.
# Total words in the sentence won't exceed 100.
# Length of each word won't exceed 10.
# 1 ≤ rows, cols ≤ 20,000.

class Solution(object):
    # DP. 观察测试用例可以发现，当句子在屏幕上重复展现时，会呈现周期性的规律：
    # I-had
    # apple
    # pie-I
    # had--
    # apple
    # pie-I
    # had--
    # apple
    # 上例中apple单词的相对位置从第二行开始循环，因此只需要找到单词相对位置的“循环节”，即可将问题简化。
    #
    # 利用字典dp记录循环节的起始位置，具体记录方式为：dp[(pc, pw)] = pr, ans
    #    以数对(pc, pw)为键，其中pw为单词在句子中出现时的下标，pc为单词出现在屏幕上的列数
    #    以数对(pr, ans)为值，其中pr为单词出现在屏幕上的行数，ans为此时已经出现过的完整句子数
    def wordsTyping(self, sentence, rows, cols): # USE THIS
        wcount = len(sentence)
        wlens = list(map(len, sentence))
        slen = sum(wlens) + wcount
        dp = dict()
        pr = pc = pw = ans = 0
        while pr < rows:
            if (pc, pw) in dp:
                pr0, ans0 = dp[(pc, pw)]
                loop = (rows - pr0) // (pr - pr0)
                ans = ans0 + loop * (ans - ans0)
                pr = pr0 + loop * (pr - pr0)
                if pr >= rows:
                    break
            else:
                dp[(pc, pw)] = pr, ans

            # fast forward for wide screen, no need to record in dp, because if
            # there is 循环节 in fast forward, there must be 循环节 before it
            scount = (cols - pc) // slen
            ans += scount
            pc += scount * slen + wlens[pw]
            # pw: no need update for complete sentence, only update when current word can
            # be inserted. pr: no need update

            if pc <= cols:
                pc += 1 # space
                pw = (pw + 1) % wcount
                ans += (pw == 0)
            if pc >= cols: # wrap around
                pc = 0
                pr += 1
        return ans


    # count how many words can be put in screen.
    # Easy to understand. Not a method applicable to other repetition problem.
    def wordsTyping2(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        slen = sum(map(len, sentence)) + len(sentence)
        scount, remCols = divmod(cols, slen)
        ans = scount * rows # when cols is big, times for complete sentence

        def words_fit(start):
            if len(sentence[start]) > remCols:
                return 0

            l, count = len(sentence[start]), 1
            i = (start + 1) % len(sentence) # next index in circular
            while l + 1 + len(sentence[i]) <= remCols:
                l += 1 + len(sentence[i])
                count += 1
                i = (i + 1) % len(sentence)
            return count

        # for each word, how many words can fit in one line
        wc = list(map(words_fit, range(len(sentence))))

        words, start = 0, 0
        for _ in range(rows):
            words += wc[start]
            start = (start + wc[start]) % len(sentence) # start index in next line
        return ans + words // len(sentence)


    def wordsTyping_bruteForce(self, sentence, rows, cols):
        l = sum(map(len, sentence)) + len(sentence)
        cnt = (rows * cols + 1 ) // l
        rs, cs = 0, 0
        ans = 0
        for k in range(cnt):
            if rs < rows:
                for s in sentence:
                    if cs + len(s) - 1 > cols - 1: # the y coord > max coord
                        rs += 1
                        cs = 0
                        if rs >= rows:
                            break
                    cs += len(s)+1
                else:
                    ans += 1
        return ans

#print(Solution().wordsTyping(["I", "had", "apple", "pie"], 22, 5)) # 7
# I-had 0
# apple 1
# pie-I 2
# had-- 3
# apple 4
# pie-I 5
# had-- 6
# apple 7
# pie-I 8
# had-- 9
# apple 10
# pie-I 11
# had-- 12
# apple 13
# pie-I 14
# had-- 15
# apple 16
# pie-I 17
# had-- 18
# apple 19
# pie-I 20
# had-- 21
#print(Solution().wordsTyping(["I", "had", "apple", "pie"], 4, 53)) # 13
# I-had-apple-pie-I-had-apple-pie-I-had-apple-pie-I-had
# apple-pie-I-had-apple-pie-I-had-apple-pie-I-had-apple
# pie-I-had-apple-pie-I-had-apple-pie-I-had-apple-pie-I
# had-apple-pie-I-had-apple-pie-I-had-apple-pie-I-had--
#print(Solution().wordsTyping(["I", "had", "apple", "pie"], 4, 52)) # 12
# I-had-apple-pie-I-had-apple-pie-I-had-apple-pie-I---
# had-apple-pie-I-had-apple-pie-I-had-apple-pie-I-had-
# apple-pie-I-had-apple-pie-I-had-apple-pie-I-had-----
# apple-pie-I-had-apple-pie-I-had-apple-pie-I-had-----
print(Solution().wordsTyping(["I", "had", "apple", "pie"], 4, 48)) # 12
# I-had-apple-pie-I-had-apple-pie-I-had-apple-pie-
# I-had-apple-pie-I-had-apple-pie-I-had-apple-pie-
# I-had-apple-pie-I-had-apple-pie-I-had-apple-pie-
# I-had-apple-pie-I-had-apple-pie-I-had-apple-pie-
print(Solution().wordsTyping(["I", "had", "apple", "pie"], 4, 5)) # 1
# I-had
# apple
# pie-I
# had--
print(Solution().wordsTyping(["I", "had", "apple", "pie"], 6, 5)) # 2
# I-had
# apple
# pie-I
# had--
# apple
# pie-I

print(Solution().wordsTyping(["hello", "world"], 2, 8)) # 1
print(Solution().wordsTyping(["hello", "world"], 3, 8)) # 1
print(Solution().wordsTyping(["a", "bcd", "e"], 3, 5)) # 2
# a-bcd-
# e-a---
# bcd-e-
