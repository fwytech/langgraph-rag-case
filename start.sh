#!/bin/bash
# 启动脚本 - 使用 uv 运行 Streamlit 应用

echo "========================================"
echo "  智能客服系统 v2.0"
echo "========================================"
echo ""

# 检查 .env 文件是否存在
if [ ! -f .env ]; then
    echo "警告: .env 文件不存在！"
    echo "请先创建 .env 文件并配置 API 密钥。"
    echo ""
    echo "示例内容："
    echo "OPENAI_BASE_URL=https://api.gptsapi.net/v1"
    echo "OPENAI_API_KEY=sk-your-api-key-here"
    echo ""
    exit 1
fi

# 检查 uv 是否安装
if ! command -v uv &> /dev/null; then
    echo "错误: uv 未安装！"
    echo "请先安装 uv: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# 检查虚拟环境是否存在
if [ ! -d .venv ]; then
    echo "虚拟环境不存在，正在创建..."
    uv sync
fi

# 启动应用
echo "正在启动应用..."
echo ""
uv run streamlit run rag.py
