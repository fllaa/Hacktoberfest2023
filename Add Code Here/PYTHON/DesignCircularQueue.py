class MyCircularDeque:
    def __init__(self, k: int):
        self.st1 = []   
        self.st2 = k
    def insertFront(self, value: int) -> bool:
        if len(self.st1) < self.st2:
            self.st1 = [value] + self.st1
            return True
        return False
    def insertLast(self, value: int) -> bool:
        if len(self.st1) < self.st2:    
            self.st1.append(value)
            return True
        return False
    def deleteFront(self) -> bool:
        if len(self.st1) > 0:    
            self.st1.pop(0)
            return True
        return False
    def deleteLast(self) -> bool:
        if len(self.st1) > 0:
            self.st1.pop()
            return True
        return False
    def getFront(self) -> int:
        return self.st1[0] if len(self.st1) > 0 else -1
    def getRear(self) -> int:
        return self.st1[-1] if len(self.st1) > 0 else -1
    def isEmpty(self) -> bool:
        return len(self.st1) == 0            
    def isFull(self) -> bool:
        return len(self.st1) == self.st2

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
#I have described here how to create a Circular Queue with trying to use less written code and more easy to understandable code.
