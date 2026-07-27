# Using standard Python dynamic lists 
#insertion deletion by built in function:
arr = [10, 20, 30, 40]

# --- INSERTION ---
arr.append(50)         # Result: [10, 20, 30, 40, 50]
print(arr)
arr.insert(2, 99)      # Result: [10, 20, 99, 30, 40, 50]
print(arr)
# --- DELETION ---
arr.pop(2)  
print(arr)           # Removes 99. Result: [10, 20, 30, 40, 50]
arr.remove(40)         # Removes 40. Result: [10, 20, 30, 50]
print(arr)