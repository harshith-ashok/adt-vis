from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sorting import measure_sort_times
from searching import measure_search_times
from ml_model import train_model, predict_time, get_predictions
from comparison import plot_predicted_vs_actual

app = FastAPI(title="Sorting & Searching Visualizer")


@app.get("/")
def home():
    return {"message": "Welcome to Sorting & Searching Visualizer"}


@app.get("/sort")
def sort_comparison():
    data = measure_sort_times()
    return JSONResponse(content=data)


@app.get("/search")
def search_comparison():
    data = measure_search_times()
    return JSONResponse(content=data)


@app.post("/train")
def train():
    response = train_model()
    return JSONResponse(content=response)


@app.get("/predict")
def predict(n: int):
    predicted_time = predict_time(n)
    return {"predicted_time": predicted_time}


@app.get("/compare")
def compare_plot():
    file_path = plot_predicted_vs_actual()
    return {"message": "Comparison plot generated", "file": file_path}
