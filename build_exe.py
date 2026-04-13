#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build executable for PDF Watermark Remover
为 PDF 水印去除器生成可执行文件
"""

import subprocess
import sys
import os
import platform
import shutil

def check_requirements():
    """检查是否安装了 PyInstaller"""
    print("[1/4] 检查 PyInstaller | Checking PyInstaller...")
    try:
        import PyInstaller
        print(f"     PyInstaller version: {PyInstaller.__version__}")
    except ImportError:
        print("     正在安装 PyInstaller... | Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("     ✓ PyInstaller 已安装")

def check_dependencies():
    """检查是否安装了所有依赖"""
    print("[2/4] 检查依赖 | Checking dependencies...")
    required = ["fitz", "PIL"]
    for dep in required:
        try:
            __import__(dep)
            print(f"     ✓ {dep}")
        except ImportError:
            print(f"     正在安装 {dep}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            break

def build_executable():
    """构建可执行文件"""
    print("[3/4] 构建可执行文件 | Building executable...")

    system = platform.system()
    if system == "Windows":
        ext = ".exe"
    else:
        ext = ""

    # PyInstaller 命令
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--name", "pdf-watermark-remover",
        "--add-data", "requirements.txt;.",
        "--hidden-import", "fitz",
        "--hidden-import", "PIL",
        "--console",
        "--clean",
        "pdf_watermark_remover.py"
    ]

    print(f"     运行命令 | Running: {' '.join(cmd)}")
    subprocess.check_call(cmd)

    # 移动生成的文件
    dist_dir = "dist"
    if os.path.exists(dist_dir):
        exe_path = os.path.join(dist_dir, f"pdf-watermark-remover{ext}")
        if os.path.exists(exe_path):
            print(f"     ✓ 可执行文件已生成 | Executable created: {exe_path}")
            return True

    return False

def copy_additional_files():
    """复制额外文件到 dist 目录"""
    print("[4/4] 复制额外文件 | Copying additional files...")

    dist_dir = "dist"
    files_to_copy = ["README.md", "requirements.txt"]

    for filename in files_to_copy:
        src = filename
        dst = os.path.join(dist_dir, filename)
        if os.path.exists(src):
            shutil.copy(src, dst)
            print(f"     ✓ 已复制 | Copied: {filename}")

def main():
    """主函数"""
    print("=" * 50)
    print("  PDF Watermark Remover - Build Executable")
    print("  PDF 水印去除器 - 生成可执行文件")
    print("=" * 50)
    print()

    try:
        check_requirements()
        check_dependencies()
        build_success = build_executable()
        if build_success:
            copy_additional_files()

        print()
        print("=" * 50)
        print("  构建完成！Build Complete!")
        print("=" * 50)
        print()
        print("  可执行文件位置 | Executable location:")
        print("  dist/pdf-watermark-remover.exe (Windows)")
        print("  dist/pdf-watermark-remover (Linux/Mac)")
        print()
        print("  使用说明 | Usage:")
        print("  pdf-watermark-remover.exe analyze your.pdf")
        print("  pdf-watermark-remover.exe remove input.pdf output.pdf")
        print()

    except subprocess.CalledProcessError as e:
        print(f"\n[错误] 构建失败：{e}\n")
        sys.exit(1)
    except Exception as e:
        print(f"\n[错误] 发生错误：{e}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
