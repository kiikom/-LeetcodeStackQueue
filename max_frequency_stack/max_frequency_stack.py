from collections import defaultdict, deque

class FreqStack:
    def __init__(self):
        self.frequency = defaultdict(int) 
        self.stack = deque()    
        self.max_freq = 0                 

    def push(self, val: int) -> None:
        self.frequency[val] += 1           
        freq = self.frequency[val]          
        while len(self.stack) < freq:  
            self.stack.append(deque())
        self.stack[freq - 1].append(val) 

    def pop(self) -> int:
        if not self.stack:  
            return None
        val = self.stack[-1].pop()  
        if not self.stack[-1]:  
            self.stack.pop()
        self.frequency[val] -= 1               
        if not self.stack:  
            self.max_freq = 0
        return val
