"""Progress dashboard statistics."""

from pylearn.progress.tracker import load_progress
from pylearn.config import QUIZ_PASS_THRESHOLD


def get_dashboard_stats(modules):
    """Compute stats for the progress dashboard.

    Args:
        modules: List of Module objects from curriculum.

    Returns:
        Dict with stats for display.
    """
    data = load_progress()

    total_lessons = sum(len(m.lessons) for m in modules)
    total_exercises = sum(len(m.exercises) for m in modules)
    total_quizzes = len(modules)

    completed_lessons = len(data.get("lessons_completed", []))
    completed_exercises = len(data.get("exercises_completed", []))
    quiz_scores = data.get("quiz_scores", {})
    quizzes_taken = len(quiz_scores)
    quizzes_passed = sum(1 for s in quiz_scores.values()
                         if s.get("pct", 0) >= QUIZ_PASS_THRESHOLD)

    streak = data.get("streak", {})

    # Per-module breakdown
    module_stats = []
    for m in modules:
        m_lessons = len(m.lessons)
        m_done = sum(1 for l in m.lessons
                     if f"{m.id}/{l.id}" in data.get("lessons_completed", []))
        m_exercises = len(m.exercises)
        m_ex_done = sum(1 for e in m.exercises
                        if f"{m.id}/{e.id}" in data.get("exercises_completed", []))
        m_quiz = quiz_scores.get(m.id)

        pct = round(m_done / m_lessons * 100) if m_lessons > 0 else 0

        module_stats.append({
            "id": m.id,
            "title": m.title,
            "lessons_total": m_lessons,
            "lessons_done": m_done,
            "exercises_total": m_exercises,
            "exercises_done": m_ex_done,
            "quiz_score": m_quiz,
            "completion_pct": pct,
        })

    overall_pct = round(completed_lessons / total_lessons * 100) if total_lessons > 0 else 0

    return {
        "total_lessons": total_lessons,
        "completed_lessons": completed_lessons,
        "total_exercises": total_exercises,
        "completed_exercises": completed_exercises,
        "total_quizzes": total_quizzes,
        "quizzes_taken": quizzes_taken,
        "quizzes_passed": quizzes_passed,
        "current_streak": streak.get("current", 0),
        "longest_streak": streak.get("longest", 0),
        "overall_pct": overall_pct,
        "module_stats": module_stats,
    }
