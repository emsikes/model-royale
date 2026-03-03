# ModelRoyale 🏆
### *Head to head LLM Evaluation App.*

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)
![Gradio](https://img.shields.io/badge/Gradio-4.x-FF7C00?style=flat&logo=gradio&logoColor=white)
![Anthropic](https://img.shields.io/badge/Anthropic-Claude-191919?style=flat&logo=anthropic&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=flat&logo=openai&logoColor=white)
![OpenRouter](https://img.shields.io/badge/OpenRouter-Multi--Model-6366F1?style=flat&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Local-grey?style=flat&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-E92063?style=flat&logo=pydantic&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=flat&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active%20Development-green?style=flat)

A side-by-side LLM evaluation harness for comparing model responses across providers, with automated LLM-as-judge scoring, latency/token metrics, session leaderboards, and CSV/JSON export.

Built as a personal portfolio project to explore multi-provider inference, async orchestration, and evaluation methodology.

---

## Features

- **1v1 and Arena modes** — compare 2 models head-to-head or run up to 5 simultaneously
- **Multi-provider support** — Anthropic, OpenAI, OpenRouter, and Ollama (local)
- **LLM-as-judge scoring** — automated 0–10 scoring with reasoning explanations
- **Latency + token metrics** — wall-clock timing and token counts per model per run
- **Session leaderboard** — aggregated win rates and average scores across all runs
- **Export** — download full session history as CSV or JSON

---

## Supported Providers

| Provider | Models |
|---|---|
| Anthropic | Claude 3.5 Haiku, Claude 3.5 Sonnet, Claude 3 Opus |
| OpenAI | GPT-4o Mini, GPT-4o, GPT-4 Turbo |
| OpenRouter | Gemini Flash 2.0, Llama 3.3 70B, Mistral Large, DeepSeek R1, Grok 2 |
| Ollama | Any locally running model (fetched dynamically) |

---

## Tech Stack

- **Python 3.11**
- **Gradio** — UI
- **Anthropic / OpenAI SDKs** — provider clients
- **Ollama** — local model inference
- **Pydantic + dataclasses** — data modeling
- **Pandas** — session data + export
- **asyncio / httpx** — parallel inference

---

## Project Structure

```
model-royale/
├── app.py                  # entry point
├── config.py               # all provider configs and model lists
├── providers/
│   ├── base.py             # abstract provider interface
│   ├── anthropic_provider.py
│   ├── openai_provider.py
│   ├── openrouter_provider.py
│   ├── ollama_provider.py
│   └── registry.py         # dynamic provider/model loader
├── core/
│   ├── models.py           # ModelResponse dataclass
│   ├── engine.py           # parallel async inference
│   ├── judge.py            # LLM-as-judge scoring
│   ├── session_log.py      # run history
│   ├── leaderboard.py      # aggregated stats
│   └── export.py           # CSV/JSON export
├── ui/
│   ├── layout.py           # Gradio layout + mode selector
│   ├── results.py          # response grid (1v1 + Arena)
│   └── leaderboard_view.py # scores + leaderboard tab
└── tests/
```

---

## Setup

```bash
# Clone and enter
git clone https://github.com/yourusername/model-royale.git
cd model-royale

# Pin Python version (requires pyenv)
pyenv local 3.11.9

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your API keys
```

---

## Configuration

Copy `.env.example` to `.env` and populate:

```
ANTHROPIC_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
OPENROUTER_API_KEY=your_key_here
OLLAMA_BASE_URL=http://localhost:11434
JUDGE_PROVIDER=anthropic
JUDGE_MODEL=claude-3-5-haiku-20241022
MAX_TOKENS=2048
```

For Ollama, ensure the Ollama server is running locally before launching the app.

---

## Running the App

```bash
python app.py
```

Navigate to `http://localhost:7860` in your browser.

---

## Status

> 🚧 **Active development** — built step-by-step as a learning and portfolio project.

- [x] Project scaffold + config
- [x] ModelResponse data contract
- [x] Abstract base provider
- [ ] Provider implementations (Anthropic, OpenAI, OpenRouter, Ollama)
- [ ] Inference engine
- [ ] LLM-as-judge
- [ ] Gradio UI
- [ ] Session leaderboard + export

---

## Author

**Matt** — Principal Architect specializing in AI/ML infrastructure, healthcare IT, and cloud architecture.

- Built as part of an active AI engineering portfolio
- Reach out via [LinkedIn](#) or [GitHub](#)
