import joblib
from fastapi import FastAPI
from pydantic import BaseModel

# Load saved model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

app = FastAPI()

# Define input format
class EmailInput(BaseModel):
    mail_text: str

@app.get("/")
def home():
    return {"Hello Welcome!!"}

@app.get("/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name}!"}

@app.post("/predict/")
def predict_email(input_mail: EmailInput):
    # Transform text using the loaded vectorizer
    input_data_features = vectorizer.transform([input_mail.mail_text])

    # Predict using the loaded model
    prediction = model.predict(input_data_features)

    return {"prediction": "Ham mail" if prediction[0] == 1 else "Spam mail"}

# uvicorn app:app --reload