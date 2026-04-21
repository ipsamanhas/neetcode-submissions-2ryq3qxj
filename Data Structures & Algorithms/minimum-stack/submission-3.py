class MinStack:

    # every solution should be in O(1)
    # this is why we cant use min() method from python

    def __init__(self):
        self.stack = []
        self.minStack = [] # will store the min value at every step
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val = min(val, self.minStack[-1])
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
