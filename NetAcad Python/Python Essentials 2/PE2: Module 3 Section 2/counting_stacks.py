#!/usr/bin/env python3

# super class
class SourceStack:
    def __init__(self):
        self.__stk = []
    
    def push(self, val):
        self.__stk.append(val)
        
    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val
    
# class
class Stack(SourceStack):
    def __init__(self):
        SourceStack.__init__(self)
        self.__push_count = 0
        self.__pop_count = 0

    def get_counter(self, op="pop"):
        try:
            choice = op.lower()
        except TypeError:
            print(f"The input '{op}' is difficult.")
        if "pop" in choice:
            return self.__pop_count
        else:
            return self.__push_count        

    def pop(self):
        SourceStack.pop(self)
        self.__pop_count += 1
        
    def push(self, val):
        SourceStack.push(self, val)
        self.__push_count += 1
    

stk = Stack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter(input("Count for pushes or pops? [push/pop]\n")))
    
