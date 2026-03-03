import time
import anthropic
import config
from core.models import ModelResponse
from providers.base import BaseProvider


class AnthropicProvider(BaseProvider):

    def __init__(self):
        self.client = anthropic.Anthropic(api_key=config.ANTHROPIC_API_KEY)
        self.provider_name = "anthropic"

    def get_available_models(self) -> dict[str, str]:
        return config.ANTHROPIC_MODELS

    async def call_model(
            self, 
            model_id: str, 
            model_display_name: str, 
            prompt: str
            ) -> ModelResponse:
        start_time = time.time()
        try:
            message = self.client.messages.create(
                model=model_id,
                max_tokens=config.MAX_TOKENS,
                messages=[{"role": "user", "content": prompt}]
            )
            latency = time.time() - start_time
            return ModelResponse(
                provider=self.provider_name,
                model_id=model_id,
                model_display_name=model_display_name,
                prompt=prompt,
                response=message.content[0].text,
                latency_seconds=round(latency, 3),
                input_tokens=message.usage.input_tokens,
                output_tokens=message.usage.output_tokens,
            )
        except Exception as e:
            return ModelResponse(
                provider=self.provider_name,
                model_id=model_id,
                model_display_name=model_display_name,
                prompt=prompt,
                response="",
                latency_seconds=round(time.time() - start_time, 3),
                error=str(e)
            )
        