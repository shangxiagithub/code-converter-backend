import openai
from ..llm_service import LLMService


class OpenAIService(LLMService):
    def __init__(self, config):
        openai.api_key = config.OPENAI_API_KEY

    def convert_code(self, source_code: str, target_lang: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{
                "role": "user",
                "content": f"Convert this to {target_lang} code:\n{source_code}"
            }]
        )
        return response.choices[0].message.content
