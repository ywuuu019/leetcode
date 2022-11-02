from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # 只有前綴一樣就可以了
        # 1. 可以先從前兩個字串開始比，取得最大重疊的部分，再和第三個字串比。慢慢縮小重疊的部分。

        # print(len(strs))
        if len(strs) == 0 or strs[0] == "" :
          return ""

        # 方法1:
        shortest = min(strs, key=len)  # 直接取得list中，長度最小的字串，太強了吧
        # print(min("jdhesiq"))  # 若是這樣，則是取得自串中，英文字母最小的字
        # print(shortest[:3]) # print 012

        # 拿最短字串中的第一個字元，跟所有的字串比較(包含自己)
        for i, ch in enumerate(shortest):
            # print(i, ch)
            for other in strs:
                if other[i] != ch:
                    # print(other[i])
                    # print(shortest[:i])
                    if i == 0:
                        return ""
                    else:
                        return shortest[:i]

        return shortest
        # 方法2:
        # strs = sorted(strs, key=len)
        # for index, short_word_letter in enumerate(strs[0]):
        #     for other_words in strs[1:]:
        #         if other_words[index] != short_word_letter:
        #             return strs[0][:index]
        # return strs[0]


if __name__ == '__main__':
    my_ans = Solution()
    # print(my_ans.longestCommonPrefix(["flower","flow","flight"]))
    # print(my_ans.longestCommonPrefix(["a"]))
    print(my_ans.longestCommonPrefix(["flower","flower","flower","flower"]))
    # print(my_ans.longestCommonPrefix([""]))