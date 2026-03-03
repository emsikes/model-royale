from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime


@dataclass
class ModelResponse:
    # Identity
    provider: str               # "anthropic", "openai", "ollama"
    model_id: str               # actual model string that we send to the API
    model_display_name: str     # shortened meaningfull name for display in the UI

    # Content
    prompt: str                 # input prompt
    response: str                # the model's response text

    # Metrics
    latency_seconds: float      # actual time for the API call
    input_tokens: int = 0       # tokens consumed by the prompt
    output_tokens: int = 0      # tokens consumed by the response

    # Judge scores
    judge_score: Optional[float] = None     # 0.0 - 10.0
    judge_reasoning: Optional[str] = None   # judge explanation

    # Metadata
    timestamp: datetime = field(default_factory=datetime.now)
    error: Optional[str] = None         # Populated if the API call fails

