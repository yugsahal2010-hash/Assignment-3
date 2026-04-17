from typing import Optional
from pydantic import BaseModel

class MatchStateResponse(BaseModel):
    match: str
    innings_number: int
    score: int
    overs: str
    wickets: int
    batting_team: str
    bowling_team: str
    target: Optional[int] = None

class ErrorResponse(BaseModel):
    detail: str