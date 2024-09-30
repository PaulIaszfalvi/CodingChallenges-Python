class CustomStack:

    def __init__(self, maxSize: int):
        self.maximum = maxSize
        self.size = 0
        self.stack = []

    def push(self, x: int) -> None:
        if self.size < self.maximum:
            self.stack.append(x)
            self.size += 1        

    def pop(self) -> int:
        if self.size == 0:
            return -1

        self.size -= 1
        return self.stack.pop()        

    def increment(self, k: int, val: int) -> None:
        count = 0

        if k < self.size:
            count = k
        else:
            count = self.size

        for x in range(count):
            self.stack[x] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
