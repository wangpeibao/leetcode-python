'''
剑指 Offer 09. 用两个栈实现队列
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )
示例 1：
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
提示：
1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用
'''

class CQueue:
    def __init__(self):  # python中没有栈，用数组实现
        self.stack1 = []  # 主存储结构
        self.stack2 = []  # 副存储

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)  # 向主存储添加元素即可

    def deleteHead(self) -> int:
        # 将stack1 pop 并存入stack2, pop掉stack2的第一位，然后再重新存入到stack1
        if len(self.stack1) == 0:
            return -1
        while self.stack1:
            self.stack2.append(self.stack1.pop(-1))
        val = self.stack2.pop(-1)
        while self.stack2:
            self.stack1.append(self.stack2.pop(-1))
        return val


# Your CQueue object will be instantiated and called as such:
obj = CQueue()
print(obj.deleteHead())
print(obj.appendTail(5))
print(obj.appendTail(2))
print(obj.deleteHead())
print(obj.deleteHead())