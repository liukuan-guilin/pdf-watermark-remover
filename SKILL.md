---
name: pdf-watermark-remover
description: Remove watermarks, headers, and footers from PDF files by extracting main content images
type: skill
---

# PDF Watermark Remover | PDF 水印去除器

[English](#english) | [简体中文](#中文)

---

## English

### Overview

**PDF Watermark Remover** is a powerful tool that removes watermarks, headers, and footers from PDF files by extracting only the main content images. It works best for image-based PDFs such as scanned documents.

### Features

- ✅ Remove headers and footers automatically
- ✅ Remove page numbers and watermarks
- ✅ Preserve main document content
- ✅ Support multi-page PDFs
- ✅ Configurable height threshold
- ✅ Bilingual support (English/Chinese)

### Requirements

- Python 3.8+
- `PyMuPDF` (fitz)
- `Pillow`

### Installation

```bash
# Install dependencies
pip install PyMuPDF Pillow

# Or install from this skill directory
cd skills/pdf-watermark-remover
pip install -r requirements.txt
```

### Usage

#### Step 1: Analyze PDF Structure

Before removing watermarks, analyze the PDF to identify potential watermarks:

```bash
python pdf_watermark_remover.py analyze your_document.pdf
```

This will show you:
- Number of pages
- Images on each page
- Which images are likely watermarks (small images)

#### Step 2: Remove Watermark

```bash
# Basic usage
python pdf_watermark_remover.py remove input.pdf output.pdf

# With custom height threshold (default: 500px)
python pdf_watermark_remover.py remove input.pdf output.pdf --min-height 300
```

### How It Works

1. **Analyzes** the PDF and extracts all images from each page
2. **Identifies** potential watermarks based on image size (small images at top/bottom)
3. **Skips** images smaller than the threshold (watermarks/headers/footers)
4. **Extracts** and **preserves** only the main content images
5. **Creates** a new clean PDF with the extracted images

### Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--min-height` | 500 | Minimum image height in pixels. Images smaller than this are considered watermarks. |

### Tips

- **For documents with small headers**: Use `--min-height 200` or lower
- **For documents with large watermarks**: Use `--min-height 800` or higher
- **Always analyze first**: Run `analyze` command to understand the PDF structure

### Example Output

```
Processing page 1/2...
  Found 2 images
  Skipping small image (watermark): 957x168
  Extracting main image: 1579x2203

Processing page 2/2...
  Found 2 images
  Skipping small image (watermark): 957x168
  Extracting main image: 1535x2157

Summary:
  Processed pages: 2
  Kept images: 2
  Skipped images (watermarks): 2
  Output saved to: output.pdf
```

---

## 中文

### 概述

**PDF 水印去除器**是一个强大的工具，通过提取主内容图像来去除 PDF 文件中的水印、页眉和页脚。它最适合基于图像的 PDF（如扫描文档）。

### 功能特点

- ✅ 自动去除页眉和页脚
- ✅ 去除页码和水印
- ✅ 保留文档主要内容
- ✅ 支持多页 PDF
- ✅ 可配置的高度阈值
- ✅ 双语支持（英文/中文）

### 环境要求

- Python 3.8+
- `PyMuPDF` (fitz)
- `Pillow`

### 安装方法

```bash
# 安装依赖
pip install PyMuPDF Pillow

# 或从此技能目录安装
cd skills/pdf-watermark-remover
pip install -r requirements.txt
```

### 使用方法

#### 第一步：分析 PDF 结构

在去除水印之前，先分析 PDF 以识别潜在的水印：

```bash
python pdf_watermark_remover.py analyze your_document.pdf
```

这将显示：
- 页数
- 每页的图像数量
- 哪些图像可能是水印（小图像）

#### 第二步：去除水印

```bash
# 基本用法
python pdf_watermark_remover.py remove input.pdf output.pdf

# 自定义高度阈值（默认：500px）
python pdf_watermark_remover.py remove input.pdf output.pdf --min-height 300
```

### 工作原理

1. **分析** PDF 并从每页提取所有图像
2. **识别** 基于图像尺寸的潜在水印（顶部/底部的小图像）
3. **跳过** 小于阈值的图像（水印/页眉/页脚）
4. **提取** 并**保留** 仅主内容图像
5. **创建** 包含提取图像的新干净 PDF

### 参数说明

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `--min-height` | 500 | 最小图像高度（像素）。小于此值的图像被视为水印。 |

### 使用技巧

- **对于有小页眉的文档**：使用 `--min-height 200` 或更低
- **对于有大水印的文档**：使用 `--min-height 800` 或更高
- **先分析再处理**：运行 `analyze` 命令了解 PDF 结构

### 示例输出

```
处理第 1/2 页...
  找到 2 个图像
  跳过小图像 (水印): 957x168
  提取主图像：1579x2203

处理第 2/2 页...
  找到 2 个图像
  跳过小图像 (水印): 957x168
  提取主图像：1535x2157

总结:
  已处理页数：2
  保留图像：2
  跳过图像 (水印): 2
  输出已保存到：output.pdf
```

---

## Files | 文件结构

```
skills/pdf-watermark-remover/
├── SKILL.md                 # This file / 本文件
├── pdf_watermark_remover.py # Main script / 主脚本
├── requirements.txt         # Python dependencies / Python 依赖
└── examples/                # Example files (optional) / 示例文件（可选）
```

---

## License | 许可证

MIT License

---

## Author | 作者

Created by liukuan-guilin

GitHub: https://github.com/liukuan-guilin
