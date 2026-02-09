"""Paths and constants for PyLearn."""

import os

# Data directory for progress persistence (stored in user's home directory)
DATA_DIR = os.path.join(os.path.expanduser("~"), ".pylearn")
PROGRESS_FILE = os.path.join(DATA_DIR, "progress.json")

# App metadata
APP_NAME = "PyLearn"
APP_VERSION = "1.0.0"
APP_TAGLINE = "Interactive Python Learning CLI"

# Display
MAX_WIDTH = 80
MENU_INDENT = "  "

# Quiz passing score (percentage)
QUIZ_PASS_THRESHOLD = 70
