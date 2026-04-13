#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF Watermark Remover - Remove watermarks/headers from PDF files
PDF 水印去除器 - 从 PDF 文件中去除水印/页眉

This tool removes watermarks, headers, or footers from PDF files by extracting
only the main content images. It works best for image-based PDFs (scanned documents).

这个工具通过提取主内容图像来去除 PDF 文件中的水印、页眉或页脚。
它最适合基于图像的 PDF（扫描文档）。
"""

import fitz
from PIL import Image
import io
import sys
import os
from pathlib import Path

# 设置控制台输出编码为 UTF-8
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')


def analyze_pdf(input_path: str) -> dict:
    """
    Analyze PDF structure and identify potential watermarks

    Args:
        input_path: Path to the input PDF file

    Returns:
        Dictionary with analysis results
    """
    doc = fitz.open(input_path)
    analysis = {
        'pages': len(doc),
        'images_per_page': [],
        'potential_watermarks': []
    }

    for page_num in range(len(doc)):
        page = doc[page_num]
        images = page.get_images()
        page_images = []

        for img_info in images:
            xref = img_info[0]
            width = img_info[2]
            height = img_info[3]
            page_images.append({
                'xref': xref,
                'width': width,
                'height': height,
                'is_watermark': height < 500  # Heuristic: small images are likely watermarks
            })

        analysis['images_per_page'].append(page_images)

        # Identify potential watermarks (small images at top/bottom)
        watermarks = [img for img in page_images if img['is_watermark']]
        if watermarks:
            analysis['potential_watermarks'].append({
                'page': page_num + 1,
                'count': len(watermarks),
                'sizes': [(img['width'], img['height']) for img in watermarks]
            })

    doc.close()
    return analysis


def remove_watermark(input_path: str, output_path: str, min_height: int = 500) -> bool:
    """
    Remove watermark/header/footer from PDF by extracting main content images

    Args:
        input_path: Path to the input PDF file
        output_path: Path to save the cleaned PDF
        min_height: Minimum image height to keep (pixels). Images smaller than this
                    are considered watermarks/headers/footers.

    Returns:
        True if successful, False otherwise
    """
    try:
        # Open input PDF
        doc = fitz.open(input_path)

        # Create new PDF document
        new_doc = fitz.open()

        processed_pages = 0
        skipped_images = 0
        kept_images = 0

        for page_num in range(len(doc)):
            page = doc[page_num]
            images = page.get_images()

            print(f"Processing page {page_num + 1}/{len(doc)}...")
            print(f"  Found {len(images)} images")

            # Extract main images (skip small ones that are likely watermarks)
            for img_info in images:
                xref = img_info[0]
                width = img_info[2]
                height = img_info[3]

                # Skip small images (watermarks/headers/footers)
                if height < min_height:
                    print(f"  Skipping small image (watermark): {width}x{height}")
                    skipped_images += 1
                    continue

                print(f"  Extracting main image: {width}x{height}")
                kept_images += 1

                try:
                    # Extract image
                    base_image = page.parent.extract_image(xref)
                    image_bytes = base_image["image"]

                    # Create new page based on image dimensions
                    new_page = new_doc.new_page(
                        width=width,
                        height=height
                    )

                    # Insert image
                    new_page.insert_image(
                        fitz.Rect(0, 0, width, height),
                        stream=image_bytes
                    )

                    processed_pages += 1

                except Exception as e:
                    print(f"  Error processing image: {e}")

        # Save new PDF
        new_doc.save(output_path)
        new_doc.close()
        doc.close()

        print(f"\nSummary:")
        print(f"  Processed pages: {processed_pages}")
        print(f"  Kept images: {kept_images}")
        print(f"  Skipped images (watermarks): {skipped_images}")
        print(f"  Output saved to: {output_path}")

        return True

    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description='PDF Watermark Remover / PDF 水印去除器',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples / 示例:
  # Analyze a PDF first
  python pdf_watermark_remover.py analyze document.pdf

  # Remove watermark with default settings
  python pdf_watermark_remover.py remove document.pdf output.pdf

  # Remove watermark with custom min_height
  python pdf_watermark_remover.py remove document.pdf output.pdf --min-height 300
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Analyze command
    analyze_parser = subparsers.add_parser('analyze', help='Analyze PDF structure')
    analyze_parser.add_argument('input', help='Input PDF file')

    # Remove command
    remove_parser = subparsers.add_parser('remove', help='Remove watermark from PDF')
    remove_parser.add_argument('input', help='Input PDF file')
    remove_parser.add_argument('output', help='Output PDF file')
    remove_parser.add_argument('--min-height', type=int, default=500,
                               help='Minimum image height to keep (default: 500)')

    args = parser.parse_args()

    if args.command == 'analyze':
        print(f"Analyzing: {args.input}")
        analysis = analyze_pdf(args.input)
        print(f"Pages: {analysis['pages']}")
        print(f"\nImages per page:")
        for i, images in enumerate(analysis['images_per_page']):
            print(f"  Page {i+1}: {len(images)} images")
            for img in images:
                status = "WATERMARK" if img['is_watermark'] else "MAIN"
                print(f"    - {img['width']}x{img['height']} [{status}]")

        if analysis['potential_watermarks']:
            print(f"\nPotential watermarks found:")
            for wm in analysis['potential_watermarks']:
                print(f"  Page {wm['page']}: {wm['count']} watermarks")
                print(f"    Sizes: {wm['sizes']}")

    elif args.command == 'remove':
        print(f"Removing watermark from: {args.input}")
        print(f"Output will be saved to: {args.output}")
        print(f"Minimum height threshold: {args.min_height}px")

        success = remove_watermark(args.input, args.output, args.min_height)

        if success:
            print("\nWatermark removal completed!")
            sys.exit(0)
        else:
            print("\nWatermark removal failed!")
            sys.exit(1)

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
