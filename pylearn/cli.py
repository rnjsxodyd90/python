"""CLI interaction: menus, prompts, paged text, code input."""

from pylearn.utils.terminal import (
    clear_screen, print_header, print_separator, print_box,
    bold, dim, success, error, warning, info, highlight,
    code_style, header_style, get_terminal_size, Color, colorize,
)
from pylearn.utils.formatting import format_code_block, wrap_text


def show_menu(title, options, subtitle=None, show_back=True, show_quit=True):
    """Display a numbered menu and get user choice.

    Args:
        title: Menu title.
        options: List of (label, value) tuples.
        subtitle: Optional subtitle.
        show_back: Show 'B) Back' option.
        show_quit: Show 'Q) Quit' option.

    Returns:
        The value from the selected option, or 'back'/'quit'.
    """
    clear_screen()
    print_header(title, subtitle)

    for i, (label, _) in enumerate(options, 1):
        print(f"  {info(str(i))}) {label}")

    print()
    if show_back:
        print(f"  {dim('B) Back')}")
    if show_quit:
        print(f"  {dim('Q) Quit')}")

    print()
    while True:
        choice = input(f"  {bold('Choose an option:')} ").strip().lower()

        if choice == 'q' and show_quit:
            return 'quit'
        if choice == 'b' and show_back:
            return 'back'

        try:
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                return options[idx][1]
        except ValueError:
            pass

        print(f"  {warning('Invalid choice. Try again.')}")


def show_lesson(lesson, module_id):
    """Display a lesson with content, code examples, and key points."""
    clear_screen()
    print_header(lesson.title, f"Module: {module_id}")

    # Content
    for paragraph in lesson.content.split("\n\n"):
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        print(wrap_text(paragraph, indent="  "))
        print()

    # Code example
    if lesson.code_example:
        print(f"  {header_style('Example Code:')}")
        print()
        print(code_style(format_code_block(lesson.code_example)))
        print()

    # Key points
    if lesson.key_points:
        print(f"  {header_style('Key Points:')}")
        for point in lesson.key_points:
            print(f"    {success('*')} {point}")
        print()

    print_separator()
    print()
    print(f"  {dim('Press Enter to continue, or type')} {info('b')} {dim('to go back')}")
    choice = input("  ").strip().lower()
    return choice != 'b'


def show_exercise(exercise):
    """Display an exercise and collect user code.

    Returns:
        User's code string, or None if they go back.
    """
    clear_screen()
    print_header(exercise.title, f"Difficulty: {exercise.difficulty}")

    print(f"  {bold('Description:')}")
    print(wrap_text(exercise.description, indent="    "))
    print()

    if exercise.starter_code:
        print(f"  {bold('Starter Code:')}")
        print(code_style(format_code_block(exercise.starter_code)))
        print()

    if exercise.expected_output:
        print(f"  {bold('Expected Output:')}")
        print(f"    {code_style(exercise.expected_output)}")
        print()

    print_separator()
    print()
    print(f"  {info('Enter your code below')} {dim('(type DONE on a new line to submit, BACK to go back):')}")
    print(f"  {dim('Hint: type HINT for a hint, SOLUTION to see the answer')}")
    print()

    hint_index = 0
    while True:
        lines = []
        while True:
            try:
                line = input(f"  {dim('>>>')} ")
            except EOFError:
                return None

            upper = line.strip().upper()
            if upper == "DONE":
                break
            elif upper == "BACK":
                return None
            elif upper == "HINT":
                if exercise.hints and hint_index < len(exercise.hints):
                    print(f"\n  {warning('Hint:')} {exercise.hints[hint_index]}\n")
                    hint_index += 1
                else:
                    print(f"\n  {dim('No more hints available.')}\n")
                continue
            elif upper == "SOLUTION":
                if exercise.solution:
                    print(f"\n  {warning('Solution:')}")
                    print(code_style(format_code_block(exercise.solution)))
                    print()
                else:
                    print(f"\n  {dim('No solution available.')}\n")
                continue
            else:
                lines.append(line)

        code = "\n".join(lines)
        if code.strip():
            return code

        print(f"  {warning('No code entered. Try again or type BACK to go back.')}")


def show_validation_result(result):
    """Display validation results."""
    print()
    if result.error:
        print_box(f"Error:\n{result.error}", style="error")
        return

    if result.success:
        print_box(f"All tests passed! ({result.summary})", style="success")
    else:
        print()
        for p in result.passed:
            print(f"  {success('PASS')} {p['name']}")
        for f in result.failed:
            print(f"  {error('FAIL')} {f['name']}")
            print(f"       Expected: {code_style(f['expected'])}")
            print(f"       Got:      {code_style(f['actual'])}")
        print()
        print(f"  {warning(result.summary)}")

    print()
    input(f"  {dim('Press Enter to continue...')}")


