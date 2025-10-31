"""
py-trex.py
A module to build a compact regular expression from a list of strings using a Trie.
"""

import re

class TrieNode:
    """Represents a single node in the Trie."""
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    """Trie data structure for building regex from strings."""
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        """
        Inserts a word into the Trie.

        Args:
            word (str): The string to insert.
        """
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end = True

    def _build_regex(self, node: TrieNode) -> str:
        """
        Recursively builds the regex from the Trie.

        Args:
            node (TrieNode): The current node in the Trie.

        Returns:
            str: A regex fragment representing the subtree.
        """
        if not node.children:
            return ''
        parts = []
        for char, child in node.children.items():
            escaped_char = re.escape(char)
            suffix = self._build_regex(child)
            if child.is_end and suffix:
                parts.append(f"{escaped_char}(?:{suffix})?")
            elif child.is_end:
                parts.append(f"{escaped_char}")
            else:
                parts.append(f"{escaped_char}{suffix}")
        return parts[0] if len(parts) == 1 else f"(?:{'|'.join(parts)})"

    def to_regex(self) -> str:
        """
        Builds the full regex pattern from the Trie.

        Returns:
            str: The complete regex pattern.
        """
        return f"^{self._build_regex(self.root)}$"


def build_regex_from_list(strings: list[str]) -> str:
    """
    Builds a regex from a list of strings.

    Args:
        strings (list[str]): List of strings to include in the regex.

    Returns:
        str: A regex pattern that matches any of the input strings.
    """
    trie = Trie()
    for s in strings:
        trie.insert(s)
    return trie.to_regex()