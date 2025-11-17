#!/usr/bin/env python3
"""
Update source_url in front matter of all Markdown files.
Replaces https://developers.sber.ru/docs/ru/salutebot/ with https://github.com/baslie/salutebot-docs/
"""

import re
from pathlib import Path

def update_source_url(file_path: Path) -> bool:
    """Update source_url in a single Markdown file."""
    try:
        content = file_path.read_text(encoding='utf-8')

        # Pattern to match source_url in front matter
        pattern = r'(source_url:\s*")https://developers\.sber\.ru/docs/ru/salutebot/(.*?)(")'

        # Replace with new GitHub URL
        new_content = re.sub(
            pattern,
            r'\1https://github.com/baslie/salutebot-docs/blob/main/data/docs_md/salutebot/\2.md\3',
            content
        )

        # Check if any changes were made
        if new_content != content:
            file_path.write_text(new_content, encoding='utf-8')
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Process all Markdown files in the documentation directory."""
    docs_dir = Path(__file__).parent / "data" / "docs_md" / "salutebot"

    if not docs_dir.exists():
        print(f"Error: Directory not found: {docs_dir}")
        return

    # Find all .md files recursively
    md_files = list(docs_dir.rglob("*.md"))
    print(f"Found {len(md_files)} Markdown files")

    updated_count = 0
    for md_file in md_files:
        if update_source_url(md_file):
            updated_count += 1
            print(f"[+] Updated: {md_file.relative_to(docs_dir)}")

    print(f"\nTotal files updated: {updated_count}/{len(md_files)}")

if __name__ == "__main__":
    main()
