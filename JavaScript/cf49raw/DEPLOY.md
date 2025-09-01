# Vercel 部署详细教程

本文档将详细介绍如何将 GitHub 私有仓库原始文件代理服务部署到 Vercel 平台。

## 前置要求

1. GitHub 账号
2. Vercel 账号（可以使用 GitHub 账号直接登录）
3. GitHub Personal Access Token（用于访问私有仓库）
4. 自定义的访问令牌（用于保护您的代理服务）

## 步骤 1：准备 GitHub Personal Access Token

1. 访问 GitHub 的 [Personal Access Tokens 页面](https://github.com/settings/tokens)
2. 点击 "Generate new token" 按钮
3. 选择适当的权限范围（至少需要 `repo` 权限以访问私有仓库）
4. 生成并复制 token（请妥善保管，只会显示一次）

## 步骤 2：准备自定义访问令牌

生成一个复杂的安全令牌，用于保护您的代理服务不被未授权访问。可以使用密码生成器或以下命令生成：

```bash
openssl rand -base64 32
```

## 步骤 3：准备项目文件

确保您拥有以下文件结构：

```
cf49raw/
├── api/
│   └── vercel-github-raw.js
├── vercel.json
```

## 步骤 4：通过 GitHub 部署（推荐）

### 4.1：将项目推送到 GitHub

1. 在 GitHub 上创建一个新的仓库（例如：`vercel-github-proxy`）
2. 将本地项目推送到该仓库：

```bash
cd cf49raw
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/vercel-github-proxy.git
git branch -M main
git push -u origin main
```

### 4.2：连接到 Vercel

1. 访问 [Vercel 官网](https://vercel.com/) 并使用 GitHub 账号登录
2. 点击 "New Project"
3. 选择您刚刚创建的仓库
4. 在项目设置中，配置以下环境变量：
   - `NINE49TOKEN` = 您在步骤 2 中生成的自定义访问令牌
   - `GITHUB49TOKEN` = 您在步骤 1 中生成的 GitHub Personal Access Token
5. 点击 "Deploy" 开始部署

## 步骤 5：通过 Vercel CLI 部署

### 5.1：安装 Vercel CLI

```bash
npm install -g vercel
```

### 5.2：登录 Vercel

```bash
vercel login
```

### 5.3：部署项目

```bash
cd cf49raw
vercel
```

按照提示操作：

1. 设置项目名称（例如：`vercel-github-proxy`）
2. 设置项目根目录（当前目录）
3. 配置环境变量：
   ```bash
   vercel env add NINE49TOKEN
   vercel env add GITHUB49TOKEN
   ```
   输入对应的值（注意：这些值不会在终端中显示）

## 步骤 6：测试部署

部署完成后，Vercel 会提供一个 URL（例如：`https://vercel-github-proxy.vercel.app`）。

使用以下格式访问私有仓库中的文件：

```
https://your-vercel-url.vercel.app/用户名/仓库名/文件路径?nine-token=您的自定义令牌
```

例如：

```
https://vercel-github-proxy.vercel.app/username/private-repo/README.md?nine-token=your-secret-token
```

## 路径处理说明

URL 路径结构遵循 GitHub 原始文件 URL 的格式：

- `/用户名/仓库名/分支名/文件路径` - 访问特定分支中的文件
- `/用户名/仓库名/commit哈希/文件路径` - 访问特定提交中的文件

例如：

- `/Nine499/mihomo-yaml/master/节点/机场/bocchi.yaml` - 访问 Nine499 用户的 mihomo-yaml 仓库中 master 分支下的文件

## 故障排除

### 环境变量未设置

如果遇到权限问题，请检查环境变量是否正确设置：

- 确保 `NINE49TOKEN` 与请求中的 `nine-token` 参数匹配
- 确保 `GITHUB49TOKEN` 具有访问目标仓库的权限

### 访问被重定向到百度

如果请求被重定向到百度，可能是以下原因之一：

- `nine-token` 参数不正确或缺失
- 环境变量未正确配置
- GitHub Personal Access Token 权限不足或已过期

### 访问被重定向到 GitHub 首页

如果提供了正确的 `nine-token` 但被重定向到 GitHub 首页，可能是：

- URL 路径不正确或缺失
- 路径参数未正确传递给 API 函数

### GitHub API 限制

如果遇到 GitHub API 速率限制，可以考虑：

- 使用多个 GitHub Personal Access Token 轮换使用
- 增加 token 的权限范围
- 检查 GitHub 的速率限制文档

## 安全建议

1. 定期更换 `GITHUB49TOKEN` 和 `NINE49TOKEN`
2. 限制 GitHub Personal Access Token 的权限范围
3. 不要在客户端代码或公共仓库中暴露这些令牌
4. 监控 Vercel 项目的访问日志
5. 考虑添加额外的安全层，如 IP 白名单
