import requests
import json

# 测试聊天 API
url = "http://localhost:8001/api/v1/chat/stream"

# 测试请求 1: 缺少 thread_id
print("测试请求 1: 缺少 thread_id")
data1 = {
    "messages": "你好"
}
try:
    response = requests.post(url, json=data1)
    print(f"状态码: {response.status_code}")
    print(f"响应: {response.json()}")
except Exception as e:
    print(f"错误: {e}")

print("\n" + "-"*50 + "\n")

# 测试请求 2: 缺少 messages
print("测试请求 2: 缺少 messages")
data2 = {
    "thread_id": "test123"
}
try:
    response = requests.post(url, json=data2)
    print(f"状态码: {response.status_code}")
    print(f"响应: {response.json()}")
except Exception as e:
    print(f"错误: {e}")

print("\n" + "-"*50 + "\n")

# 测试请求 3: 正确格式
print("测试请求 3: 正确格式")
data3 = {
    "thread_id": "test123",
    "messages": "你好"
}
try:
    response = requests.post(url, json=data3)
    print(f"状态码: {response.status_code}")
    print(f"响应: {response.json()}")
except Exception as e:
    print(f"错误: {e}")