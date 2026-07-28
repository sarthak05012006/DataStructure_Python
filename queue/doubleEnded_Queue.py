from collections import deque
queue = deque()

queue.append("Ravi")
queue.append("Priya")
queue.append("you")
queue.append("Karan")
for item in queue:
    print(item)
first = queue.popleft()
print(first)
print(queue)
