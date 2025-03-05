import requests
import re
from ..llm_service import LLMService


class DeepSeekService(LLMService):
    def __init__(self, config):
        self.api_url = "https://api.deepseek.com/v1/chat/completions"
        self.api_key = config.DEEPSEEK_API_KEY

    def convert_code(self, source_code: str, target_lang: str) -> str:
        headers = {"Authorization": f"Bearer {self.api_key}"}

        prompt = f"""Convert this code to {target_lang} and return only the code:
{source_code}"""

        response = requests.post(
            self.api_url,
            headers=headers,
            json={
                "model": "deepseek-coder-33b-instruct",
                "messages": [{
                    "role": "user",
                    "content": prompt
                }]
            }
        )

        # 清理响应内容
        code = response.json()['choices'][0]['message']['content']
        return re.sub(r'^```.*?\n|\n```$', '', code, flags=re.DOTALL)