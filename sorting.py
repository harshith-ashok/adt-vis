import random
import time


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def measure_sort_times():
    data = [random.randint(0, 250000) for _ in range(5000)]
    results = {}

    for name, func in [("Bubble Sort", bubble_sort), ("Quick Sort", quick_sort)]:
        sample = data.copy()
        start = time.time()
        func(sample)
        elapsed = round(time.time() - start, 4)
        results[name] = elapsed

    return {"sorting_times": results}
