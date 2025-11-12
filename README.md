# 智能客服系统 v3.0

基于 LangGraph + RAG（检索增强生成）技术的智能客服系统，使用 Streamlit 构建 Web 界面。

## ✨ 主要特性

- 🚀 使用 **uv** 包管理器进行依赖管理（更快、更可靠）
- 📝 使用 `.env` 文件管理 API 配置（更安全、更灵活）
- 📦 采用 `pyproject.toml` 标准化项目配置
- 🔧 优化的环境变量加载机制
- 🤖 支持多种 LLM 平台（OpenAI、Ollama、Xinference、阿里云百炼）
- 📚 基于 Chroma 的向量知识库管理

## 📋 系统要求

- Python >= 3.10
- uv 包管理器（推荐）或 pip

## 🚀 快速开始

### 1. 安装 uv 包管理器（如果还未安装）

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. 克隆项目

```bash
git clone https://github.com/fwytech/langgraph-rag-case.git
cd langgraph-rag-case
```

### 3. 配置 API 密钥

编辑 `.env` 文件（已存在），或创建一个新的：

```bash
# .env 文件内容
OPENAI_BASE_URL=https://api.gptsapi.net/v1
OPENAI_API_KEY=sk-your-api-key-here
DEFAULT_MODEL=gpt-3.5-turbo
DEFAULT_TEMPERATURE=0.1
```

**⚠️ 重要：请勿将 `.env` 文件提交到版本控制系统！**

### 4. 安装依赖

使用 uv（推荐）：

```bash
uv sync
```

或使用传统 pip 方式：

```bash
pip install -r requirements.txt
pip install python-dotenv
```

### 5. 运行项目

使用 uv：

```bash
uv run streamlit run rag.py
```

或使用传统方式：

```bash
# 激活虚拟环境（如果使用 uv sync 安装）
source .venv/bin/activate  # Linux/macOS
# 或
.venv\Scripts\activate  # Windows

# 运行应用
streamlit run rag.py
```

### 6. 访问应用

浏览器自动打开 http://localhost:8501

## 📚 功能特性

### 1. 智能客服对话
- 基于 LangGraph 的对话流程管理
- 支持多轮对话和上下文记忆
- 实时显示知识库检索过程
- 流式输出，体验流畅

### 2. 知识库管理
- 创建自定义知识库
- 上传 Markdown 文档
- 自动文档分块和向量化
- 基于 Chroma 的向量存储

### 3. 多模型支持
- **OpenAI**: GPT-4o, GPT-3.5-turbo（默认）
- **Ollama**: 本地部署开源模型
- **Xinference**: 多种模型托管平台

### 4. 灵活配置
- Temperature 控制：0.1-1.0
- 历史消息长度：1-10 轮
- 多知识库同时使用

## 📖 使用指南

### 创建知识库

1. 点击侧边栏 "行业知识库"
2. 选择 "新建知识库"
3. 输入知识库名称（英文，如：bank）
4. 选择 Embedding 模型
5. 点击 "创建知识库"

### 上传文档

1. 选择已创建的知识库
2. 上传 Markdown 文档（支持批量上传）
3. 系统自动处理并向量化

### 开始对话

1. 点击 "智能客服" 页面
2. 在侧边栏选择要使用的知识库
3. 配置模型参数（可选）
4. 输入问题，开始对话

### 示例问题

项目自带银行客服知识库，可以尝试以下问题：

- 如何查询账户余额？
- 如何修改账户密码？
- 如何进行转账操作？
- 信用卡怎么申请？

## 🏗️ 项目结构

```
langgraph-rag-case/
├── rag.py                    # 主入口文件
├── utils.py                  # 工具函数
├── pyproject.toml            # 项目配置（uv 标准格式）
├── requirements.txt          # 依赖列表（兼容传统方式）
├── .env                      # 环境变量配置（需自行配置）
├── tools/                    # RAG 工具模块
│   └── naive_rag_tool.py    # RAG 检索工具
├── webui/                    # Web 界面
│   ├── rag_chat_page.py     # 对话页面
│   └── knowledge_base_page.py # 知识库管理页面
├── kb/                       # 知识库存储
│   └── bank/                # 示例：银行知识库
│       ├── files/           # 原始文档
│       └── vectorstore/     # 向量数据
└── img/                      # UI 资源
```

## 🔧 技术栈

- **LangChain & LangGraph**: 对话流程编排
- **Streamlit**: Web UI 框架
- **Chroma**: 向量数据库
- **OpenAI API**: LLM 服务
- **uv**: 现代 Python 包管理器

## 🛠️ 开发相关

### 添加新依赖

使用 uv：

```bash
uv add package-name
```

或手动编辑 `pyproject.toml`，然后运行：

```bash
uv sync
```

### 更新依赖

```bash
uv sync --upgrade
```

### 虚拟环境管理

uv 会自动在项目根目录创建 `.venv` 虚拟环境。

激活虚拟环境：

```bash
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

## ❓ 常见问题

### Q: 如何更换 API 服务商？

A: 编辑 `.env` 文件，修改 `OPENAI_BASE_URL` 和 `OPENAI_API_KEY`。

### Q: 支持哪些文档格式？

A: 当前版本支持 Markdown (.md) 格式。

### Q: 如何调整检索精度？

A: 编辑 `tools/naive_rag_tool.py`，修改 `score_threshold` 参数（默认 0.15）。

### Q: uv 和 pip 有什么区别？

A: uv 是用 Rust 编写的现代 Python 包管理器，比 pip 快 10-100 倍，依赖解析更可靠。

## 📝 版本历史

### v2.0.0 (2024-11)
- 迁移到 uv 包管理器
- 使用 .env 文件管理配置
- 标准化项目结构

### v1.0.0
- 初始版本
- 基础 RAG 功能
- Streamlit UI

## 📄 许可证

本项目仅供学习和研究使用。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📧 联系方式

如有问题，请访问 https://github.com/fwytech/langgraph-rag-case
