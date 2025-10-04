# ML Sorting and Searching Benchmark API

This project is a **Python FastAPI application** that benchmarks and predicts the performance of common **sorting** and **searching algorithms**.
It measures real execution times for different dataset sizes and uses a **machine learning model** to estimate how long a search operation would take without running it directly.

---

## Overview

The API can:

- Benchmark **linear** and **binary search** for large arrays (up to 250,000 elements)
- Benchmark multiple **sorting algorithms** (quick, merge, insertion, bubble, and Python’s built-in sort)
- Use measured results to train a regression model that predicts expected search times
- Return all results in JSON format for easy integration

---

## Project Structure

```
project/
│
├── main.py                # App entry point (FastAPI app)
│
├── routers/
│   ├── benchmark.py       # Benchmark endpoints for searching
│   ├── sort.py            # Sorting benchmark endpoints
│   └── train.py           # ML model training and prediction endpoints
│
├── ml/
│   ├── model.py           # Model creation, training, saving, and prediction
│   └── features.py        # Feature extraction utilities
│
└── utils/
    ├── algorithms.py      # Sorting and searching implementations
    └── benchmark_utils.py # Benchmarking and timing helpers
```

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/ml-sort-search-api.git
   cd ml-sort-search-api
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   or manually:

   ```bash
   pip install fastapi uvicorn numpy scikit-learn matplotlib python-multipart aiofiles
   ```

3. Start the server:

   ```bash
   uvicorn main:app --reload
   ```

4. Open the API documentation:

   ```
   http://localhost:8000/docs
   ```

---

## API Endpoints

### Search Benchmark

```
GET /api/benchmark/search?size=50000&algorithm=linear
```

**Example Response**

```json
{
  "algorithm": "linear",
  "size": 50000,
  "search_time": 0.0143,
  "found": true
}
```

### Sort Benchmark

```
GET /api/sort/compare?size=10000
```

**Example Response**

```json
{
  "results": [
    { "algorithm": "builtin", "time": 0.0045 },
    { "algorithm": "merge_sort", "time": 0.012 },
    { "algorithm": "quick_sort", "time": 0.015 }
  ]
}
```

### Train the ML Model

```
POST /api/ml/train
```

**Request Body**

```json
{
  "n_samples": 200,
  "max_size": 100000,
  "repeat": 3,
  "test_size": 0.2
}
```

**Response**

```json
{
  "status": "success",
  "train_r2": 0.97,
  "test_r2": 0.95,
  "model_saved": true
}
```

### Predict Search Time

```
POST /api/ml/predict
```

**Request Body**

```json
{
  "size": 80000,
  "sorted_flag": true,
  "algorithm": "binary",
  "target_present": true,
  "target_position_ratio": 0.75
}
```

**Response**

```json
{
  "predicted_time": 0.00062
}
```

### Model Status

```
GET /api/ml/status
```

**Response**

```json
{
  "model_status": "trained",
  "model_file": "ml/search_time_model.pkl"
}
```

---

## How Machine Learning Is Used

The system records actual runtimes from benchmarking and uses them to train a **regression model** (Random Forest) that predicts search time based on:

- Dataset size
- Whether the array is sorted
- Algorithm used
- Whether the target element exists
- Approximate target position

This allows quick estimation of runtime trends without re-running benchmarks.

---

## Technologies Used

- Python
- FastAPI
- NumPy
- scikit-learn
- Matplotlib (for optional plotting)
- Uvicorn (server)

---

## Future Improvements

- Add a recommendation endpoint for suggesting the fastest algorithm
- Support more data structures and algorithms
