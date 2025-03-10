如何配置 GitHub Secrets
进入你的 GitHub 仓库。

点击 Settings > Secrets and variables > Actions > Secrets。

添加以下 Secrets：
AZURE_CLIENT_ID: 你的客户端 ID

AZURE_TENANT_ID: 你的租户 ID

AZURE_CLIENT_SECRET: 你的客户端密钥

注意事项
权限问题：
如果 API 调用返回 403（权限不足），需要在 Azure AD 中为你的应用添加相应的 Microsoft Graph API 权限（例如 User.Read），并确保管理员已授予同意。

运行频率：
GitHub Actions 的免费套餐有运行时间限制（每月 2000 分钟），频繁调度可能会超出配额。

替代方案：
如果需要更长时间或更灵活的调度，建议将代码部署到云服务（如 Azure Functions 或 AWS Lambda），而不是依赖 GitHub Actions。

