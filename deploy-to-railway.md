# 🚀 一键部署到Railway

## 快速部署步骤

### 1. 准备工作
```bash
# 确保代码已提交到GitHub
git add .
git commit -m "准备Railway部署"
git push origin main
```

### 2. 在Railway上部署
1. 访问 [railway.app](https://railway.app)
2. 点击 "New Project" → "Deploy from GitHub repo"
3. 选择你的仓库
4. 点击 "Deploy Now"

### 3. 配置环境变量（可选）
如果需要API访问：
```
EXCHANGE_API_KEY=your_api_key
EXCHANGE_SECRET=your_secret
```

### 4. 访问应用
部署完成后，Railway会提供一个HTTPS URL，直接访问即可。

## 📁 部署文件说明

- `Dockerfile` - 容器化配置
- `railway.json` - Railway部署配置
- `railway_start.py` - 智能启动脚本
- `requirements-railway.txt` - 部署专用依赖
- `.dockerignore` - 排除不需要的文件

## 🔧 本地测试

在部署前，可以在本地测试Docker构建：

```bash
# 构建镜像
docker build -t crypto-dashboard .

# 运行容器
docker run -p 8501:8501 crypto-dashboard
```

## ⚡ 特性

- ✅ 自动端口检测
- ✅ 智能应用选择（完整版/简化版）
- ✅ 健康检查
- ✅ 自动重启
- ✅ HTTPS支持
- ✅ 环境变量支持

## 🆘 故障排除

如果部署失败：
1. 检查构建日志
2. 确认所有文件都已提交
3. 验证Dockerfile语法
4. 检查依赖版本兼容性

---

**部署完成后，你的应用就可以通过互联网访问了！** 🎉
