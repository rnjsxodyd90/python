"""Paths and constants for PyLearn."""

import os

# Root of the project (directory containing run.py)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Data directory for progress persistence
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
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
