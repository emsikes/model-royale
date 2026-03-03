import os
from dotenv import load_dotenv

load_dotenv(override=True)

# API Keys and Model Endpoints
ANTHROPIC_API_KEY=os.getenv("ANTHROPIC_API_KEY", "")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY", "")
OPENROUTER_API_KEY=os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
OLLAMA_BASE_URL=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

# Judge configuration
JUDGE_PROVIDER=os.getenv("JUDGE_PROVIDER", "anthropic")
JUDGE_MODEL=os.getenv("JUDGE_MODEL", "claude-haiku-4-5-20251001")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "2048"))

# Available models per provider (display name → model ID)
ANTHROPIC_MODELS = {
    "Claude Sonnet 4.6":  "claude-sonnet-4-6",
    "Claude Opus 4.6":    "claude-opus-4-6",
    "Claude Haiku 4.5":   "claude-haiku-4-5-20251001",
    "Claude Sonnet 4.5":  "claude-sonnet-4-5-20251022",
}

OPENAI_MODELS = {
    "GPT-4o Mini":   "gpt-4o-mini",
    "GPT-4o":        "gpt-4o",
    "GPT-5.2":       "gpt-5.2",
}

OPENROUTER_MODELS = {
    "Gemini 2.5 Flash":   "google/gemini-2.5-flash",
    "Llama 3.3 70B":      "meta-llama/llama-3.3-70b-instruct",
    "Mistral Medium 3":   "mistralai/mistral-medium-3",
    "DeepSeek R1":        "deepseek/deepseek-r1",
    "Grok 2":             "x-ai/grok-2-1212",
}

OLLAMA_MODELS = {
    "GPT-OSS 20B":       "gpt-oss:20b",
    "Gemma3 27B":        "gemma3:27b",
    "Gemma3 270M":       "gemma3:270m",
    "Llama 3.1 8B":      "llama3.1:8b",
    "Llama 3.2":         "llama3.2:latest",
    "Llama 3.2 Vision":  "llama3.2-vision:latest",
}

# Evaluation modes
EVAL_MODES = ["1v1", "Arena (up to 5)"]
ARENA_MAX_MODELS = 5