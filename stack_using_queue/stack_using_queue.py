from queue import Queue
class MyStack:

    def __init__(self):
        self.queue1 = Queue()
        self.top_elem= None

    def push(self, x: int) -> None:
        size = self.queue1.qsize()
        self.queue1.put(x)
        for _ in range(size):
            self.queue1.put(self.queue1.get())
    def pop(self) -> int:
        return self.queue1.get()
    def top(self) -> int:
        return self.queue1.queue[0]
        
    def empty(self) -> bool:
        return self.queue1.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()