from fastapi import FastAPI, Query
from datetime import datetime
import httpx

app = FastAPI(title="Kisan AI Sahayak Backend")

@app.get("/health")
def health():
    return {"status": "ok", "message": "Backend running", "time": datetime.utcnow().isoformat()}

@app.get("/api/v1/weather-advisory")
async def weather_advisory(
    lat: float = Query(...),
    lon: float = Query(...),
    crop: str = Query("generic"),
    stage: str = Query("germination")
):
    # Mock weather data (replace later with live API)
    weather = {
        "temp": 30,
        "max_temp": 33,
        "min_temp": 22,
        "rain_prob": 40,
        "humidity": 65,
        "condition": "Partly cloudy"
    }
    advisory = []
    if crop.lower() == "cotton" and stage.lower() == "flowering" and weather["rain_prob"] > 60:
        advisory.append({
            "priority": "high",
            "message": "Heavy rain expected — risk of boll rot",
            "action": "Spray fungicide before rain (e.g. Mancozeb) if available"
        })
    return {"weather": weather, "advisory": advisory, "updated_at": datetime.utcnow().isoformat()}
