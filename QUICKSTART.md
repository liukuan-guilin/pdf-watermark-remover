# 快速开始 | Quick Start

## 🚀 三种使用方式

### 方式一：双击运行 start.bat（最简单）

1. 先运行 `install.bat` 安装依赖
2. 双击 `start.bat` 打开交互式菜单
3. 按照提示选择操作

```
┌────────────────────────────────────────┐
│   PDF Watermark Remover 菜单            │
├────────────────────────────────────────┤
│  [1] 分析 PDF 结构                        │
│  [2] 去除水印                            │
│  [3] 快速去水印（拖放文件）               │
│  [4] 查看帮助                            │
│  [5] 退出                                │
└────────────────────────────────────────┘
```

### 方式二：生成独立 .exe 文件

```bash
# 安装 PyInstaller
pip install pyinstaller

# 运行构建脚本
python build_exe.py

# 生成的文件在 dist/ 目录
dist/pdf-watermark-remover.exe
```

### 方式三：命令行直接使用

```bash
# 安装依赖
pip install -r requirements.txt

# 分析 PDF
python pdf_watermark_remover.py analyze your.pdf

# 去除水印
python pdf_watermark_remover.py remove input.pdf output.pdf

# 自定义阈值
python pdf_watermark_remover.py remove input.pdf output.pdf --min-height 300
```

---

## 📁 文件说明

| 文件 | 说明 |
|------|------|
| `install.bat` | 一键安装脚本（Windows） |
| `start.bat` | 交互式启动菜单（Windows） |
| `build_exe.py` | 生成独立 .exe 的脚本 |
| `pdf_watermark_remover.py` | 主程序 |
| `requirements.txt` | Python 依赖 |
| `README.md` | 详细文档 |
| `SKILL.md` | 技能说明（双语） |

---

## 💡 快速去水印（推荐）

运行 `start.bat` 后选择 `[3] 快速去水印`：

1. 将 PDF 文件拖放到命令行窗口
2. 按回车键
3. 自动生成 `xxx_no_watermark.pdf`
4. 自动打开输出目录

---

## 🔧 常见问题

### Q: 提示 "未检测到 Python 环境"
A: 请先安装 Python 3.8+：https://www.python.org/downloads/

### Q: 去除水印后效果不好
A: 调整 `--min-height` 参数：
- 水印较小：降低阈值（如 200）
- 水印较大：提高阈值（如 800）

### Q: 如何批量处理多个 PDF？
A: 创建一个批处理脚本：

```batch
@echo off
for %%f in (*.pdf) do (
    python pdf_watermark_remover.py remove "%%f" "%%~nf_clean.pdf"
)
echo 批量处理完成!
pause
```

---

## 📞 项目链接

- **GitHub**: https://github.com/liukuan-guilin/pdf-watermark-remover
- **PyPI**: （待发布）
