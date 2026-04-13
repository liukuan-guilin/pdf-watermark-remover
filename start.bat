@echo off
chcp 65001 >nul 2>&1
setlocal enabledelayedexpansion

:: ============================================
:: PDF Watermark Remover - 交互式启动脚本
:: PDF 水印去除器 - 交互式启动
:: ============================================

title PDF Watermark Remover - PDF 水印去除器

:menu
cls
echo ============================================
echo   PDF Watermark Remover | PDF 水印去除器
echo ============================================
echo.
echo 请选择操作 | Select operation:
echo.
echo   [1] 分析 PDF 结构 (Analyze PDF)
echo   [2] 去除水印 (Remove watermark)
echo   [3] 快速去水印 (Quick remove - 默认设置)
echo   [4] 查看帮助 (Show help)
echo   [5] 退出 (Exit)
echo.
echo ============================================
set /p choice="请输入选项 | Enter choice (1-5): "

if "%choice%"=="1" goto analyze
if "%choice%"=="2" goto remove
if "%choice%"=="3" goto quick
if "%choice%"=="4" goto help
if "%choice%"=="5" goto end
goto menu

:analyze
cls
echo.
echo ============================================
echo   分析 PDF | Analyze PDF
echo ============================================
echo.
set /p filepath="请输入 PDF 文件路径 | Enter PDF file path: "
if not exist "%filepath%" (
    echo.
    echo [错误] 文件不存在！| [Error] File not found!
    echo.
    pause
    goto menu
)
echo.
echo 正在分析 | Analyzing...
echo.
python pdf_watermark_remover.py analyze "%filepath%"
echo.
pause
goto menu

:remove
cls
echo.
echo ============================================
echo   去除水印 | Remove Watermark
echo ============================================
echo.
set /p inputfile="请输入输入 PDF 路径 | Enter input PDF path: "
if not exist "%inputfile%" (
    echo.
    echo [错误] 文件不存在！| [Error] File not found!
    echo.
    pause
    goto menu
)

set /p outputfile="请输入输出 PDF 路径 | Enter output PDF path: "

echo.
set /p threshold="请输入最小高度阈值 (默认 500) | Enter min height (default 500): "
if "%threshold%"=="" set threshold=500

echo.
echo 正在处理 | Processing...
echo.
python pdf_watermark_remover.py remove "%inputfile%" "%outputfile%" --min-height %threshold%

if %errorlevel% equ 0 (
    echo.
    echo [✓] 处理完成！| Processing complete!
    echo 输出文件 | Output: %outputfile%
) else (
    echo.
    echo [错误] 处理失败！| Processing failed!
)
echo.
pause
goto menu

:quick
cls
echo.
echo ============================================
echo   快速去水印 | Quick Remove
echo ============================================
echo.
echo 将 PDF 文件拖放到此窗口，然后按回车...
echo Drag and drop PDF file here, then press Enter...
echo.
set /p inputfile=
set "inputfile=%inputfile:"=%"
if not exist "%inputfile%" (
    echo.
    echo [错误] 文件不存在！| [Error] File not found!
    echo.
    pause
    goto menu
)

:: 生成输出文件名
for %%I in ("%inputfile%") do set "outputfile=%%~dpI%%~nI_no_watermark.pdf"

echo.
echo 正在处理 | Processing...
echo 输出文件 | Output: %outputfile%
echo.
python pdf_watermark_remover.py remove "%inputfile%" "%outputfile%" --min-height 500

if %errorlevel% equ 0 (
    echo.
    echo [✓] 处理完成！| Processing complete!
    echo 正在打开输出目录...
    explorer /select,"%outputfile%"
) else (
    echo.
    echo [错误] 处理失败！| Processing failed!
)
echo.
pause
goto menu

:help
cls
echo.
echo ============================================
echo   帮助 | Help
echo ============================================
echo.
python pdf_watermark_remover.py --help
echo.
pause
goto menu

:end
cls
echo.
echo ============================================
echo   感谢使用 | Thank you for using!
echo   PDF Watermark Remover
echo ============================================
echo.
exit /b 0
