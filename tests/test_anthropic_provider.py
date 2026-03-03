import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from providers.anthropic_provider import AnthropicProvider

async def test():
    p = AnthropicProvider()
    print("Provider name:", p.provider_name)
    print("Available models:", p.get_available_models())

    result = await p.call_model(
        model_id="claude-haiku-4-5-20251001",
        model_display_name="Claude Haiku 4.5",
        prompt="In one sentence, what is 2+2 and why?"
    )
    
    print("Response:", result.response)
    print("Latency:", result.latency_seconds)
    print("Tokens in/out:", result.input_tokens, "/", result.output_tokens)
    print("Error:", result.error)

asyncio.run(test())