import uvicorn
from fastapi import FastAPI, Request
from typing import List, Dict, Any

app = FastAPI(title="Test Alerts Receiver")

# Stockage des alertes reçues
received_alerts: List[Dict[str, Any]] = []

@app.get("/")
def home():
    return {"message": "Hello, World!"}

# Endpoint pour recevoir les alertes
@app.post("/alert")
async def receive_alert(request: Request):
    body = await request.json()
    received_alerts.append(body)
    return {"status": "received", "count": len(received_alerts)}

# Endpoint pour consulter les alertes reçues
@app.get("/alerts")
async def get_alerts():
    return {"alerts": received_alerts}

# Endpoint pour vider la mémoire des alertes reçues
@app.delete("/alerts")
async def clear_alerts():
    received_alerts.clear()
    return {"status": "cleared"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
