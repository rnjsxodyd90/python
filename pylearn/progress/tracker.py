"""JSON-based progress persistence with atomic writes."""

import json
import os
import time
from pylearn.config import DATA_DIR, PROGRESS_FILE


def _ensure_data_dir():
    """Create data directory if it doesn't exist."""
    os.makedirs(DATA_DIR, exist_ok=True)


def _default_progress():
    """Return a fresh progress structure."""
    return {
        "version": 1,
        "created_at": time.time(),
        "updated_at": time.time(),
        "lessons_completed": [],     # List of "module_id/lesson_id"
        "exercises_completed": [],    # List of "module_id/exercise_id"
        "exercise_attempts": {},      # "module_id/exercise_id" -> count
        "quiz_scores": {},            # "module_id" -> {"score": X, "total": Y, "pct": Z}
        "streak": {
            "current": 0,
            "longest": 0,
            "last_date": None,
        },
        "total_time_seconds": 0,
    }


def load_progress():
    """Load progress from JSON file."""
    _ensure_data_dir()
    if not os.path.exists(PROGRESS_FILE):
        return _default_progress()
    try:
        with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except (json.JSONDecodeError, KeyError):
        return _default_progress()


def save_progress(data):
    """Save progress with atomic write (write tmp, rename)."""
    _ensure_data_dir()
    data["updated_at"] = time.time()

    tmp_path = PROGRESS_FILE + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    # Atomic rename (on Windows, need to remove target first)
    if os.path.exists(PROGRESS_FILE):
        os.replace(tmp_path, PROGRESS_FILE)
    else:
        os.rename(tmp_path, PROGRESS_FILE)


def _update_streak(data):
    """Update daily streak."""
    today = time.strftime("%Y-%m-%d")
    last = data["streak"].get("last_date")

    if last == today:
        return  # Already counted today

    if last:
        # Check if yesterday
        import datetime
        last_date = datetime.date.fromisoformat(last)
        today_date = datetime.date.fromisoformat(today)
        diff = (today_date - last_date).days
        if diff == 1:
            data["streak"]["current"] += 1
        elif diff > 1:
            data["streak"]["current"] = 1
    else:
        data["streak"]["current"] = 1

    data["streak"]["last_date"] = today
    data["streak"]["longest"] = max(
        data["streak"]["longest"],
        data["streak"]["current"],
    )


def mark_lesson_complete(module_id, lesson_id):
    """Mark a lesson as completed."""
    data = load_progress()
    key = f"{module_id}/{lesson_id}"
    if key not in data["lessons_completed"]:
        data["lessons_completed"].append(key)
    _update_streak(data)
    save_progress(data)


def mark_exercise_complete(module_id, exercise_id):
    """Mark an exercise as completed."""
    data = load_progress()
    key = f"{module_id}/{exercise_id}"
    if key not in data["exercises_completed"]:
        data["exercises_completed"].append(key)
    _update_streak(data)
    save_progress(data)


def record_exercise_attempt(module_id, exercise_id):
    """Record an exercise attempt."""
    data = load_progress()
    key = f"{module_id}/{exercise_id}"
    data["exercise_attempts"][key] = data["exercise_attempts"].get(key, 0) + 1
    save_progress(data)


def record_quiz_score(module_id, score, total):
    """Record a quiz score."""
    data = load_progress()
    pct = round(score / total * 100) if total > 0 else 0
    data["quiz_scores"][module_id] = {
        "score": score,
        "total": total,
        "pct": pct,
        "timestamp": time.time(),
    }
    _update_streak(data)
    save_progress(data)


def is_lesson_complete(module_id, lesson_id):
    """Check if a lesson is completed."""
    data = load_progress()
    return f"{module_id}/{lesson_id}" in data["lessons_completed"]


def is_exercise_complete(module_id, exercise_id):
    """Check if an exercise is completed."""
    data = load_progress()
    return f"{module_id}/{exercise_id}" in data["exercises_completed"]


def get_quiz_score(module_id):
    """Get quiz score for a module, or None if not taken."""
    data = load_progress()
    return data["quiz_scores"].get(module_id)
