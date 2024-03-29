class MyQueue:
    
    def __init__(self):
        self.s1 = []      

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        temp = self.s1[0]
        self.s1 = self.s1[1:]
        return temp
    
    # To make pop O(1)
    
    # while self.s1:
    #         self.s2.append(self.s1.pop())
    #     self.s1.append(x)
    #     while self.s2:
    #         self.s1.append(self.s2.pop())


    def peek(self) -> int:
        return self.s1[0]

    def empty(self) -> bool:
        return len(self.s1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()