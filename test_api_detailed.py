#!/usr/bin/env python3
"""
详细的 API 连接诊断脚本
"""
import os
import requests
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def test_direct_api():
    """直接测试 API 端点"""
    base_url = os.getenv('OPENAI_BASE_URL')
    api_key = os.getenv('OPENAI_API_KEY')

    print("=" * 60)
    print("详细 API 诊断测试")
    print("=" * 60)
    print(f"Base URL: {base_url}")
    print(f"API Key: {api_key[:20]}...")
    print()

    # 测试 1: 直接 HTTP 请求
    print("测试 1: 直接 HTTP 请求到 /v1/models")
    print("-" * 60)
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        # 尝试列出模型
        response = requests.get(
            f"{base_url}/models",
            headers=headers,
            timeout=10
        )

        print(f"状态码: {response.status_code}")
        print(f"响应头: {dict(response.headers)}")
        print(f"响应内容: {response.text[:500]}")

    except Exception as e:
        print(f"错误: {str(e)}")

    print()

    # 测试 2: 测试聊天接口
    print("测试 2: 聊天完成接口")
    print("-" * 60)
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        model = os.getenv('DEFAULT_MODEL', 'gpt-4o-mini')
        data = {
            "model": model,
            "messages": [{"role": "user", "content": "Hello"}],
            "max_tokens": 50
        }
        print(f"使用模型: {model}")

        response = requests.post(
            f"{base_url}/chat/completions",
            headers=headers,
            json=data,
            timeout=30
        )

        print(f"状态码: {response.status_code}")
        if response.status_code == 200:
            print("✓ API 调用成功！")
            print(f"响应: {response.json()}")
        else:
            print(f"✗ API 调用失败")
            print(f"错误信息: {response.text}")

    except Exception as e:
        print(f"错误: {str(e)}")

    print()
    print("=" * 60)

if __name__ == "__main__":
    test_direct_api()
