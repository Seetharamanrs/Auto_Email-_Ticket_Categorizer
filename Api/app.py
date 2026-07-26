from fastapi import FastAPI
import joblib

app=FastAPI()
from src.preprocessing import preprocessing
model=joblib.load("models/lr_model.pkl")
vect=joblib.load("models/tfidf_vectorizer.pkl")

def processing(data):
    cleaned=preprocessing(data)
     priority_words = [
        "urgent",
        "immediately",
        "critical",
        "down",
        "error",
        "failed",
        "not working"
    ]

    priority = "Normal"
    for i in priority_words:
        if cleaned in priority_words:
            priority="High"
    vector=vect.transform([cleaned])
    predicted=model.predict(vector)
    confident=model.predict(vector).max()
    if confidence < 0.60:
        predicted = "Needs Human Review"

    return predicted[0],confident,priority
class Ticket(BaseModel):
    ticket:str

@app.post("/predict")
def predict(data:Ticket):
    prediction=processing(data.ticket)
    return {"predicted_department":prediction,
            "confidence": round(confidence, 2),
        "priority": priority}
