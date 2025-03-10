import requests
import msal
import os
from datetime import datetime

# 从环境变量获取 Azure AD 配置
client_id = os.getenv("AZURE_CLIENT_ID")
tenant_id = os.getenv("AZURE_TENANT_ID")
client_secret = os.getenv("AZURE_CLIENT_SECRET")
authority = f"https://login.microsoftonline.com/{tenant_id}"
scope = ["https://graph.microsoft.com/.default"]

# 获取访问令牌的函数
def get_access_token():
    app = msal.ConfidentialClientApplication(
        client_id,
        authority=authority,
        client_credential=client_secret
    )
    result = app.acquire_token_for_client(scopes=scope)
    if "access_token" in result:
        return result["access_token"]
    else:
        raise Exception("无法获取访问令牌: ", result.get("error_description"))

# 调用 Microsoft Graph API 的函数
def call_graph_api():
    try:
        # 获取访问令牌
        access_token = get_access_token()
        
        # Microsoft Graph API 端点：获取当前用户信息
        endpoint = "https://graph.microsoft.com/v1.0/me"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        
        # 发送请求
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()  # 如果请求失败，抛出异常
        
        # 解析并打印结果
        user_data = response.json()
        print(f"[{datetime.now()}] API 调用成功！用户信息：")
        print(f"显示名称: {user_data.get('displayName')}")
        print(f"邮箱: {user_data.get('mail')}")
        print(f"用户ID: {user_data.get('id')}")
        
        # 可选：将结果保存到文件
        with open("user_data.txt", "a") as f:
            f.write(f"[{datetime.now()}] {user_data}\n")
            
    except requests.exceptions.RequestException as e:
        print(f"[{datetime.now()}] API 调用失败: {e}")
        raise  # 抛出异常以让 GitHub Actions 标记为失败
    except Exception as e:
        print(f"[{datetime.now()}] 错误: {e}")
        raise

# 主程序入口
if __name__ == "__main__":
    print(f"[{datetime.now()}] 开始调用 Microsoft Graph API...")
    call_graph_api()
