import re

# 通过 pip install volcengine-python-sdk[ark] 安装方舟SDK
from volcenginesdkarkruntime import Ark

from services.llm_service import LLMService


class ArkService(LLMService):
    def __init__(self, config):
        self.api_url = "https://ark.cn-beijing.volces.com/api/v3"
        self.client = Ark(api_key=config['ARK_API_KEY'])

    def convert_code(self, source_code: str, target_lang: str) -> str:
        prompt = f"""请执行以下任务：
                        1. 自动识别以下代码的编程语言
                        2. 将其转换为{target_lang}代码
                        3. 只返回转换后的代码，不要任何解释

                        原始代码：
                        {source_code}
                        """

        # 创建一个对话请求
        response = self.client.chat.completions.create(
            model="ep-20250218194527-6d6rz",
            messages=[
                {"role": "user",
                 "content": prompt},
            ],
        )

        # 清理响应内容
        # type = response.choices[0].message.content.split("\n")[-1].split(":")[-1].strip()
        # code = response.choices[0].message.content.split("\n")[1:-1]
        print(type)
        code = response.choices[0].message.content
        # print(type, code)
        return re.sub(r'^```.*?\n|\n```$', '', code, flags=re.DOTALL)

    def detect_language(self, source_code: str) -> str:
        prompt = f"""请执行以下任务：
                    1. 自动识别以下代码的编程语言
                    2. 只返回语言类型，不要任何解释

                    原始代码：
                    {source_code}
                    """

        # 创建一个对话请求
        response = self.client.chat.completions.create(
            model="ep-20250218194527-6d6rz",
            messages=[
                {"role": "user",
                 "content": prompt},
            ],
        )

        # 清理响应内容
        type = response.choices[0].message.content
        return re.sub(r'^```.*?\n|\n```$', '', type, flags=re.DOTALL)
