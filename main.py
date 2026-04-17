from fastapi import FastAPI
from schemas import MatchStateResponse
from services import get_match_state

app = FastAPI(title="Khel AI Match State API")
@app.get("/")
def home():
    return {
        "status": "Online",
        "message": "Khel AI API is live and operational.",
        "documentation": "/docs"
    }

@app.get("/api/match/{match_id}/state/", response_model=MatchStateResponse)
def read_match_state(match_id: int):
    # This calls the service that aggregates score, overs, and target
    return get_match_state(match_id)