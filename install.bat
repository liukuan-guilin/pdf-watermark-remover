@echo off
chcp 65001 >nul 2>&1
setlocal enabledelayedexpansion

:: ============================================
:: PDF Watermark Remover - 一键安装脚本
:: PDF 水印去除器 - 一键安装
:: ============================================

echo ============================================
echo   PDF Watermark Remover 安装程序
echo   PDF 水印去除器 - 一键安装
echo ============================================
echo.

:: 检查 Python 是否已安装
echo [Step 1/3] 检查 Python 环境...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [错误] 未检测到 Python 环境！
    echo [Error] Python is not installed!
    echo.
    echo 请先安装 Python 3.8+: https://www.python.org/downloads/
    echo Please install Python 3.8+ first
    echo.
    pause
    exit /b 1
)

python --version
echo [✓] Python 已安装

:: 检查 pip
echo.
echo [Step 2/3] 检查 pip...
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] pip 未安装
    pause
    exit /b 1
)
echo [✓] pip 已安装

:: 安装依赖
echo.
echo [Step 3/3] 安装依赖...
echo Installing dependencies...

pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo.
    echo [错误] 依赖安装失败！
    echo [Error] Failed to install dependencies!
    echo.
    pause
    exit /b 1
)

echo.
echo ============================================
echo   安装完成！Installation Complete!
echo ============================================
echo.
echo 使用方法 Usage:
echo   1. 分析 PDF: python pdf_watermark_remover.py analyze your_file.pdf
echo   2. 去除水印：python pdf_watermark_remover.py remove input.pdf output.pdf
echo.
echo 或者直接运行：start.bat 进行交互式操作
echo.
pause
