import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.models import ModelResponse

r = ModelResponse(
    provider="anthropic",
    model_id="claude-3-5-haiku-20241022",
    model_display_name="Claude 3.5 Haiku",
    prompt="Hello",
    response="Hi there",
    latency_seconds=1.23
)
print(r.provider, r.latency_seconds, r.judge_score)