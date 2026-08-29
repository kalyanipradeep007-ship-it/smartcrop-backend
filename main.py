from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="SmartCrop AI Backend")

# Allow CORS so the live frontend at https://smart-crop-guardian-30.lovable.app can connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict to ["https://smart-crop-guardian-30.lovable.app"] in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "online", "message": "SmartCrop AI Backend is running securely on HTTPS!"}

@app.post("/predict")
def predict_disease():
    # Placeholder endpoint for crop disease prediction logic
    return {"disease": "Healthy", "confidence": 0.95, "risk": "LOW"}