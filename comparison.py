import os
from ml_model import get_predictions, generate_data
import matplotlib.pyplot as plt
import matplotlib
# <-- Add this line right at the top (before pyplot import)
matplotlib.use("Agg")


def plot_predicted_vs_actual():
    X_test, y_pred = get_predictions()
    X_actual, y_actual = generate_data()

    plt.figure(figsize=(8, 5))
    plt.scatter(X_actual[:, 0], y_actual, label="Actual", s=15)
    plt.scatter(X_test[:, 0], y_pred, label="Predicted", s=15)
    plt.xlabel("Array Size")
    plt.ylabel("Time (seconds)")
    plt.title("Predicted vs Actual Search Times")
    plt.legend()

    os.makedirs("plots", exist_ok=True)
    file_path = "plots/predicted_vs_actual.png"
    plt.savefig(file_path)
    plt.close()
    return file_path
