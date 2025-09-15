#!/usr/bin/env python3
"""
Railway部署启动脚本
自动检测环境并启动合适的应用版本
"""

import os
import sys
import subprocess
from pathlib import Path

def get_port():
    """获取端口号，优先使用Railway的PORT环境变量"""
    return int(os.environ.get("PORT", 8501))

def check_dependencies():
    """检查关键依赖是否可用"""
    try:
        import streamlit
        import pandas
        import numpy
        import pandas_ta
        print("✅ 核心依赖检查通过")
        return True
    except ImportError as e:
        print(f"❌ 依赖检查失败: {e}")
        return False

def check_optional_dependencies():
    """检查可选依赖"""
    optional_deps = {}
    try:
        import ccxt
        optional_deps['ccxt'] = True
        print("✅ CCXT可用 - 支持实时数据")
    except ImportError:
        optional_deps['ccxt'] = False
        print("⚠️  CCXT不可用 - 将使用模拟数据")
    
    try:
        import pandas_ta
        optional_deps['pandas_ta'] = True
        print("✅ Pandas-TA可用 - 支持技术指标")
    except ImportError:
        optional_deps['pandas_ta'] = False
        print("⚠️  Pandas-TA不可用 - 部分功能受限")
    
    return optional_deps

def choose_app_version(optional_deps):
    """根据环境选择应用版本"""
    # 检查是否有网络连接（通过尝试导入ccxt）
    if optional_deps.get('ccxt', False):
        print("🌐 网络连接正常，使用完整版dashboard")
        return "dashboard.py"
    else:
        print("⚠️  ccxt不可用，使用简化版dashboard")
        return "simple_dashboard.py"

def start_streamlit(app_file, port):
    """启动Streamlit应用"""
    cmd = [
        sys.executable, "-m", "streamlit", "run", app_file,
        "--server.port", str(port),
        "--server.address", "0.0.0.0",
        "--server.headless", "true",
        "--server.enableCORS", "false",
        "--server.enableXsrfProtection", "false"
    ]
    
    print(f"🚀 启动命令: {' '.join(cmd)}")
    print(f"📱 应用将在端口 {port} 上运行")
    print(f"🌍 访问地址: http://0.0.0.0:{port}")
    
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ 启动失败: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n👋 应用已停止")

def main():
    """主函数"""
    print("=" * 50)
    print("🚀 Railway 加密货币交易监控面板")
    print("=" * 50)
    
    # 检查依赖
    if not check_dependencies():
        print("请安装必要的依赖: pip install -r requirements.txt")
        sys.exit(1)
    
    # 检查可选依赖
    optional_deps = check_optional_dependencies()
    
    # 获取端口
    port = get_port()
    print(f"🔌 使用端口: {port}")
    
    # 选择应用版本
    app_file = choose_app_version(optional_deps)
    print(f"📄 使用应用文件: {app_file}")
    
    # 检查文件是否存在
    if not Path(app_file).exists():
        print(f"❌ 应用文件不存在: {app_file}")
        sys.exit(1)
    
    # 启动应用
    start_streamlit(app_file, port)

if __name__ == "__main__":
    main()
