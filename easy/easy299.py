'''
299. 猜数字游戏
你正在和你的朋友玩 猜数字（Bulls and Cows）游戏：你写下一个数字让你的朋友猜。每次他猜测后，你给他一个提示，
告诉他有多少位, 数字和确切位置都猜对了（称为“Bulls”, 公牛），有多少位数字猜对了但是位置不对（称为“Cows”, 奶牛）。
你的朋友将会根据提示继续猜，直到猜出秘密数字。

请写出一个根据秘密数字和朋友的猜测数返回提示的函数，用 A 表示公牛，用 B 表示奶牛。

请注意秘密数字和朋友的猜测数都可能含有重复数字。

示例 1:

输入: secret = "1807", guess = "7810"

输出: "1A3B"

解释: 1 公牛和 3 奶牛。公牛是 8，奶牛是 0, 1 和 7。
示例 2:

输入: secret = "1123", guess = "0111"

输出: "1A1B"

解释: 朋友猜测数中的第一个 1 是公牛，第二个或第三个 1 可被视为奶牛。
说明: 你可以假设秘密数字和朋友的猜测数都只包含数字，并且它们的长度永远相等。

思路：　因为secret和guess的长度总是相同，可以较容易得到位置和数字都正确的个数，然后适用dict来统计数字在两个字符串中出现的频率，如果两个dict有相同
的数组出现，取出现个数少的那个，同时别忘记减去位置和数组都正确的个数
'''


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        has_dict = dict()
        has_dict_guess = dict()
        A = 0
        B = 0
        for se in secret:
            if se in has_dict.keys():
                has_dict[se] += 1
            else:
                has_dict[se] = 1
        for index, gu in enumerate(guess):
            if gu == secret[index]:
                A += 1
            if gu in has_dict_guess.keys():
                has_dict_guess[gu] += 1
            else:
                has_dict_guess[gu] = 1
        for key, value in has_dict_guess.items():
            if key in has_dict.keys():
                B += min(has_dict[key], value)
        return "%dA%dB" % (A, B - A)



so = Solution()

examples = [
    {"secret": "1807", "guess": "7810", "result": "1A3B"},
    {"secret": "1123", "guess": "0111", "result": "1A1B"},
]

for exa in examples:
    result = so.getHint(exa["secret"], exa["guess"])
    print(result == exa["result"])
