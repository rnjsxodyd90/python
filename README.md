# PyLearn - Interactive Python Learning CLI

An interactive, terminal-based Python learning tool covering beginner-to-advanced topics plus interview prep. Navigate lessons, run exercises, take quizzes, and track progress -- all from the command line.

**Zero external dependencies** -- pure Python stdlib.

## Installation

```bash
pip install .          # install from source
pip install -e .       # editable/dev install
```

## Quick Start

```bash
pylearn                # run via installed command
python -m pylearn      # alternative
python run.py          # run without installing
```

## What's Included

| Module | Lessons | Exercises | Quiz |
|--------|---------|-----------|------|
| 01 - Python Basics | 4 | 4 | 5 |
| 02 - Data Types | 7 | 7 | 7 |
| 03 - Control Flow | 5 | 5 | 5 |
| 04 - Functions | 6 | 6 | 6 |
| 05 - OOP (Expanded) | 12 | 8 | 8 |
| 10 - Interview Prep | 3 | 10 | 5 |
| **Total** | **37** | **40** | **36** |

## Features

- **Lessons** with explanations, code examples, and key points
- **Exercises** with validation, hints, and solutions
- **Quizzes** with scoring and explanations
- **Progress tracking** with streaks and per-module stats
- **Interview prep** with classic coding problems (Two Sum, FizzBuzz, Binary Search, etc.)
- **ANSI colors** for a clean terminal UI
- Works on Windows, macOS, and Linux

## Project Structure

```
python/
├── run.py                    # Entry point (dev)
├── pyproject.toml            # Package metadata
├── pylearn/
│   ├── app.py                # Main app loop & routing
│   ├── cli.py                # Menus, prompts, display
│   ├── config.py             # Paths & constants
│   ├── utils/                # Terminal colors, formatting
│   ├── engine/               # Code runner & validator
│   ├── progress/             # JSON-based progress tracking
│   └── curriculum/           # Auto-discovered lesson modules
│       ├── 01_basics/
│       ├── 02_data_types/
│       ├── 03_control_flow/
│       ├── 04_functions/
│       ├── 05_oop/
│       └── 10_interview_prep/
~/.pylearn/
└── progress.json             # Auto-created on first run
```
