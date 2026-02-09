"""Main application loop and screen routing."""

import sys
from pylearn.config import APP_NAME, APP_VERSION, APP_TAGLINE, QUIZ_PASS_THRESHOLD
from pylearn.cli import (
    show_menu, show_lesson, show_exercise, show_validation_result,
    show_quiz_question, show_quiz_result, show_progress_dashboard,
    press_enter, clear_screen, print_header, confirm,
)
from pylearn.utils.terminal import (
    bold, dim, success, error, warning, info, highlight, print_box,
)
from pylearn.curriculum import discover_modules
from pylearn.engine.validator import validate_output, validate_with_tests, validate_with_function
from pylearn.progress.tracker import (
    mark_lesson_complete, mark_exercise_complete,
    record_exercise_attempt, record_quiz_score,
    is_lesson_complete, is_exercise_complete, get_quiz_score,
)
from pylearn.progress.stats import get_dashboard_stats


def main():
    """Entry point for PyLearn."""
    # Handle CLI flags when invoked via `pylearn` command
    import sys
    args = sys.argv[1:]
    if args:
        from pylearn.__main__ import cli
        cli()
        return

    modules = discover_modules()

    if not modules:
        print("No curriculum modules found. Please check your installation.")
        sys.exit(1)

    while True:
        result = main_menu(modules)
        if result == 'quit':
            clear_screen()
            print(f"\n  {success('Thanks for learning with PyLearn! Keep coding!')}\n")
            break


def main_menu(modules):
    """Show the main menu."""
    options = [
        (f"Learn Python  {dim('- Start or continue lessons')}", "learn"),
        (f"Practice      {dim('- Exercises by module')}", "practice"),
        (f"Interview Prep {dim('- Coding problems')}", "interview"),
        (f"View Progress  {dim('- Dashboard & stats')}", "progress"),
    ]

    choice = show_menu(
        f"{APP_NAME} v{APP_VERSION}",
        options,
        subtitle=APP_TAGLINE,
        show_back=False,
        show_quit=True,
    )

    if choice == 'quit':
        return 'quit'
    elif choice == 'learn':
        module_browser(modules)
    elif choice == 'practice':
        practice_browser(modules)
    elif choice == 'interview':
        interview_browser(modules)
    elif choice == 'progress':
        stats = get_dashboard_stats(modules)
        show_progress_dashboard(stats)

    return 'continue'


def module_browser(modules):
    """Browse and select modules."""
    while True:
        options = []
        for m in modules:
            # Show completion indicator
            check = ""
            score = get_quiz_score(m.id)
            if score and score.get("pct", 0) >= QUIZ_PASS_THRESHOLD:
                check = success(" [COMPLETED]")
            label = f"{m.title}{check}"
            options.append((label, m))

        choice = show_menu(
            "Learn Python",
            options,
            subtitle="Select a module to begin learning",
        )

        if choice in ('back', 'quit'):
            return choice

        result = module_detail(choice)
        if result == 'quit':
            return 'quit'


def module_detail(module):
    """Show module detail: lessons, exercises, quiz."""
    while True:
        options = [
            (f"Lessons ({len(module.lessons)})", "lessons"),
            (f"Exercises ({len(module.exercises)})", "exercises"),
        ]
        if module.quiz:
            quiz_info = ""
            score = get_quiz_score(module.id)
            if score:
                quiz_info = f" - Last: {score['pct']}%"
            options.append((f"Take Quiz ({len(module.quiz)} questions){quiz_info}", "quiz"))

        choice = show_menu(
            module.title,
            options,
            subtitle=module.description,
        )

        if choice in ('back', 'quit'):
            return choice

        if choice == 'lessons':
            result = lesson_browser(module)
        elif choice == 'exercises':
            result = exercise_browser(module)
        elif choice == 'quiz':
            result = run_quiz(module)

        if result == 'quit':
            return 'quit'


