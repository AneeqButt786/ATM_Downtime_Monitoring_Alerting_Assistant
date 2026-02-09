from agents import Agent
from services.tools import detect_atm_downtime

agent = Agent(
    name="ATM Downtime Notifier",
    instructions="Monitor ATM logs for downtime. Use detect_atm_downtime to identify ERROR 503, TIMEOUT, DISCONNECTED, UNRESPONSIVE. Provide structured alerts with ATM ID, timestamp, and issue.",
    model="gpt-4o-mini",
    tools=[detect_atm_downtime],
)
