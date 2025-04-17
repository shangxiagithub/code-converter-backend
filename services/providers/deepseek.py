import requests
import re
import ollama
from ..llm_service import LLMService


class DeepSeekService(LLMService):
    def __init__(self, config):
        # self.api_url = "127.0.0.1:11434/api/chat"
        self.api_url = "http://localhost:11434/api/chat"
        # self.api_url = "https://api.deepseek.com/v1/chat/completions"
        self.api_key = config['DEEPSEEK_API_KEY']

    def convert_code(self, source_code: str, target_lang: str) -> str:
        # content2 = "X先生一周后将去哈尔滨旅游，帮X先生设计一个哈尔滨一日游形成安排。"
        # response = ollama.chat(model = 'qwen2:7b',  #选择模型
        #                       messages = [
        #                         {'role': 'system', 'content': "你是X先生的私人助理，负责X先生的形成安排。"},
        #                         {'role': 'user', 'content': content2}
        #                       ]
        #                      )

        prompt = f"""Convert this {source_code} to {target_lang} and return only the code"""
        # response = ollama.generate(model='deepseek-r1:7b',  # 选择模型
        #                            prompt=prompt)
        response = ollama.generate(model='llama3',  # 选择模型
                                   prompt=prompt)

        # result = response['message']['content']
        resp = response
        # result = response.json().get("message", {}).get("content", "")
        result = response['response']
        print(result)

        # headers = {"Authorization": f"Bearer {self.api_key}"}
        # response = requests.post(
        #     self.api_url,
        #     headers=headers,
        #     json={
        #         "model": "deepseek-r1:7b",
        #         "messages": [{
        #             "role": "user",
        #             "content": prompt
        #         }]
        #     }
        # )

        # 清理响应内容
        # code = response.json()['message']['content']
        # return re.sub(r'^```.*?\n|\n```$', '', code, flags=re.DOTALL)
        return re.sub(r'^```.*?\n|\n```$', '', result, flags=re.DOTALL)
