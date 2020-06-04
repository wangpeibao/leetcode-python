'''
859. 亲密字符串
给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，就返回 true ；否则返回 false 。
示例 1：
输入： A = "ab", B = "ba"
输出： true
示例 2：
输入： A = "ab", B = "ab"
输出： false
示例 3:
输入： A = "aa", B = "aa"
输出： true
示例 4：
输入： A = "aaaaaaabc", B = "aaaaaaacb"
输出： true
示例 5：
输入： A = "", B = "aa"
输出： false
提示：
0 <= A.length <= 20000
0 <= B.length <= 20000
A 和 B 仅由小写字母构成。
'''


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        # 长度得相同
        if len(A) != len(B):
            return False
        # 存在不同字母
        dif = []
        for i in range(len(A)):
            if A[i] != B[i]:
                dif.append(i)
        if len(dif) == 0:
            if len(set(list(A))) < len(A):
                return True
            return False
        elif len(dif) != 2:
            return False
        # 进行变换之后相等
        if A[dif[0]] == B[dif[1]] and A[dif[1]] == B[dif[0]]:
            return True
        return False

so = Solution()

print(so.buddyStrings("ab", "ba") == True)
print(so.buddyStrings("ab", "ab") == False)
print(so.buddyStrings("aa", "aa") == True)
print(so.buddyStrings("aaaaaaabc", "aaaaaaacb") == True)
print(so.buddyStrings("", "aa") == False)
