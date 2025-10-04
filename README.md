# ADT ML Sorting & Search Visualization

**Interactive visualization of sorting algorithms with dynamic ML-predicted search times.**

Explore **Bubble and Merge Sort** step by step and interact with search algorithms. The project uses a **machine learning model** to predict how long Linear and Binary search would take on large arrays, helping visualize algorithm efficiency.

---

## Features

- **Bubble Sort & Merge Sort Animation:** Step-by-step visualizations showing how arrays are sorted.
- **Interactive Search:** Search a number in a small array using Linear or Binary search and see actual times.
- **Dynamic ML Prediction Graph:** Enter any array sizes to see predicted Linear vs Binary search times instantly.
- **Scalable & Educational:** Demonstrates algorithm efficiency for realistically large datasets.

## Tech Stack

- **Backend:** Python 3.x, Flask
- **ML:** scikit-learn (Linear Regression)
- **Numerical Operations:** NumPy
- **Frontend:** Plotly.js for interactive animations and graphs

---

## Project Structure

```
adt_ml_sorting/
│
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # Frontend template
├── static/
│ ├── js/ # Optional JS files
│ └── css/ # Optional CSS files
└── README.md # Project documentation
```

---

## Installation & Running

1. Clone the repository:

```bash
git clone <repo-url>
cd adt_ml_sorting
```

2. (Optional) Create a virtual environment:

```bash
python -m venv venv
# Activate it:
# Mac/Linux: source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Flask app:

```bash
python app.py
```

5. Open your browser and go to:

```
http://127.0.0.1:5000/
```

---

## How to Use

1. **Sorting Visualization:** Watch Bubble Sort and Merge Sort animations on the default small array.
2. **Search a Number:** Enter a number, choose Linear/Binary search, and see actual + predicted times.
3. **Dynamic ML Graph:** Enter any array sizes (comma-separated) to update the predicted search time graph in real time.
