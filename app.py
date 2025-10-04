from flask import Flask, render_template, request, jsonify
import random
import time
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# ML Model training (simulate search times)
sizes = np.array([50, 500, 5000, 50000, 100000, 250000]).reshape(-1, 1)
linear_times = np.array([0.00005, 0.0005, 0.005, 0.05, 0.1, 0.25])
binary_times = np.array([0.00002, 0.00003, 0.00005, 0.0001, 0.00015, 0.0002])

linear_model = LinearRegression().fit(sizes, linear_times)
binary_model = LinearRegression().fit(sizes, binary_times)


def predict_time(n, algo='linear'):
    if algo == 'linear':
        return linear_model.predict(np.array([[n]]))[0]
    else:
        return binary_model.predict(np.array([[n]]))[0]

# Small array for animation


def generate_array(size=50):
    return random.sample(range(0, 250001), size)

# Sorting Steps for animation


def bubble_sort_steps(arr):
    arr = arr.copy()
    steps = [arr.copy()]
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                steps.append(arr.copy())
    return steps


def merge_sort_steps(arr):
    arr_copy = arr.copy()
    steps = []

    def merge_sort_rec(lst):
        if len(lst) > 1:
            mid = len(lst)//2
            L, R = lst[:mid], lst[mid:]
            merge_sort_rec(L)
            merge_sort_rec(R)
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    lst[k] = L[i]
                    i += 1
                else:
                    lst[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                lst[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                lst[k] = R[j]
                j += 1
                k += 1
            steps.append(arr_copy.copy())
    merge_sort_rec(arr_copy)
    return steps

# Search functions (small array)


def linear_search(arr, target):
    start = time.time()
    for i, val in enumerate(arr):
        if val == target:
            return i, time.time()-start
    return -1, time.time()-start


def binary_search(arr, target):
    arr_sorted = sorted(arr)
    start = time.time()
    low, high = 0, len(arr_sorted)-1
    while low <= high:
        mid = (low+high)//2
        if arr_sorted[mid] == target:
            return mid, time.time()-start
        elif arr_sorted[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1, time.time()-start

# Routes


@app.route('/')
def index():
    anim_array = generate_array(50)
    bubble_steps = bubble_sort_steps(anim_array)
    merge_steps = merge_sort_steps(anim_array)
    return render_template("index.html", bubble_steps=bubble_steps, merge_steps=merge_steps, anim_array=anim_array)


@app.route('/search', methods=['POST'])
def search():
    data = request.json
    target = int(data['target'])
    algo = data['algo']
    arr = data['arr']           # small animation array
    full_size = int(data['full_size'])  # user input size

    # Actual search on small array
    if algo == 'linear':
        index, t = linear_search(arr, target)
    else:
        index, t = binary_search(arr, target)

    # ML prediction for user input size
    pred_time = predict_time(full_size, algo)
    return jsonify({'index': index, 'time': round(t, 6), 'pred_time': round(pred_time, 6)})


@app.route('/ml_predict', methods=['POST'])
def ml_predict():
    data = request.json
    sizes_input = data['sizes']  # array of sizes input by user
    linear_pred = [predict_time(s, 'linear') for s in sizes_input]
    binary_pred = [predict_time(s, 'binary') for s in sizes_input]
    return jsonify({'linear': linear_pred, 'binary': binary_pred})


if __name__ == "__main__":
    app.run(debug=True)
