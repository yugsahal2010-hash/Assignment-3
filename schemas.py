from typing import Optional
from pydantic import BaseModel


class MatchStateInput(BaseModel):
    match: str
    innings_number: int
    score: int
    overs: str
    wickets: int
    batting_team: str
    bowling_team: str
    target: Optional[int] = None  # Required if innings_number == 2


class MatchStateResponse(BaseModel):
    match: str
    innings_number: int
    score: int
    overs: str
    wickets: int
    batting_team: str
    bowling_team: str
    target: Optional[int] = None
    runs_needed: Optional[int] = None
    balls_remaining: Optional[int] = None
    required_run_rate: Optional[float] = None


class ErrorResponse(BaseModel):
    detail: str
