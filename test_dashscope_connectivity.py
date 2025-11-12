#!/usr/bin/env python3
"""
百炼平台网络连通性和 API Key 验证测试
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def test_connectivity():
    """测试网络连通性和 API Key 格式"""
    api_key = os.getenv('OPENAI_API_KEY')
    base_url = os.getenv('OPENAI_BASE_URL')

    print("=" * 60)
    print("百炼平台连通性诊断")
    print("=" * 60)
    print()

    # 检查 API Key 格式
    print("1. API Key 格式检查")
    print("-" * 60)
    print(f"API Key: {api_key}")
    print(f"长度: {len(api_key)}")
    print(f"前缀: {api_key[:3]}")

    if api_key.startswith('sk-'):
        print("✓ API Key 格式看起来正确（sk- 前缀）")
    else:
        print("✗ API Key 格式可能不正确")
    print()

    # 检查网络连通性
    print("2. 网络连通性检查")
    print("-" * 60)
    try:
        # 尝试访问百炼平台域名
        response = requests.get("https://dashscope.aliyuncs.com", timeout=10)
        print(f"✓ 可以访问 dashscope.aliyuncs.com")
        print(f"  状态码: {response.status_code}")
    except Exception as e:
        print(f"✗ 无法访问 dashscope.aliyuncs.com: {e}")
    print()

    # 测试各种可能的端点
    print("3. 尝试各种可能的 API 端点")
    print("-" * 60)

    endpoints = [
        "/chat/completions",
        "/v1/chat/completions",
        "/api/v1/chat/completions",
    ]

    for endpoint in endpoints:
        try:
            url = base_url.rstrip('/') + endpoint if not endpoint.startswith('/v1') else base_url.replace('/compatible-mode/v1', '') + endpoint

            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }

            data = {
                "model": "qwen-plus",
                "messages": [{"role": "user", "content": "hi"}],
                "max_tokens": 10
            }

            response = requests.post(url, headers=headers, json=data, timeout=10)

            print(f"端点: {endpoint}")
            print(f"  完整 URL: {url}")
            print(f"  状态码: {response.status_code}")

            if response.status_code == 200:
                print(f"  ✓ 成功！")
                result = response.json()
                if 'choices' in result:
                    print(f"  回复: {result['choices'][0]['message']['content']}")
                return True
            else:
                print(f"  ✗ 失败: {response.text[:100]}")
            print()

        except Exception as e:
            print(f"端点: {endpoint}")
            print(f"  ✗ 异常: {str(e)[:100]}")
            print()

    print("=" * 60)
    print("\n建议排查：")
    print("1. 登录百炼平台控制台确认 API Key 状态")
    print("2. 检查 API Key 是否已启用")
    print("3. 查看是否需要开通 OpenAI 兼容接口权限")
    print("4. 确认账户余额是否充足")
    print("5. 检查是否有 IP 白名单限制")
    print()
    print("百炼平台控制台: https://bailian.console.aliyun.com/")
    print("=" * 60)

    return False

if __name__ == "__main__":
    test_connectivity()
