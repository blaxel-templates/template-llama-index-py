from typing import AsyncGenerator

from blaxel.llamaindex import bl_model, bl_tools
from llama_index.core.agent.workflow import AgentStream, ReActAgent
from llama_index.core.tools import FunctionTool


async def weather(city: str) -> str:
    """Get the weather in a given city"""
    return f"The weather in {city} is sunny"


async def agent(input: str) -> AsyncGenerator[str, None]:
    prompt = (
        "You are a helpful assistant that can answer questions and help with tasks."
    )
    tools = await bl_tools(["blaxel-search"]) + [
        FunctionTool.from_defaults(async_fn=weather)
    ]
    model = await bl_model("sandbox-openai")
    agent = ReActAgent(llm=model, tools=tools, system_prompt=prompt)
    async for event in agent.run(input).stream_events():
        if isinstance(event, AgentStream):
            yield event.delta
