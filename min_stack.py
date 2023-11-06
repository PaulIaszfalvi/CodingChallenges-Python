class MinStack:

    # Solution 2
    
    
    def __init__(self):
        self.stack = []  # Main stack to store values
        self.min_stack = []  # Auxiliary stack to keep track of the minimum value

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]

    

    # Solution 1

    # def __init__(self):
    #     self.stack = []
    #     self.val = None
    #     self.min = False
    #     self.index = -1

    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     self.val = val
    #     self.index += 1
       
    # def pop(self) -> None:
    #     if len(self.stack) > 0:
    #         self.index -= 1
    #         return self.stack.pop()
                        
    # def top(self) -> int:
    #     if self.index > -1:
    #         return self.stack[self.index]

    # def getMin(self) -> int:
    #     return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()