def show_quiz_question(question, number, total):
    """Display a quiz question and get the answer.

    Returns:
        The user's answer letter (uppercase), or None for quit.
    """
    clear_screen()
    print_header(f"Quiz - Question {number}/{total}")

    print(f"  {bold(question.question)}")
    print()

    for option in question.options:
        print(f"    {option}")
    print()

    while True:
        answer = input(f"  {bold('Your answer (A/B/C/D):')} ").strip().upper()
        if answer in ('A', 'B', 'C', 'D'):
            return answer
        if answer in ('Q', 'QUIT'):
            return None
        print(f"  {warning('Please enter A, B, C, or D.')}")


def show_quiz_result(score, total, results, questions):
    """Display quiz results."""
    clear_screen()
    pct = round(score / total * 100) if total > 0 else 0
    print_header("Quiz Results", f"Score: {score}/{total} ({pct}%)")

    for i, (correct, user_answer, question) in enumerate(zip(
        [r for r in results], [r for r in results], questions
    ), 1):
        pass  # We'll use the detailed version below

    for i, (is_correct, user_ans, q) in enumerate(results, 1):
        if is_correct:
            print(f"  {success('*')} Q{i}: {success('Correct')}")
        else:
            print(f"  {error('x')} Q{i}: {error('Wrong')} "
                  f"(You: {user_ans}, Correct: {q.correct})")
            if q.explanation:
                print(f"       {dim(q.explanation)}")

    print()
    if pct >= 70:
        print_box(f"Congratulations! You passed with {pct}%!", style="success")
    else:
        print_box(f"Score: {pct}%. You need 70% to pass. Try again!", style="warning")

    print()
    input(f"  {dim('Press Enter to continue...')}")
    return pct


def show_progress_dashboard(stats):
    """Display the progress dashboard."""
    clear_screen()
    print_header("Your Progress", "Track your Python learning journey")

    # Overall
    print(f"  {bold('Overall Progress:')}")
    bar = _progress_bar(stats["overall_pct"], 40)
    print(f"    {bar} {stats['overall_pct']}%")
    print()

    print(f"    Lessons:   {info(str(stats['completed_lessons']))}/{stats['total_lessons']}")
    print(f"    Exercises: {info(str(stats['completed_exercises']))}/{stats['total_exercises']}")
    print(f"    Quizzes:   {info(str(stats['quizzes_passed']))} passed / "
          f"{stats['quizzes_taken']} taken / {stats['total_quizzes']} total")
    print()

    # Streak
    print(f"  {bold('Streak:')}")
    streak_icon = success("*") if stats["current_streak"] > 0 else dim("*")
    print(f"    {streak_icon} Current: {info(str(stats['current_streak']))} days")
    print(f"    {dim('*')} Longest: {info(str(stats['longest_streak']))} days")
    print()

    # Per-module
    print(f"  {bold('Modules:')}")
    print_separator()
    for ms in stats["module_stats"]:
        bar = _progress_bar(ms["completion_pct"], 20)
        quiz_info = ""
        if ms["quiz_score"]:
            qpct = ms["quiz_score"]["pct"]
            quiz_info = f" | Quiz: {success(str(qpct)+'%') if qpct >= 70 else warning(str(qpct)+'%')}"
        print(f"    {bar} {ms['title']}")
        print(f"         Lessons: {ms['lessons_done']}/{ms['lessons_total']} | "
              f"Exercises: {ms['exercises_done']}/{ms['exercises_total']}{quiz_info}")
    print()

    print_separator()
    input(f"\n  {dim('Press Enter to go back...')}")


def _progress_bar(pct, width=30):
    """Create a text progress bar."""
    from pylearn.utils.terminal import BAR_FULL, BAR_EMPTY
    filled = int(width * pct / 100)
    empty = width - filled
    bar_color = Color.BRIGHT_GREEN if pct >= 70 else Color.BRIGHT_YELLOW if pct >= 30 else Color.BRIGHT_RED
    bar = colorize(BAR_FULL * filled, bar_color) + dim(BAR_EMPTY * empty)
    return f"[{bar}]"


def confirm(prompt="Continue?"):
    """Ask a yes/no confirmation."""
    answer = input(f"  {bold(prompt)} {dim('(y/n):')} ").strip().lower()
    return answer in ('y', 'yes')


def press_enter(message="Press Enter to continue..."):
    """Wait for Enter key."""
    input(f"  {dim(message)}")
