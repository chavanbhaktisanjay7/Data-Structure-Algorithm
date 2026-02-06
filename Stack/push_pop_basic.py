#class stack
class stack:
    def __init__(self):
        self.st = []
    def push(self,data):
        self.st = [data] + self.st
    def pop(self):
        return self.st.pop(0)
    def size(self):
        return len(self.st)
    def isEmpty(self):
        return self.size() == 0
    def peek(self):
        return self.st[0]
        
        
s = stack()
s.push(6)
s.push(2)
s.push(8)
s.push(4)
s.push(1)
print(s.st)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.st)