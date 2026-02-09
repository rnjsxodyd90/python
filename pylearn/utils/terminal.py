"""Terminal utilities: clear screen, ANSI colors, terminal size."""

import os
import sys


# --- ANSI Color Codes ---

class Color:
    """ANSI color codes for terminal output."""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"

    # Foreground
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    GRAY = "\033[90m"

    # Bright foreground
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"

    # Background
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"


def _supports_color():
    """Check if the terminal supports ANSI colors."""
    if os.environ.get("NO_COLOR"):
        return False
    if os.environ.get("FORCE_COLOR"):
        return True
    if sys.platform == "win32":
        # Windows Terminal and modern cmd support ANSI
        return os.environ.get("WT_SESSION") or os.environ.get("TERM_PROGRAM") or True
    return hasattr(sys.stdout, "isatty") and sys.stdout.isatty()


_color_enabled = _supports_color()

# Enable ANSI escape sequences on Windows
if sys.platform == "win32":
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except Exception:
        pass


def colorize(text, *codes):
    """Wrap text in ANSI color codes."""
    if not _color_enabled:
        return text
    prefix = "".join(codes)
    return f"{prefix}{text}{Color.RESET}"


def bold(text):
    return colorize(text, Color.BOLD)


def dim(text):
    return colorize(text, Color.DIM)


def success(text):
    return colorize(text, Color.BRIGHT_GREEN)


def error(text):
    return colorize(text, Color.BRIGHT_RED)


def warning(text):
    return colorize(text, Color.BRIGHT_YELLOW)


def info(text):
    return colorize(text, Color.BRIGHT_CYAN)


def highlight(text):
    return colorize(text, Color.BRIGHT_MAGENTA)


def code_style(text):
    return colorize(text, Color.YELLOW)


def header_style(text):
    return colorize(text, Color.BOLD, Color.BRIGHT_BLUE)


def clear_screen():
    """Clear the terminal screen."""
    os.system("cls" if sys.platform == "win32" else "clear")


def get_terminal_size():
    """Get terminal width and height."""
    try:
        columns, lines = os.get_terminal_size()
        return columns, lines
    except (ValueError, OSError):
        return 80, 24


def print_separator(char="─", width=None):
    """Print a horizontal separator line."""
    if width is None:
        width = min(get_terminal_size()[0], 80)
    print(dim(char * width))


def print_header(title, subtitle=None):
    """Print a styled header."""
    width = min(get_terminal_size()[0], 80)
    print()
    print_separator("═", width)
    print(header_style(f"  {title}"))
    if subtitle:
        print(dim(f"  {subtitle}"))
    print_separator("═", width)
    print()


def print_box(text, style="info"):
    """Print text in a simple box."""
    width = min(get_terminal_size()[0], 76)
    color_fn = {"info": info, "success": success, "error": error, "warning": warning}.get(style, info)
    print(f"  {color_fn('┌' + '─' * (width - 4) + '┐')}")
    for line in text.split("\n"):
        padding = width - 6 - len(line)
        if padding < 0:
            line = line[:width - 9] + "..."
            padding = 0
        print(f"  {color_fn('│')} {line}{' ' * padding} {color_fn('│')}")
    print(f"  {color_fn('└' + '─' * (width - 4) + '┘')}")
