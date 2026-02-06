#reverse the string using stack 
class stack:
    def __init__(self):
        self.st = []
    def push(self, data):
        self.st = [data] + self.st
    def pop(self):
        return self.st.pop(0)
    def size(self):
        return len(self.st)
    def isEmpty(self):
        return self.size() == 0
    def peek(self):
        return self.st[0]
    def top(self):
        return self.st[0]

def display(st):
    for i in st:
        print(i,end = "")
    print()


def reverse_string(s):
    rev = stack()
    for i in s.st:
        rev.push(i)
    
    
    ans = ""
    while not rev.isEmpty():
        ans += rev.top()
        rev.pop()   
    return ans

s = stack()

s.push("H")
s.push("e")
s.push("l")
s.push("l")
s.push("o")

print("Original String:")
display(s.st)
reversed_s = reverse_string(s)
print("\nReversed String:")
display(reversed_s)
