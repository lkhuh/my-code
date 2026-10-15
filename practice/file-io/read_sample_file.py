"""Read a sample text file stored beside this script."""
from pathlib import Path

sample_path = Path(__file__).with_name("sample_text.txt")
text = sample_path.read_text(encoding="utf-8")
print(text)
