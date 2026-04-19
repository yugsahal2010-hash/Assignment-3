from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import MatchStateInput, MatchStateResponse, ErrorResponse
from services import get_match_state

app = FastAPI(title="Khel AI Match State API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "status": "Online",
        "message": "Khel AI API is live and operational.",
        "documentation": "/docs"
    }


@app.post(
    "/api/match/state/",
    response_model=MatchStateResponse,
    responses={400: {"model": ErrorResponse}, 500: {"model": ErrorResponse}},
)
def read_match_state(input_data: MatchStateInput):
    if input_data.innings_number == 2 and input_data.target is None:
        raise HTTPException(status_code=400, detail="target is required for 2nd innings.")
    if input_data.innings_number not in [1, 2]:
        raise HTTPException(status_code=400, detail="innings_number must be 1 or 2.")
    try:
        return get_match_state(input_data.model_dump())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Calculation error: {str(e)}")
