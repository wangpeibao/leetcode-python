'''
5413. 重新排列句子中的单词  显示英文描述
「句子」是一个用空格分隔单词的字符串。给你一个满足下述格式的句子 text :
句子的首字母大写
text 中的每个单词都用单个空格分隔。
请你重新排列 text 中的单词，使所有单词按其长度的升序排列。如果两个单词的长度相同，则保留其在原句子中的相对顺序。
请同样按上述格式返回新的句子。
'''


class Solution:
    def arrangeWords1(self, text: str) -> str:  # 超出时间限制
        # 使用选择排序
        tlist = text.split(" ")
        result = ""
        while tlist:
            min_length = 10 ** 5 + 1
            min_index = -1
            for index, val in enumerate(tlist):
                if len(val) < min_length:
                    min_length = len(val)
                    min_index = index
            min_value = tlist.pop(min_index)
            if not result:
                result += min_value.title()
            else:
                result += " " + min_value.lower()
        return result

    def arrangeWords(self, text: str) -> str:  # 冒泡排序
        tlist = text.split(" ")
        tlist[0] = tlist[0].lower()
        sort_list = []
        for val in tlist:
            sort_list.append([val, len(val)])
        sort_list.sort(key=lambda x: x[1])
        result = ""
        for sl in sort_list:
            if not result:
                result += sl[0].title()
            else:
                result += " " + sl[0]
        return result




so = Solution()

print(so.arrangeWords("Leetcode is cool") == "Is cool leetcode")
print(so.arrangeWords("Keep calm and code on") == "On and keep calm code")
print(so.arrangeWords("To be or not to be") == "To be or to be not")
