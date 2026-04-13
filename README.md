# PDF Watermark Remover | PDF 水印去除器

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyPI - PyMuPDF](https://img.shields.io/badge/PyMuPDF->=1.23.0-green.svg)](https://pypi.org/project/PyMuPDF/)

**English** | [简体中文](#中文)

---

## English

### 🚀 Quick Start

#### Option 1: One-Click Interactive Mode (Recommended)

```batch
# Windows - Double click to run
install.bat      # Install dependencies
start.bat        # Open interactive menu
```

#### Option 2: Generate Standalone .exe

```bash
python build_exe.py    # Generate .exe file
dist/pdf-watermark-remover.exe   # Use standalone executable
```

#### Option 3: Command Line

```bash
pip install PyMuPDF Pillow
python pdf_watermark_remover.py remove input.pdf output.pdf
```

### ✨ Features

- **Automatic Detection** - Identifies watermarks based on image size
- **Smart Extraction** - Preserves main content, removes headers/footers
- **Configurable** - Adjust threshold for different document types
- **Bilingual** - Full English and Chinese support

### 📖 Documentation

See [SKILL.md](skills/pdf-watermark-remover/SKILL.md) for detailed usage instructions.

### 🔧 Usage Examples

```bash
# Analyze PDF structure first
python pdf_watermark_remover.py analyze document.pdf

# Remove watermark with default settings
python pdf_watermark_remover.py remove input.pdf output.pdf

# Custom height threshold (300px)
python pdf_watermark_remover.py remove input.pdf output.pdf --min-height 300
```

### 📦 Installation

```bash
# Clone or download this skill
cd skills/pdf-watermark-remover

# Install dependencies
pip install -r requirements.txt
```

---

## 中文

### 🚀 快速开始

#### 方式一：一键交互模式（推荐）

```batch
# Windows - 双击运行
install.bat      # 安装依赖
start.bat        # 打开交互式菜单
```

#### 方式二：生成独立 .exe 文件

```bash
python build_exe.py    # 生成 .exe 文件
dist/pdf-watermark-remover.exe   # 使用独立可执行文件
```

#### 方式三：命令行

```bash
pip install PyMuPDF Pillow
python pdf_watermark_remover.py remove input.pdf output.pdf
```

### ✨ 功能特点

- **自动检测** - 基于图像尺寸识别水印
- **智能提取** - 保留主要内容，移除页眉/页脚
- **可配置** - 针对不同文档类型调整阈值
- **双语支持** - 完整的英文和中文支持

### 📖 文档说明

详细使用说明请参阅 [SKILL.md](skills/pdf-watermark-remover/SKILL.md)。

### 🔧 使用示例

```bash
# 先分析 PDF 结构
python pdf_watermark_remover.py analyze document.pdf

# 使用默认设置去除水印
python pdf_watermark_remover.py remove input.pdf output.pdf

# 自定义高度阈值（300px）
python pdf_watermark_remover.py remove input.pdf output.pdf --min-height 300
```

### 📦 安装方法

```bash
# 克隆或下载此技能
cd skills/pdf-watermark-remover

# 安装依赖
pip install -r requirements.txt
```

---

## 📊 Before & After | 处理前后

| Before | After |
|--------|-------|
| PDF with header/watermark | Clean PDF without watermark |
| 带页眉/水印的 PDF | 无水印的干净 PDF |

---

## 🛠️ How It Works | 工作原理

```
┌─────────────────────────────────────────────────────────┐
│                    Input PDF                            │
│  ┌─────────────────────────────────────────────────┐    │
│  │  [HEADER/WATERMARK - 957x168] ← Skipped         │    │
│  │                                                 │    │
│  │  ┌───────────────────────────────────────────┐  │    │
│  │  │                                           │  │    │
│  │  │     MAIN CONTENT IMAGE                    │  │    │
│  │  │     1579x2203 ← Extracted & Preserved     │  │    │
│  │  │                                           │  │    │
│  │  └───────────────────────────────────────────┘  │    │
│  └─────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────┐
│                   Output PDF                            │
│  ┌─────────────────────────────────────────────────┐    │
│  │                                                 │    │
│  │  ┌───────────────────────────────────────────┐  │    │
│  │  │                                           │  │    │
│  │  │     MAIN CONTENT IMAGE                    │  │    │
│  │  │     1579x2203 (Clean, No Watermark)       │  │    │
│  │  │                                           │  │    │
│  │  └───────────────────────────────────────────┘  │    │
│  └─────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

---

## 📝 License | 许可证

MIT License - See [LICENSE](LICENSE) file for details.

---

## 👤 Author | 作者

**liukuan-guilin**

- GitHub: [@liukuan-guilin](https://github.com/liukuan-guilin)
- PyPI: [ankicli-tool](https://pypi.org/project/ankicli-tool/)

---

## 🔗 Related Projects | 相关项目

- [Anki CLI](https://github.com/liukuan-guilin/anki-cli) - Command-line interface for Anki
- [MinerU](https://github.com/opendatalab/MinerU) - PDF parsing tool by OpenDataLab
