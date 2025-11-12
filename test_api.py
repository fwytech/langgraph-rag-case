#!/usr/bin/env python3
"""
测试脚本：验证 API 配置是否正确
"""
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def test_api_connection():
    """测试 API 连接"""
    from utils import get_chatllm

    print("=" * 60)
    print("测试 API 连接...")
    print("=" * 60)

    # 显示配置信息
    print(f"API Base URL: {os.getenv('OPENAI_BASE_URL')}")
    print(f"API Key: {os.getenv('OPENAI_API_KEY')[:20]}...")
    print()

    try:
        # 创建 LLM 实例
        llm = get_chatllm('OpenAI', 'gpt-3.5-turbo', temperature=0.1)
        print("✓ LLM 实例创建成功")

        # 测试简单对话
        print("\n测试简单对话...")
        response = llm.invoke("你好，请用一句话介绍自己。")
        print(f"✓ API 响应成功")
        print(f"\n回复内容：{response.content}\n")

        print("=" * 60)
        print("✓ 所有测试通过！API 配置正确。")
        print("=" * 60)
        return True

    except Exception as e:
        print(f"\n✗ 测试失败：{str(e)}")
        print("\n请检查：")
        print("1. .env 文件中的 API 密钥是否正确")
        print("2. API Base URL 是否可访问")
        print("3. 网络连接是否正常")
        return False

if __name__ == "__main__":
    test_api_connection()
