import random
import time


def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def measure_search_times():
    arr = sorted(random.sample(range(0, 250000), 5000))
    target = random.choice(arr)
    results = {}

    start = time.time()
    linear_search(arr, target)
    results["Linear Search"] = round(time.time() - start, 5)

    start = time.time()
    binary_search(arr, target)
    results["Binary Search"] = round(time.time() - start, 5)

    return {"search_times": results}
