"""Base dataclasses for curriculum content."""

from dataclasses import dataclass, field
from typing import List, Optional, Callable, Any


@dataclass
class Lesson:
    """A single lesson with content and optional code examples."""
    id: str
    title: str
    content: str                      # Multi-line lesson text
    code_example: str = ""            # Demonstrative code
    key_points: List[str] = field(default_factory=list)


@dataclass
class Exercise:
    """A coding exercise the user solves."""
    id: str
    title: str
    description: str                  # What to do
    starter_code: str = ""            # Boilerplate to start with
    expected_output: str = ""         # Simple output matching
    test_cases: List[dict] = field(default_factory=list)  # Advanced validation
    validator: Optional[Callable] = None  # Custom validator function
    hints: List[str] = field(default_factory=list)
    solution: str = ""                # Revealed on request
    difficulty: str = "easy"          # easy, medium, hard


@dataclass
class QuizQuestion:
    """A multiple-choice quiz question."""
    id: str
    question: str
    options: List[str]                # ['A) ...', 'B) ...', ...]
    correct: str                      # 'A', 'B', 'C', or 'D'
    explanation: str = ""


@dataclass
class Module:
    """A learning module containing lessons, exercises, and quiz."""
    id: str                           # e.g. "01_basics"
    title: str
    description: str
    lessons: List[Lesson] = field(default_factory=list)
    exercises: List[Exercise] = field(default_factory=list)
    quiz: List[QuizQuestion] = field(default_factory=list)
    order: int = 0                    # Sort order (extracted from directory name)
