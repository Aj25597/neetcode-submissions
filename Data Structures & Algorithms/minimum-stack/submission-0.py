class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        #Get top val of stack. If val is less than curr min, then append that, else append min
        if len(self.min_stack) == 0:
            #know it's the only element
            self.min_stack.append(val)
        else:
            curr_min = self.min_stack[len(self.min_stack)-1]
            if val < curr_min:
                self.min_stack.append(val)
            else:
                self.min_stack.append(curr_min)

        return None

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        return None

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.min_stack[(len(self.min_stack)-1)]
        
