'''
925. 长按键入
你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。
示例 1：
输入：name = "alex", typed = "aaleex"
输出：true
解释：'alex' 中的 'a' 和 'e' 被长按。
示例 2：
输入：name = "saeed", typed = "ssaaedd"
输出：false
解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。
示例 3：
输入：name = "leelee", typed = "lleeelee"
输出：true
示例 4：
输入：name = "laiden", typed = "laiden"
输出：true
解释：长按名字中的字符并不是必要的。
提示：
name.length <= 1000
typed.length <= 1000
name 和 typed 的字符都是小写字母。
'''


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:  # 计算两个字符串相连相同字符的个数
        def _get_count(ss):
            start = 0
            before = 0
            record = []
            length = len(ss)
            while start < length:
                if ss[start] == ss[before]:
                    start += 1
                else:
                    record.append([ss[before], start - before])
                    before = start
            record.append([ss[before], start - before])
            return record

        r1 = _get_count(name)
        r2 = _get_count(typed)
        if len(r1) != len(r2):
            return False
        for index, rr in enumerate(r1):
            if rr[0] != r2[index][0] or rr[1] > r2[index][1]:
                return False
        return True

so = Solution()

print(so.isLongPressedName("alex", "aaleex") == True)
print(so.isLongPressedName("saeed", "ssaaedd") == False)
print(so.isLongPressedName("leelee", "lleeelee") == True)
print(so.isLongPressedName("laiden", "laiden") == True)