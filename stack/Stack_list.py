stack = []
stack.append("a")
stack.append("b")
stack.append("c")
print(stack)
#peek 
top_element = stack[-1] if stack else None
print("Top Element : ", top_element)
item = stack.pop()
print("Popped : ",item)
print(stack)
print("Stack size:", len(stack))
print("Is empty?\n", len(stack) == 0)
