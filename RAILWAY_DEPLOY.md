# Railway 部署指南

本指南将帮助你将加密货币交易监控面板部署到Railway平台。

## 🚀 快速部署步骤

### 1. 准备工作

#### 1.1 创建Railway账户
- 访问 [Railway.app](https://railway.app)
- 使用GitHub账户登录
- 完成账户验证

#### 1.2 准备代码仓库
确保你的代码已经推送到GitHub仓库，包含以下文件：
- `Dockerfile` - 容器化配置
- `railway.json` - Railway部署配置
- `requirements.txt` - Python依赖
- `dashboard.py` - 主应用文件

### 2. 部署到Railway

#### 2.1 创建新项目
1. 登录Railway控制台
2. 点击 "New Project"
3. 选择 "Deploy from GitHub repo"
4. 选择你的代码仓库
5. 点击 "Deploy Now"

#### 2.2 配置环境变量（可选）
如果需要配置API密钥或其他敏感信息：
1. 在项目设置中找到 "Variables" 标签
2. 添加必要的环境变量：
   ```
   EXCHANGE_API_KEY=your_api_key
   EXCHANGE_SECRET=your_secret
   ```

#### 2.3 等待部署完成
- Railway会自动检测到Dockerfile并开始构建
- 构建过程通常需要2-5分钟
- 部署完成后会显示访问URL

### 3. 访问应用

部署成功后，你可以通过以下方式访问：
- Railway提供的HTTPS URL
- 应用会自动在端口8501上运行
- 支持HTTPS和自定义域名

## 🔧 配置说明

### 3.1 端口配置
Railway会自动设置`PORT`环境变量，应用会监听该端口：
```python
import os
port = int(os.environ.get("PORT", 8501))
```

### 3.2 内存和CPU限制
- Railway免费版：512MB RAM, 0.5 vCPU
- 付费版：更多资源可选

### 3.3 自动重启
- 应用崩溃时会自动重启
- 最多重试10次
- 健康检查路径：`/`

## 📊 监控和日志

### 4.1 查看日志
1. 在Railway控制台选择你的项目
2. 点击 "Deployments" 标签
3. 选择最新的部署
4. 查看实时日志

### 4.2 性能监控
- CPU和内存使用情况
- 网络流量统计
- 响应时间监控

## 🛠️ 故障排除

### 5.1 常见问题

#### 构建失败
- 检查Dockerfile语法
- 确认requirements.txt中的依赖版本
- 查看构建日志中的错误信息

#### 应用无法启动
- 检查端口配置
- 确认环境变量设置
- 查看应用日志

#### 内存不足
- 优化代码减少内存使用
- 升级到付费计划
- 调整应用配置

### 5.2 调试技巧
1. 使用`simple_dashboard.py`进行测试
2. 在本地使用Docker测试：
   ```bash
   docker build -t crypto-dashboard .
   docker run -p 8501:8501 crypto-dashboard
   ```

## 🔄 更新部署

### 6.1 自动部署
- 推送到GitHub主分支会自动触发部署
- 每次提交都会创建新的部署版本

### 6.2 手动部署
1. 在Railway控制台点击 "Deploy"
2. 选择要部署的提交
3. 等待部署完成

## 💡 优化建议

### 7.1 性能优化
- 使用`simple_dashboard.py`减少依赖
- 优化数据处理逻辑
- 启用缓存机制

### 7.2 成本优化
- 使用免费版进行测试
- 合理设置自动休眠
- 监控资源使用情况

## 📝 注意事项

1. **数据持久化**：Railway的免费版不提供持久化存储
2. **API限制**：注意交易所API的调用频率限制
3. **安全性**：不要在代码中硬编码API密钥
4. **备份**：定期备份重要配置和数据

## 🆘 获取帮助

如果遇到问题，可以：
1. 查看Railway官方文档
2. 检查GitHub Issues
3. 联系技术支持

---

**部署完成后，你的加密货币交易监控面板就可以通过互联网访问了！** 🎉
