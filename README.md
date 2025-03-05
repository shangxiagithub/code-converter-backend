#### 项目名称
智能代码转换工具

#### 项目简介
智能代码转换工具是一个基于Flask框架的Web应用程序，旨在帮助用户将一种编程语言的代码转换为另一种编程语言。该工具支持多种大语言模型（LLM）提供商，并提供历史记录查看功能。

#### 目录结构
```plaintext
code-converter/
├── app.py                # 应用入口
├── config.py             # 配置管理
├── database.sql          # 数据库初始化SQL脚本
├── requirements.txt      # 依赖清单
├── services/
│   ├── __init__.py
│   ├── llm_service.py    # 大语言模型服务抽象层
│   └── providers/        # 各厂商API实现
│       ├── deepseek.py
│       └── openai.py
├── models/
│   ├── __init__.py
│   └── conversion.py     # 数据模型及DAO
├── routes/
│   ├── __init__.py
│   ├── converter.py      # 转换相关路由
│   └── history.py        # 历史记录路由
├── static/
│   └── style.css         # 样式文件
└── templates/
    ├── index.html        # 主页面模板
    └── history.html      # 历史记录页面模板
```


#### 环境配置
1. **安装依赖**
   使用以下命令安装项目所需的Python包：
   ```bash
   pip install -r requirements.txt
   ```


2. **配置环境变量**
   在`.env`文件中配置必要的环境变量，或直接在系统环境中设置：
   ```plaintext
   MYSQL_HOST=localhost
   MYSQL_USER=root
   MYSQL_PASSWORD=your_password
   MYSQL_DB=code_converter
   LLM_PROVIDER=doubao
   DEEPSEEK_API_KEY=your_deepseek_api_key
   OPENAI_API_KEY=your_openai_api_key
   ARK_API_KEY=your_ark_api_key
   ```


3. **初始化数据库**
   使用提供的`database.sql`脚本创建和初始化数据库表。

#### 运行应用
1. **启动虚拟环境**
   激活虚拟环境：
   ```bash
   source venv/bin/activate
   ```


2. **运行应用**
   使用以下命令启动Flask应用：
   ```bash
   python app.py
   ```


3. **访问应用**
   打开浏览器并访问`http://127.0.0.1:5000`以使用智能代码转换工具。

#### 功能模块说明
- **app.py**: 应用程序的入口文件，负责创建Flask应用实例并注册蓝图。
- **config.py**: 包含应用程序的配置项，如数据库连接信息和大语言模型提供商的API密钥。
- **services/**: 包含大语言模型服务的抽象层和各提供商的具体实现。
- **models/**: 包含数据模型和数据库访问对象（DAO），用于与数据库交互。
- **routes/**: 包含处理HTTP请求的路由逻辑，分为转换相关路由和历史记录路由。
- **static/**: 包含静态资源文件，如CSS样式文件。
- **templates/**: 包含HTML模板文件，用于渲染前端页面。

#### 技术栈
- **后端**: Python, Flask
- **前端**: HTML, CSS
- **数据库**: MySQL
- **大语言模型**: 支持DeepSeek、OpenAI等提供商

#### 开发者指南
- **添加新功能**: 修改`routes/`目录下的路由文件以添加新的功能。
- **切换LLM提供商**: 修改`config.py`中的`LLM_PROVIDER`环境变量值以切换不同的大语言模型提供商。
- **扩展数据库功能**: 修改`models/conversion.py`中的`ConversionDAO`类以扩展数据库操作功能。

#### 贡献者
欢迎任何开发者为项目贡献代码或提出改进建议。请遵循项目的开发规范并确保提交的代码质量。

#### 许可证
本项目采用MIT许可证，详情参见LICENSE文件。

---

希望这个README文档能帮助你更好地理解和使用智能代码转换工具。如果有任何问题或建议，请随时联系项目维护者。