from abc import ABC, abstractmethod


class LLMService(ABC):
    @abstractmethod
    def convert_code(self, source_code: str, target_lang: str) -> str:
        pass

    # @abstractmethod
    def detect_language(self, source_code: str) -> str:
        pass


class LLMProviderFactory:
    @staticmethod
    def create_service(config) -> LLMService:
        if config['LLM_PROVIDER'] == 'deepseek':
            from .providers.deepseek import DeepSeekService
            return DeepSeekService(config)
        elif config['LLM_PROVIDER'] == 'openai':
            from .providers.openai import OpenAIService
            return OpenAIService(config)
        elif config['LLM_PROVIDER'] == 'ark':
            from .providers.ark import ArkService
            return ArkService(config)
        raise ValueError("Unsupported LLM provider")
