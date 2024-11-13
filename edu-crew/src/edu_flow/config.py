import os
from dotenv import load_dotenv

load_dotenv()


LLM_CONFIGS = {
    "openai": {
        "model": "gpt-4o-mini",
        "api_key": os.getenv('OPENAI_API_KEY')
    },
    "groq": {
        "model": "groq/llama3-70b-8192", 
        "api_key": os.getenv('GROQ_API_KEY')
    },
    "anthropic": {
        "model": "anthropic/claude-3-5-sonnet-20240620",
        "api_key": os.getenv('ANTHROPIC_API_KEY')
    },
    "gemini": {
        "model": "gemini/gemini-1.5-flash-002",
        "api_key": os.getenv('GEMINI_API_KEY')
    },
}

LLM_CONFIG = LLM_CONFIGS["gemini"] # Change this to switch between LLMs

EDU_FLOW_INPUT_VARIABLES = {
    "audience_level": "introdutório",
    "topic": "Sistema Multi-agentes com CrewAI"
} 