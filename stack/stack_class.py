class Stack:

    def __init__(self):
        self.items = []

    def push(self,items):
        self.items.append(items)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None 
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        print("Stack(top>bottom) :",self.items[::-1])

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print("After pushing :")
s.display()
print("Top Element : ",s.peek())
print("Popped element :",s.pop())
print("After pop : ")
s.display()
print("Total size : ",s.size())
print("Is stack Empty :",s.is_empty())