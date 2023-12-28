import re
text = "The quick b   n brown fox jumps over the lazy dog."
pattern = r"b...n"
pattern = r"^The"

result = re.search(pattern, text)
if result:    print("Pattern found:", result.group())
