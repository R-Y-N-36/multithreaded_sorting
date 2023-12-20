from threading import Thread, Lock
from time import sleep

# Sorting functions
def merge_sort(arr):
    # Implementation of merge sort algorithm
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    # Merging two sorted arrays into a single sorted array
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def bubble_sort(arr):
    # Implementation of bubble sort algorithm
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

def quick_sort(arr):
    # Implementation of quick sort algorithm
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    result = quick_sort(left) + middle + quick_sort(right)
    return result

lock = Lock()

def execute_sorting_function(sort_function, lock, data):
    # Function to execute a sorting function in a thread-safe manner

    lock.acquire()

    sleep(0.1)
    print(sort_function)
    result = sort_function(data)
    print("Result:", result)

    lock.release()

# Input data
data = [4, 2, 7, 1, 9, 5, 3, 8, 6]

# Threads for sorting functions
threads = [
    Thread(target=execute_sorting_function, args=(merge_sort, lock, data)),
    Thread(target=execute_sorting_function, args=(bubble_sort, lock, data)),
    Thread(target=execute_sorting_function, args=(quick_sort, lock, data)),
]

# Start threads
for thread in threads:
    thread.start()

# Wait for threads to finish
for thread in threads:
    thread.join()
