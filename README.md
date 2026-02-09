# ATM Downtime Monitoring and Alerting Agent

## Overview

Monitors ATM system logs to detect downtime patterns (ERROR 503, TIMEOUT, DISCONNECTED, UNRESPONSIVE). Emits structured incidents with ATM ID, timestamp, and issue for alerting pipelines and operational dashboards.

## Features

- Detect downtime patterns from logs
- Structured incident output (ATM ID, timestamp, issue)
- Chainlit chat UI with streaming

## Tech Stack

Python 3.12+, OpenAI Agents SDK, Chainlit, python-dotenv

## Setup

1. cd ATM_Downtime_Monitoring_Alerting_Assistant
2. pip install -r requirements.txt
3. Copy .env.example to .env and set OPENAI_API_KEY

## Run Commands

chainlit run app.py

## Example Use Cases

1. Paste ATM logs: "ATM-202 | 2025-05-25 14:04:18 | ERROR 503 - Service Unavailable"
2. Detect issues from a list of log entries
3. Get structured incident report for dashboard
