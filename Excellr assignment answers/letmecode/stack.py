class Stack:
    def __init__(self):
        self.elements = []
    
    def Push(self,data):
        self.elements.append(data)

    def Pop(self):
        self.elements.pop()

    def Peek(self):
        return self.elements[-1]

    def isEmpty(self):
        return len(self.elements) == 0

    def printstack(self):
        for i in self.elements:
            print(i,end=" ")


s = Stack()

s.Push(1)
s.Push(4)
s.Push(5)
s.Push(6)



print(s.Peek())

s.printstack()

s.Pop()

print(s.Peek())


print(s.isEmpty())
