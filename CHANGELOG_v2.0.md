# v2.0 重构说明

## 📅 更新日期
2024-11-12

## 🎯 重构目标
将项目从传统的 pip 包管理方式迁移到现代的 uv 包管理器，并改进 API 配置管理方式。

## ✨ 主要变更

### 1. 包管理器迁移
- **从**: pip + requirements.txt
- **到**: uv + pyproject.toml
- **优势**:
  - 更快的依赖安装速度（10-100倍）
  - 更可靠的依赖解析
  - 标准化的项目配置

### 2. API 配置管理
- **新增**: `.env` 文件用于存储 API 密钥
- **新增**: `python-dotenv` 依赖
- **修改**: `utils.py` - 自动从环境变量加载 API 配置

**配置方式**:
```bash
# .env 文件
OPENAI_BASE_URL=https://api.gptsapi.net/v1
OPENAI_API_KEY=sk-your-api-key-here
```

### 3. 代码修改详情

#### utils.py
**添加了环境变量加载**:
```python
from dotenv import load_dotenv
load_dotenv()
```

**优化了 API 配置读取**:
- `get_chatllm()`: 现在从环境变量自动读取 base_url 和 api_key
- `get_embedding_model()`: 同样支持环境变量配置

### 4. 新增文件

| 文件 | 说明 |
|-----|------|
| `pyproject.toml` | uv 项目配置文件 |
| `.env` | API 配置文件（已配置实际密钥）|
| `.env.example` | 配置文件模板 |
| `start.sh` | Linux/macOS 启动脚本 |
| `start.bat` | Windows 启动脚本 |
| `test_api.py` | API 连接测试脚本 |
| `CHANGELOG_v2.0.md` | 本变更说明文档 |

### 5. 更新文件

| 文件 | 变更内容 |
|-----|---------|
| `README.md` | 完全重写，详细说明 v2.0 使用方式 |
| `.gitignore` | 添加 .env、uv 相关文件 |
| `utils.py` | 添加 dotenv 支持，优化配置读取 |

## 📦 依赖变更

**新增依赖**:
- `python-dotenv==1.0.0` - 环境变量管理

**所有依赖已在 pyproject.toml 中定义**

## 🚀 快速开始（v2.0）

### 安装依赖
```bash
# 使用 uv（推荐）
uv sync

# 或使用 pip
pip install -r requirements.txt
pip install python-dotenv
```

### 运行项目
```bash
# 使用 uv
uv run streamlit run rag.py

# 或使用启动脚本
./start.sh  # Linux/macOS
start.bat   # Windows

# 或传统方式
source .venv/bin/activate
streamlit run rag.py
```

## 🧪 测试验证

已完成以下测试：

1. ✅ **模块导入测试** - 所有模块可正常导入
2. ✅ **环境变量加载** - .env 文件正确加载
3. ✅ **工具函数测试** - LLM 和 Embedding 模型创建成功
4. ⚠️ **API 连接测试** - 因 API 密钥权限问题，需用户自行验证

## 📝 配置 API 密钥

项目已预配置以下 API 信息：
```
Base URL: https://api.gptsapi.net/v1
API Key: sk-LGMb9526b856efa4d171db6254b740d481f8cd97650FKppy
```

如需更换，请编辑 `.env` 文件。

## 🔄 从 v1.0 迁移

如果您已经在使用 v1.0：

1. **拉取最新代码**
   ```bash
   git pull origin main
   ```

2. **安装 uv**（如果还没有）
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. **安装依赖**
   ```bash
   uv sync
   ```

4. **检查 .env 文件**
   - 确保已创建并配置正确

5. **运行项目**
   ```bash
   uv run streamlit run rag.py
   ```

## 🐛 已知问题

1. **API 访问限制**: 测试时遇到 "Access denied" 错误
   - 可能原因：API 密钥权限限制
   - 解决方案：请联系 API 提供商确认密钥状态

## 📚 参考资料

- [uv 官方文档](https://github.com/astral-sh/uv)
- [python-dotenv 文档](https://github.com/theskumar/python-dotenv)
- [LangChain 文档](https://python.langchain.com/)
- [Streamlit 文档](https://docs.streamlit.io/)

## 👥 贡献者

- 重构执行：Claude Code Assistant
- 需求提出：项目维护者

## 📧 问题反馈

如遇到问题，请：
1. 查看 README.md 中的常见问题
2. 运行 `test_api.py` 诊断 API 配置
3. 在 GitHub 提交 Issue

---

**重构完成时间**: 2024-11-12
**项目状态**: ✅ 重构完成，已通过基础测试
