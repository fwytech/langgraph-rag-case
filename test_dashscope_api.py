#!/usr/bin/env python3
"""
百炼平台专用 API 测试脚本
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def test_dashscope_api():
    """测试阿里云百炼平台 API"""
    base_url = os.getenv('OPENAI_BASE_URL')
    api_key = os.getenv('OPENAI_API_KEY')
    model = os.getenv('DEFAULT_MODEL', 'qwen-plus')

    print("=" * 60)
    print("阿里云百炼平台 API 测试")
    print("=" * 60)
    print(f"Base URL: {base_url}")
    print(f"API Key: {api_key[:20]}...")
    print(f"Model: {model}")
    print()

    # 测试 1: 标准 OpenAI 兼容格式
    print("测试 1: OpenAI 兼容格式")
    print("-" * 60)
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "model": model,
            "messages": [
                {"role": "user", "content": "你好"}
            ]
        }

        response = requests.post(
            f"{base_url}/chat/completions",
            headers=headers,
            json=data,
            timeout=30
        )

        print(f"状态码: {response.status_code}")

        if response.status_code == 200:
            result = response.json()
            print("✓ API 调用成功！")
            print(f"\n回复内容: {result['choices'][0]['message']['content']}")
        else:
            print(f"✗ API 调用失败")
            print(f"错误信息: {response.text}")

    except Exception as e:
        print(f"✗ 请求异常: {str(e)}")

    print()

    # 测试 2: 尝试不同的认证方式
    print("测试 2: 使用 X-DashScope-SSE 头")
    print("-" * 60)
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "X-DashScope-SSE": "disable"
        }

        data = {
            "model": model,
            "messages": [
                {"role": "user", "content": "你好"}
            ]
        }

        response = requests.post(
            f"{base_url}/chat/completions",
            headers=headers,
            json=data,
            timeout=30
        )

        print(f"状态码: {response.status_code}")

        if response.status_code == 200:
            result = response.json()
            print("✓ API 调用成功！")
            print(f"\n回复内容: {result['choices'][0]['message']['content']}")
        else:
            print(f"✗ API 调用失败")
            print(f"错误信息: {response.text}")

    except Exception as e:
        print(f"✗ 请求异常: {str(e)}")

    print()

    # 测试 3: 使用 LangChain 调用
    print("测试 3: 使用 LangChain ChatOpenAI")
    print("-" * 60)
    try:
        from langchain_openai import ChatOpenAI

        llm = ChatOpenAI(
            model=model,
            openai_api_base=base_url,
            openai_api_key=api_key,
            temperature=0.1
        )

        print("✓ ChatOpenAI 实例创建成功")

        response = llm.invoke("你好，请简单介绍一下你自己")

        print("✓ LangChain 调用成功！")
        print(f"\n回复内容: {response.content}")

    except Exception as e:
        print(f"✗ LangChain 调用失败: {str(e)}")

    print()
    print("=" * 60)

if __name__ == "__main__":
    test_dashscope_api()
