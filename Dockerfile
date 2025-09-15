# 完全干净的Dockerfile - 解决所有依赖问题
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 设置环境变量
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# 升级pip到最新版本
RUN python -m pip install --upgrade pip

# 验证pip版本
RUN pip --version

# 复制requirements文件
COPY requirements.txt .

# 升级构建工具
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# 安装所有依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY . .

# 创建非root用户
RUN useradd --create-home --shell /bin/bash app \
    && chown -R app:app /app
USER app

# 暴露端口
EXPOSE 8501

# 启动命令
CMD ["python", "railway_start.py"]