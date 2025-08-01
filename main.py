import os
import asyncio
from langchain.agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI
from dotenv import load_dotenv
import rich

# =================== ENV SETUP ===================
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

try:
    external_client = AsyncOpenAI(
        api_key=GEMINI_API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    )
    model = OpenAIChatCompletionsModel(
        model="gemini-2.0-flash",
        openai_client=external_client,
    )
except Exception as e:  # noqa: F841
    raise

# ================== AGENTS ======================

poet_identifier_agent = Agent(
    name="PoetIdentifierAgent",
    instructions="""
You are a poet identification agent. Analyze the given poetry and determine if it resembles the style of any well-known poet. Mention the likely poet and explain why. If no poet is identified, state so and provide a brief reason.
""",
    model=model,
)

dramatic_agent = Agent(
    name="DramaticAgent",
    instructions="""
You are a dramatic poetry analysis agent. Detect emotional intensity, dramatic language, or psychological conflict in the poetry and explain it. If no dramatic elements are found, state so and provide a brief reason.
""",
    model=model,
)

narrative_agent = Agent(
    name="NarrativeAgent",
    instructions="""
You are a narrative structure analysis agent. Identify any story structure, character development, or sequence of events within the poetry. If no narrative elements are found, state so and provide a brief reason.
""",
    model=model,
)

main_agent = Agent(
    name="MainAgent",
    instructions="""
You are the Main Agent in a multi-agent poetry analysis system. Receive a poetry text input, classify it based on linguistic and semantic content, and delegate to the most appropriate sub-agent:
- PoetIdentifierAgent: if the poetry uses concise metaphors, abstract themes, or stylistic markers resembling a known poet (e.g., Emily Dickinson’s short lines, metaphors, or dashes).
- DramaticAgent: if the poetry has intense emotions, vivid imagery, or psychological conflict (e.g., rage, sorrow, or dramatic shifts).
- NarrativeAgent: if the poetry has a story-like structure, characters, or chronological events.
If the poetry is ambiguous, prioritize PoetIdentifierAgent for short, metaphorical poems, then NarrativeAgent for story-like content, and default to DramaticAgent only if no other category fits.
""",
    model=model,
    handoffs=[poet_identifier_agent, dramatic_agent, narrative_agent],
)

# ================== ASYNC RUNNER ===================

async def main():
    poetry = input("Enter poetry text (or press Enter for default): ").strip()
    if not poetry:
        poetry = "In the battlefield of my heart, I fought memories like enemies. Then she smiled, and my war was over."
    
    try:
        result = await Runner.run(
            starting_agent=main_agent,
            input=poetry,
        )
        rich.print("[bold green]Final Output:[/bold green]", result.final_output)
        rich.print("[bold cyan]Last Agent Used:[/bold cyan]", result.last_agent.name)
    except Exception as e:  # noqa: F841
        rich.print("[bold red]Error:[/bold red] Failed to analyze poetry.")

# ================== RUN APP ========================

if __name__ == "__main__":
    asyncio.run(main())