class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        if ( len(s) == 1 ):
            return roman[s[0]]

        # range(10)：產生從0到9的整數序列。
        # range(1, 11)：產生從1到10的整數序列(未指定遞增值的情況下，其遞增值預設為1)。

        # 其實邏輯滿簡單的，只要右邊的數比我大，我就要被減，
        # 其餘情況我都是被加。
        # print(s)
        # print(s[0])
        # print(roman["D"])  #500
        # print( roman[s[0]] )  #1000

        result = 0
        for i in range(len(s)):
            # print("i=", i)
            # print(roman[s[i]])
            if i+1 < len(s):
                if roman[s[i]] < roman[s[i+1]]:
                    result = result - roman[s[i]]
                else:
                    result = result + roman[s[i]]
            else:
                result = result + roman[s[i]]
        return result

if __name__ == '__main__':
    my_ans = Solution()
    print(my_ans.romanToInt("MCMXCIV"))