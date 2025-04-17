import requests
import re
from ..llm_service import LLMService


class DoubaoService(LLMService):
    def __init__(self, config):
        # self.api_url = "https://ark.cn-beijing.volces.com/api/v3"
        self.api_url = "127.0.0.1:11434"
        self.api_key = config['DOUBAO_API_KEY']

    def convert_code(self, source_code: str, target_lang: str) -> str:
        headers = {"Authorization": f"Bearer {self.api_key}"}

        prompt = f"""Convert this code to {target_lang} and return only the code:
                    {source_code}"""

        response = requests.post(
            self.api_url,
            headers=headers,
            json={
                "model": "ep-20250218194527-6d6rz",
                "messages": [{
                    "role": "user",
                    "content": prompt
                }]
            }
        )

        # 清理响应内容
        code = response.json()['choices'][0]['message']['content']
        return re.sub(r'^```.*?\n|\n```$', '', code, flags=re.DOTALL)
