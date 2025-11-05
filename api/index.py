from fastapi import FastAPI, Request
from typing import List, Dict, Any
# import logging

# # Configuration du logging pour déboguer
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

app = FastAPI(title="Test Alerts Receiver")

# Stockage des alertes reçues
received_alerts: List[Dict[str, Any]] = []

@app.get("/")
def home():
    # logger.info("Home endpoint called")
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
    # logger.info(f"Retrieving {len(received_alerts)} alerts")
    return {"alerts": received_alerts}

# Endpoint pour vider la mémoire des alertes reçues
@app.delete("/alerts")
async def clear_alerts():
    received_alerts.clear()
    return {"status": "cleared"}