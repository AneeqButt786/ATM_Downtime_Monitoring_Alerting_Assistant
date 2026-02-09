from typing import List
from agents import function_tool

DOWNTIME_PATTERNS = ["ERROR 503", "TIMEOUT", "DISCONNECTED", "UNRESPONSIVE", "DOWN"]

@function_tool
def detect_atm_downtime(logs: List[str]) -> List[dict]:
    """Detects ATM downtime incidents from logs."""
    incidents = []
    for log in logs:
        for pattern in DOWNTIME_PATTERNS:
            if pattern in log:
                parts = log.split(" | ")
                incidents.append({"atm_id": parts[0], "timestamp": parts[1], "issue": pattern, "log": log})
                break
    return incidents or [{"message": "No downtime issues detected."}]