def lesson_browser(module):
    """Browse lessons in a module."""
    while True:
        options = []
        for lesson in module.lessons:
            done = is_lesson_complete(module.id, lesson.id)
            check = success(" [done]") if done else ""
            options.append((f"{lesson.title}{check}", lesson))

        choice = show_menu(
            f"{module.title} - Lessons",
            options,
            subtitle="Select a lesson to read",
        )

        if choice in ('back', 'quit'):
            return choice

        continued = show_lesson(choice, module.id)
        if continued:
            mark_lesson_complete(module.id, choice.id)


def exercise_browser(module):
    """Browse exercises in a module."""
    while True:
        options = []
        for ex in module.exercises:
            done = is_exercise_complete(module.id, ex.id)
            check = success(" [done]") if done else ""
            diff_color = {"easy": success, "medium": warning, "hard": error}.get(
                ex.difficulty, dim
            )
            options.append((
                f"{ex.title} {diff_color(f'[{ex.difficulty}]')}{check}",
                ex
            ))

        choice = show_menu(
            f"{module.title} - Exercises",
            options,
            subtitle="Select an exercise to practice",
        )

        if choice in ('back', 'quit'):
            return choice

        run_exercise(module, choice)


def run_exercise(module, exercise):
    """Run a single exercise."""
    while True:
        code = show_exercise(exercise)
        if code is None:
            return 'back'

        record_exercise_attempt(module.id, exercise.id)

        # Validate
        if exercise.validator:
            result = validate_with_function(code, exercise.validator)
        elif exercise.test_cases:
            result = validate_with_tests(code, exercise.test_cases)
        elif exercise.expected_output:
            result = validate_output(code, exercise.expected_output)
        else:
            # No validation - just run and show output
            from pylearn.engine.runner import run_code
            exec_result = run_code(code)
            if exec_result.success:
                print(f"\n  {success('Output:')}")
                if exec_result.stdout:
                    print(f"  {exec_result.stdout}")
                mark_exercise_complete(module.id, exercise.id)
            else:
                print(f"\n  {error('Error:')}")
                print(f"  {exec_result.error}")
            press_enter()
            return 'done'

        show_validation_result(result)

        if result.success:
            mark_exercise_complete(module.id, exercise.id)
            return 'done'

        if not confirm("Try again?"):
            return 'back'


def run_quiz(module):
    """Run the quiz for a module."""
    if not module.quiz:
        print_box("No quiz available for this module yet.", style="info")
        press_enter()
        return 'back'

    results = []  # (is_correct, user_answer, question)
    score = 0

    for i, question in enumerate(module.quiz, 1):
        answer = show_quiz_question(question, i, len(module.quiz))
        if answer is None:
            return 'back'

        is_correct = answer == question.correct
        if is_correct:
            score += 1
        results.append((is_correct, answer, question))

    record_quiz_score(module.id, score, len(module.quiz))
    show_quiz_result(score, len(module.quiz), results, module.quiz)
    return 'done'


def practice_browser(modules):
    """Browse exercises across all modules."""
    while True:
        options = []
        for m in modules:
            if m.exercises:
                done = sum(1 for e in m.exercises
                           if is_exercise_complete(m.id, e.id))
                options.append((
                    f"{m.title} ({done}/{len(m.exercises)} completed)",
                    m
                ))

        if not options:
            print_box("No exercises available yet.", style="info")
            press_enter()
            return 'back'

        choice = show_menu(
            "Practice Exercises",
            options,
            subtitle="Select a module to practice",
        )

        if choice in ('back', 'quit'):
            return choice

        result = exercise_browser(choice)
        if result == 'quit':
            return 'quit'


def interview_browser(modules):
    """Browse interview prep modules."""
    interview_modules = [m for m in modules if m.order >= 10]

    if not interview_modules:
        print_box("Interview prep content coming soon!", style="info")
        press_enter()
        return 'back'

    while True:
        options = []
        for m in interview_modules:
            options.append((m.title, m))

        choice = show_menu(
            "Interview Prep",
            options,
            subtitle="Practice coding interview problems",
        )

        if choice in ('back', 'quit'):
            return choice

        result = module_detail(choice)
        if result == 'quit':
            return 'quit'
