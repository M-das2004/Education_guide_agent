🎓 Education Guidance Agent
This is a multi-agent system designed to provide personalized educational recommendations and detailed admissions/funding logistics. It is built using the Google Agent Development Kit (ADK) and structured to process user queries sequentially, ensuring high-quality, grounded, and actionable advice.

🚀 Agent Workflow
The project uses a SequentialAgent orchestrator to manage two specialized sub-agents, ensuring a logical flow from abstract advice to concrete logistics.

RecommendationAgent (LlmAgent):

Input: User's academic profile, career goals, and interests.

Task: Uses Google Search to research and recommend 2-3 specific educational paths (e.g., degree programs, certifications) that align with the user's input.

Output: A detailed recommendation_summary.

AdmissionsFundingAgent (LlmAgent):

Input: The recommendation_summary from the previous agent.

Task: Uses Google Search to find specific admissions requirements, key application deadlines, and available funding/scholarship opportunities for the recommended programs.

Output: A detailed logistics_summary.

EducationGuidanceAgent (SequentialAgent):

Task: Orchestrates the two sub-agents, handles the data handoff, and synthesizes the final combined report for the user.

📁 Project Structure
education_guidance_agent/
├── .env                       # Environment variables for configuration
├── _init_.py                # Module initialization
├── agent.py                   # Contains the main agent definitions and orchestration logic
└── instructions.py            # Contains detailed system prompts for all agents
requirements.txt               # Project dependencies
README.md                      # This file

🛠 Setup and Installation
1. Dependencies
This project requires the following Python packages. They are defined in the requirements.txt file.

google-adk
google-generativeai
python-dotenv

You can install them using pip:

pip install -r requirements.txt

2. Configuration
The agent needs access to the Gemini API and specific model settings, which are configured via the .env file.

Create a file named .env in the education_guidance_agent/ directory with the following content, replacing the placeholder with your actual Google API Key:

GOOGLE_API_KEY=your_google_api_key
GOOGLE_GENAI_MODEL=gemini-2.0-flash
GOOGLE_GENAI_USE_VERTEXAI=FALSE

⚙ Running the Agent
(Instructions on how to run the agent would typically go here once the execution environment is defined, such as via a main script or an ADK runner.)
