@echo off
REM 启动脚本 - 使用 uv 运行 Streamlit 应用（Windows版）

echo ========================================
echo   智能客服系统 v2.0
echo ========================================
echo.

REM 检查 .env 文件是否存在
if not exist .env (
    echo 警告: .env 文件不存在！
    echo 请先创建 .env 文件并配置 API 密钥。
    echo.
    echo 示例内容：
    echo OPENAI_BASE_URL=https://api.gptsapi.net/v1
    echo OPENAI_API_KEY=sk-your-api-key-here
    echo.
    pause
    exit /b 1
)

REM 检查 uv 是否安装
where uv >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo 错误: uv 未安装！
    echo 请先安装 uv: powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    pause
    exit /b 1
)

REM 检查虚拟环境是否存在
if not exist .venv (
    echo 虚拟环境不存在，正在创建...
    uv sync
)

REM 启动应用
echo 正在启动应用...
echo.
uv run streamlit run rag.py
