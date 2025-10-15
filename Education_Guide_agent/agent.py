import os

try:
    from dotenv import load_dotenv
    load_dotenv()

    # Retrieve the model name from the environment variable, defaulting to gemini-2.0-flash
    MODEL_NAME = os.environ.get("GOOGLE_GENAI_MODEL", "gemini-2.0-flash")
except ImportError:
    # Fallback if python-dotenv is not installed
    print("Warning: python-dotenv not installed. Ensure API key is set or environment is configured.")
    MODEL_NAME = "gemini-2.0-flash"

from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.tools import google_search

# Import the necessary instructions for the sub-agents and orchestrator
from Education_Guide_agent.instructions import (
    RECOMMENDATION_AGENT_INSTRUCTIONS,
    ADMISSIONS_FUNDING_AGENT_INSTRUCTIONS,
    ORCHESTRATOR_INSTRUCTION
)

# --- 1. Sub-Agent for Program Recommendation ---
recommendation_agent = LlmAgent(
    name="RecommendationAgent",
    model=MODEL_NAME,
    description="An agent that analyzes a user's profile and interests to suggest suitable academic programs and career paths.",
    instruction=RECOMMENDATION_AGENT_INSTRUCTIONS,
    tools=[google_search],
    output_key="recommendation_summary"  # Key for storing the output in the state
)

# --- 2. Sub-Agent for Logistics and Funding ---
admissions_funding_agent = LlmAgent(
    name="AdmissionsFundingAgent",
    model=MODEL_NAME,
    description="An agent that researches admission requirements, deadlines, and funding options for the recommended programs.",
    instruction=ADMISSIONS_FUNDING_AGENT_INSTRUCTIONS,
    tools=[google_search],
    # This agent implicitly receives 'recommendation_summary' from the previous agent
    output_key="logistics_summary"  # Key for storing the output in the state
)

# --- 3. Sequential Orchestrator Agent (The Root Agent) ---
Education_Guidance_Orchestrator = SequentialAgent(
    name="EducationGuidanceAgent",
    description=ORCHESTRATOR_INSTRUCTION,
    sub_agents=[
        recommendation_agent,
        admissions_funding_agent,
    ]
)

# The root_agent variable must be set to the main agent instance
root_agent = Education_Guidance_Orchestrator
