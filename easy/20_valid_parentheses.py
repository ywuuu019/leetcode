class Solution:
    def isValid(self, s: str) -> bool:
        # 關鍵在於，最後一個進來的，一定要能跟下一個配對
        # 迴圈走每個字元，如果是([{就加到stack裡面
        # 如果字原是)]}，就比對stack最後的字元，是不是對應的字元，如果是就pop
        # 如果都不是這六種字元，就return false.
        # 如果stack最後不等於0, return false; 等於0 return true.
        ### 我的解法 ###
        stack = []
        dict = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for char in s:
            # print(char)
            # print(stack)
            if char in dict.keys():
                stack.append(char)
            elif char in dict.values():
                # "not stack" means: stack is empty
                # python有個神奇的功能，可以從後開始取值，所以[-1]就是最後一個
                if stack and char != dict[stack[-1]]:  # 確保不會list index out of range
                    return False
                elif not stack:
                    return False
                else:
                    stack.pop()
            else:
                return False


        if len(stack) == 0:
            return True
        else:
            return False

        ### 別人的解法 ###
        # stack = []
        # dict = {"]": "[", "}": "{", ")": "("}
        # for char in s:
        #     if char in dict.values():
        #         stack.append(char)
        #     elif char in dict.keys():
        #         # 前面成立，後面就不會去計算了(short-circuiting),所以不用擔心index out of range
        #         if stack == [] or dict[char] != stack.pop():  # 這行就會執行pop
        #             return False
        #     else:
        #         return False
        # return stack == []  # 判斷stack是不是0，很精簡的寫法


if __name__ == '__main__':
    my_ans = Solution()
    # print(my_ans.isValid("()"))      # True
    print(my_ans.isValid("())"))  # False
    # print(my_ans.isValid("([)]"))    # False
    # print(my_ans.isValid("()[]{}"))  # True
    # print(my_ans.isValid("([{}])"))  # True
    # print(my_ans.isValid("([{)])"))  # False
