class MinStack:

    def __init__(self):
        self.min = 0
        self.min_stack = list()
        self.previous_min = list()
        self.helper_dict = dict()

    def push(self, val: int) -> None:
        if not val is None:
            self.min_stack.append(val)
            self.helper_dict[val] = 1 + self.helper_dict.get(val,0)
            # Check whether the val is smaller than self.min or if it is the first element
            if len(self.min_stack) == 1:
                self.min = val
            elif val < self.min:
                # We store the current self.min in previous_min
                self.previous_min.append(self.min)
                # We update the current min
                self.min = val
        else:
            raise Exception("ERROR - Pushing None values is not permitted.")

    def pop(self) -> None:
        # Check if stack is not empty
        if self.min_stack:
            # Pop and update helper_dict
            popped = self.min_stack.pop()
            self.helper_dict[popped] -= 1
            # Check whether poped element was min, fetch new min from previous_min
            if popped == self.min and len(self.min_stack) > 1 and self.helper_dict[popped] == 0:
                # print("LOG - pop() - ",self.previous_min)
                self.min = self.previous_min[-1]
                # Update self.previous_min
                self.previous_min.pop()
            # print(self.helper_dict)
            if len(self.min_stack) == 1:
                self.min = self.min_stack[0]
        else:
            raise Exception("ERROR - Popping empty stack is not permitted.")



    def top(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        else:
            raise Exception("ERROR - top() from an empty stack is not permitted.")
        

    def getMin(self) -> int:
        # print("LOG - getMin() - ",self.min_stack)
        if self.min_stack:
            return self.min
        else:
            raise Exception("ERROR - getMin() of empty stack is not permitted")    

        


# Your MinStack object will be instantiated and called as such:
# ["MinStack","push","push","push","getMin","pop","getMin"]
# [[],[0],[1],[0],[],[],[]]
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()