import os


class Config:
    # 数据库配置
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_DB = os.getenv('MYSQL_DB', 'code_converter')
    # LLM 提供商配置
    LLM_PROVIDER = os.getenv('LLM_PROVIDER', 'doubao')  # 可切换提供商
    DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    ARK_API_KEY = os.getenv('ARK_API_KEY')


if __name__ == '__main__':
    config = Config()
    print(config.LLM_PROVIDER)