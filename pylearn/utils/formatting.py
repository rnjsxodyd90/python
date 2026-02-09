"""Text wrapping and formatting helpers."""

import textwrap
from pylearn.config import MAX_WIDTH


def wrap_text(text, width=None, indent=""):
    """Wrap text to terminal width with optional indent."""
    if width is None:
        width = MAX_WIDTH
    return textwrap.fill(text, width=width, initial_indent=indent,
                         subsequent_indent=indent)


def indent_code(code, spaces=4):
    """Indent a code block."""
    prefix = " " * spaces
    return "\n".join(prefix + line for line in code.split("\n"))


def format_code_block(code, language="python"):
    """Format a code block for display."""
    from pylearn.utils.terminal import BOX_V
    lines = code.strip().split("\n")
    result = []
    for i, line in enumerate(lines, 1):
        result.append(f"  {i:3d} {BOX_V} {line}")
    return "\n".join(result)


def truncate(text, max_len=60):
    """Truncate text with ellipsis."""
    if len(text) <= max_len:
        return text
    return text[:max_len - 3] + "..."
