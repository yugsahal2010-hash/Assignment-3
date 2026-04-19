from typing import Dict, Any


def _overs_to_balls(overs_str: str) -> int:
    try:
        parts = overs_str.split(".")
        full = int(parts[0])
        balls = int(parts[1]) if len(parts) > 1 else 0
        return (full * 6) + balls
    except (ValueError, IndexError):
        return 0


def get_match_state(data: Dict[str, Any]) -> dict:
    result = {
        "match": data["match"],
        "innings_number": data["innings_number"],
        "score": data["score"],
        "overs": data["overs"],
        "wickets": data["wickets"],
        "batting_team": data["batting_team"],
        "bowling_team": data["bowling_team"],
        "target": data.get("target"),
        "runs_needed": None,
        "balls_remaining": None,
        "required_run_rate": None,
    }

    if data["innings_number"] == 2 and data.get("target"):
        balls_bowled = _overs_to_balls(data["overs"])
        # Assuming T20 = 120 balls total
        balls_remaining = max(0, 120 - balls_bowled)
        runs_needed = max(0, data["target"] - data["score"])
        rrr = round((runs_needed / (balls_remaining / 6)), 2) if balls_remaining > 0 else 99.99

        result["runs_needed"] = runs_needed
        result["balls_remaining"] = balls_remaining
        result["required_run_rate"] = rrr

    return result
