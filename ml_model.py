import random
import time
import joblib
import numpy as np
from sklearn.linear_model import LinearRegression


def generate_data():
    X = []
    y = []
    for n in range(1000, 25000, 1000):
        arr = list(range(n))
        target = random.choice(arr)

        start = time.time()
        for i in arr:
            if i == target:
                break
        linear_time = time.time() - start

        start = time.time()
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                break
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        binary_time = time.time() - start

        X.append([n, 0])  # linear search
        y.append(linear_time)

        X.append([n, 1])  # binary search
        y.append(binary_time)
    return np.array(X), np.array(y)


def train_model():
    X, y = generate_data()
    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, "model.pkl")
    return {"message": "Model trained successfully", "data_points": len(X)}


def predict_time(n, search_type="linear"):
    model = joblib.load("model.pkl")
    type_code = 0 if search_type == "linear" else 1
    prediction = model.predict([[n, type_code]])[0]
    return round(float(prediction), 6)


def get_predictions():
    model = joblib.load("model.pkl")
    X_test = np.array([[i, 0] for i in range(1000, 25000, 1000)] +
                      [[i, 1] for i in range(1000, 25000, 1000)])
    y_pred = model.predict(X_test)
    return X_test, y_pred
