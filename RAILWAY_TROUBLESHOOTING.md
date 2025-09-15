# Railway 部署故障排除指南

## 🚨 常见问题及解决方案

### 1. 依赖安装失败

#### 问题：`pandas_ta==0.3.14b0` 找不到
```
ERROR: Could not find a version that satisfies the requirement pandas_ta==0.3.14b0
```

**解决方案：**
- 使用 `Dockerfile.simple` 而不是 `Dockerfile`
- 该版本在PyPI上不可用，已移除该依赖
- 应用会自动检测并跳过不可用的依赖

#### 问题：Python版本不兼容
```
ERROR: Ignored the following versions that require a different python version
```

**解决方案：**
- 确保使用Python 3.11
- 检查依赖版本兼容性
- 使用范围版本而不是固定版本

### 2. 构建超时

#### 问题：构建过程超时
**解决方案：**
- 使用 `Dockerfile.simple` 减少构建时间
- 移除不必要的依赖
- 使用多阶段构建优化镜像大小

### 3. 应用启动失败

#### 问题：端口绑定失败
```
ERROR: Port already in use
```

**解决方案：**
- 确保使用 `PORT` 环境变量
- 检查 `railway_start.py` 中的端口配置
- 验证Railway的端口设置

#### 问题：依赖导入失败
```
ModuleNotFoundError: No module named 'xxx'
```

**解决方案：**
- 检查 `railway_start.py` 中的依赖检查逻辑
- 确保所有必需依赖都在 `requirements-simple.txt` 中
- 使用可选依赖检查机制

### 4. 网络连接问题

#### 问题：无法访问外部API
**解决方案：**
- 应用会自动切换到模拟数据模式
- 检查 `simple_dashboard.py` 是否可用
- 配置代理或使用VPN

## 🔧 调试步骤

### 1. 本地测试
```bash
# 构建镜像
docker build -f Dockerfile.simple -t crypto-dashboard .

# 运行容器
docker run -p 8501:8501 crypto-dashboard

# 查看日志
docker logs <container_id>
```

### 2. 检查依赖
```bash
# 进入容器
docker exec -it <container_id> /bin/bash

# 检查Python包
pip list

# 测试导入
python -c "import streamlit, pandas, numpy; print('核心依赖OK')"
python -c "import ccxt; print('CCXT可用')" || echo "CCXT不可用"
```

### 3. 查看Railway日志
1. 登录Railway控制台
2. 选择项目
3. 点击 "Deployments"
4. 查看构建和运行日志

## 📋 部署检查清单

### 部署前检查
- [ ] 代码已提交到GitHub
- [ ] 使用 `Dockerfile.simple`
- [ ] 使用 `requirements-simple.txt`
- [ ] `railway_start.py` 存在且可执行
- [ ] `.dockerignore` 配置正确

### 部署后检查
- [ ] 构建成功完成
- [ ] 应用正常启动
- [ ] 端口正确绑定
- [ ] 健康检查通过
- [ ] 可以访问应用URL

## 🆘 紧急修复

如果部署完全失败，可以尝试：

### 1. 使用最简配置
```dockerfile
FROM python:3.11-slim
WORKDIR /app
RUN pip install streamlit pandas numpy
COPY simple_dashboard.py .
EXPOSE 8501
CMD ["streamlit", "run", "simple_dashboard.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
```

### 2. 手动安装依赖
在Railway控制台中添加环境变量：
```
PIP_EXTRA_INDEX_URL=https://pypi.org/simple/
```

### 3. 使用Railway CLI
```bash
# 安装Railway CLI
npm install -g @railway/cli

# 登录
railway login

# 部署
railway up
```

## 📞 获取帮助

如果问题仍然存在：
1. 查看Railway官方文档
2. 检查GitHub Issues
3. 联系技术支持
4. 提供完整的错误日志

---

**记住：简化版应用使用模拟数据，即使某些依赖不可用也能正常运行！** 🎯
