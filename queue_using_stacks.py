class MyQueue:
        
    def __init__(self):
    
        self.master = []
        self.slave = []

    def push(self, x: int) -> None:
        if not self.master:
            while len(self.slave):           
                self.master.append(self.slave.pop())   
        self.master.append(x)             

    def pop(self) -> int:     
        if not self.slave:
            while len(self.master):            
                self.slave.append(self.master.pop())
        return self.slave.pop()

    def peek(self) -> int:
        if not self.slave:
            while len(self.master):            
                self.slave.append(self.master.pop())
        return self.slave[-1]

    def empty(self) -> bool:

        return len(self.master) + len(self.slave) == 0
     
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


