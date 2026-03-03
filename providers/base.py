from abc import ABC, abstractmethod
from core.models import ModelResponse


class BaseProvider(ABC):
    @abstractmethod
    def get_available_models(self) -> dict[str, str]:
        """Return {display_name: model_id} for this provider."""
        pass

    @abstractmethod
    async def call_model(
        self,
        model_id: str,
        model_display_name: str,
        prompt: str,
    ) -> ModelResponse:
        """Call the model and return a full populated ModelResponse."""
        pass