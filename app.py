"""ATM Downtime Monitoring - Chainlit App. Run with: chainlit run app.py"""

import chainlit as cl
from agents import Runner, set_default_openai_key
from openai.types.responses import ResponseTextDeltaEvent

from config import get_config
from agent_defs import agent
from utils.logging import get_logger

logger = get_logger(__name__)

def _ensure_config():
    cfg = get_config()
    set_default_openai_key(cfg["openai_api_key"])
    return cfg

@cl.on_chat_start
async def on_chat_start():
    try:
        _ensure_config()
        cl.user_session.set("chat_history", None)
        await cl.Message(content="**ATM Downtime Monitor** - Paste ATM log entries to detect downtime (ERROR 503, TIMEOUT, DISCONNECTED, etc.). Format: ATM-ID | timestamp | status", author="ATM Monitor").send()
    except ValueError as e:
        await cl.Message(content="Configuration Error: " + str(e), author="System").send()
        raise

@cl.on_message
async def on_message(message: cl.Message):
    user_content = message.content.strip()
    if not user_content:
        await cl.Message(content="Please paste ATM log entries.", author="ATM Monitor").send()
        return
    try:
        _ensure_config()
        logger.info("Processing: %s", user_content[:80])
        result = Runner.run_streamed(agent, input=user_content)
        msg = cl.Message(content="", author="ATM Monitor")
        await msg.send()
        import asyncio
        async for event in result.stream_events():
            if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                if event.data.delta:
                    await msg.stream_token(event.data.delta)
            await asyncio.sleep(0.01)
        await msg.update()
        logger.info("Response streamed")
    except Exception:
        logger.exception("ATM query failed")
        await cl.Message(content="Something went wrong. Please try again.", author="ATM Monitor").send()
