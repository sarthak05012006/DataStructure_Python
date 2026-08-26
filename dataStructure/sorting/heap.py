def heapify(arr, n, i):
    """Ensures the subtree rooted at index i satisfies the Max Heap property."""
    largest = i          # Initialize largest as root
    left = 2 * i + 1     # Left child index
    right = 2 * i + 2    # Right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest element is not the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected sub-tree

def heap_sort(arr):
    """Main function to sort an array using Heap Sort."""
    n = len(arr)

    # Step 1: Build a Max Heap (rearrange array)
    # Start from the last non-leaf node and move upwards to the root
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Move current root to the end
        heapify(arr, i, 0)               # Call max heapify on the reduced heap

# --- Example Usage ---
if __name__ == "__main__":
    data = [12, 11, 13, 5, 6, 7]
    print("Original array:", data)
    
    heap_sort(data)
    print("Sorted array:  ", data)
