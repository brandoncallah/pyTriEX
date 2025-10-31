# TrieFastRegex

A Python library for building compact regular expressions from lists of strings using Trie data structure.

## Installation

```bash
pip install TrieFastRegex
```

## Usage

```python
from pyTriEX import build_regex_from_list

# Build regex from a list of strings
strings = ["cat", "car", "card", "care", "careful"]
regex = build_regex_from_list(strings)
print(regex)  # ^ca(?:t|r(?:(?:d|e(?:ful)?))?)$

# Use the regex
import re
pattern = re.compile(regex)
print(pattern.match("car"))  # Match object
print(pattern.match("dog"))  # None
```

## Features

- Efficient Trie-based regex construction
- Compact output patterns
- Easy to use

## License

MIT License