'''
443. 压缩字符串
给定一组字符，使用原地算法将其压缩。
压缩后的长度必须始终小于或等于原数组长度。
数组的每个元素应该是长度为1 的字符（不是 int 整数类型）。
在完成原地修改输入数组后，返回数组的新长度。
进阶：
你能否仅使用O(1) 空间解决问题？
示例 1：
输入：
["a","a","b","b","c","c","c"]

输出：
返回6，输入数组的前6个字符应该是：["a","2","b","2","c","3"]

说明：
"aa"被"a2"替代。"bb"被"b2"替代。"ccc"被"c3"替代。
示例 2：

输入：
["a"]

输出：
返回1，输入数组的前1个字符应该是：["a"]

说明：
没有任何字符串被替代。
示例 3：

输入：
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

输出：
返回4，输入数组的前4个字符应该是：["a","b","1","2"]。

说明：
由于字符"a"不重复，所以不会被压缩。"bbbbbbbbbbbb"被“b12”替代。
注意每个数字在数组中都有它自己的位置。
'''


class Solution:
    def compress(self, chars) -> int:  # 双指针法
        length = len(chars)
        slow = 0
        offset = 0
        while slow < length - offset:
            fast = slow + 1
            count = 1
            self_offset = 0
            while fast < length - offset:
                if chars[fast] == chars[slow]:
                    count += 1
                    fast += 1
                else:
                    break
            if count > 1:
                count_list = list(str(count))
                for i in range(len(count_list)):
                    chars[slow + i + 1] = count_list[i]
                for i in range(slow + len(count_list) + 1, slow + count):
                    chars.pop(i - self_offset)
                    offset += 1
                    self_offset += 1
            slow = fast - self_offset
        return len(chars)


so = Solution()
print(so.compress(["a", "a", "b", "b", "c", "c", "c"]) == 6)
print(so.compress(["a"]) == 1)
print(so.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]) == 4)
print(so.compress(["a", "a", "a", "b", "b", "a", "a"]) == 6)
