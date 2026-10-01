class MinStack():
    def __init__(self):
        self.values = []
        self.mins = []
        
    def push(self, val):
        if not self.mins:
            cur_min = val
        else:
            cur_min = min(self.mins[-1], val)
        self.mins.append(cur_min)
        self.values.append(val)

    def pop(self):
        if self.is_empty():
            return None
        self.mins.pop()
        return self.values.pop()
    
    def top(self):
        if self.is_empty():
            return None
        return self.values[-1]
    
    def is_empty(self):
        return not self.values
    
    def getMin(self):
        if self.is_empty():
            return None
        else:
            return self.mins[-1]

def test_min_stack():
    stack = MinStack()

    stack.push(-2)
    stack.push(0)
    stack.push(-3)

    print(stack.getMin())  # expected: -3

    stack.pop()

    print(stack.top())     # expected: 0
    print(stack.getMin())  # expected: -2


test_min_stack()