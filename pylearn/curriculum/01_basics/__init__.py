"""Module 01: Python Basics -- hello world, variables, I/O, and comments."""

from pylearn.curriculum.base import Module, Lesson, Exercise, QuizQuestion

# ---------------------------------------------------------------------------
# Lessons
# ---------------------------------------------------------------------------

_lesson_hello_world = Lesson(
    id="hello_world",
    title="Hello, World!",
    content=(
        "Every programming journey starts with the same ritual: making the\n"
        "computer say hello. In Python this is delightfully simple -- a single\n"
        "call to the built-in print() function is all you need.\n\n"
        "print() is a built-in function, which means Python already knows about\n"
        "it and you can use it without importing anything. You pass it one or\n"
        "more values (called arguments) and it writes them to the screen,\n"
        "followed by a newline character so the cursor moves to the next line.\n\n"
        "Strings -- pieces of text -- must be enclosed in quotes. You can use\n"
        "single quotes ('Hello') or double quotes (\"Hello\"); both are\n"
        "perfectly valid. Pick one style and be consistent.\n\n"
        "You can pass multiple arguments to print() separated by commas. By\n"
        "default Python will place a space between each argument in the output.\n"
        "You can change this separator with the sep keyword argument.\n\n"
        "Python also supports f-strings (formatted string literals), which let\n"
        "you embed expressions directly inside a string by prefixing it with\n"
        "the letter f and placing expressions in curly braces. For example,\n"
        "f\"2 + 2 = {2 + 2}\" produces the string \"2 + 2 = 4\". We will\n"
        "explore f-strings more in later lessons.\n\n"
        "To run your first program, create a file called hello.py, type the\n"
        "code below, and execute it with the command `python hello.py` in your\n"
        "terminal. Congratulations -- you are now a Python programmer!"
    ),
    code_example=(
        "# Your very first Python program\n"
        "print(\"Hello, World!\")\n"
        "\n"
        "# print() accepts multiple arguments\n"
        "print(\"Hello\", \"World\", \"from\", \"Python\")\n"
        "\n"
        "# Quick f-string preview\n"
        "language = \"Python\"\n"
        "print(f\"Hello from {language}!\")\n"
    ),
    key_points=[
        "print() is a built-in function -- no imports required.",
        "Strings must be wrapped in quotes (single or double).",
        "Multiple arguments to print() are separated by spaces by default.",
        "f-strings let you embed expressions inside strings with curly braces.",
    ],
)

_lesson_variables = Lesson(
    id="variables",
    title="Variables & Assignment",
    content=(
        "Variables are one of the most fundamental concepts in programming.\n"
        "In Python, a variable is simply a name that refers to (or 'points\n"
        "to') a value stored in memory. You create a variable by using the\n"
        "assignment operator (=). The name goes on the left and the value on\n"
        "the right: x = 10.\n\n"
        "Python is dynamically typed, which means you do not have to declare\n"
        "the type of a variable ahead of time. The same variable can first\n"
        "hold an integer and later be reassigned to a string. While this\n"
        "flexibility is powerful, it also means you need to keep track of what\n"
        "each variable contains so you don't make mistakes.\n\n"
        "Variable names must follow a few rules. They can contain letters,\n"
        "digits, and underscores, but they cannot start with a digit. Python\n"
        "convention (PEP 8) recommends using snake_case for variable names --\n"
        "all lowercase words separated by underscores, such as my_variable or\n"
        "total_count.\n\n"
        "Certain words are reserved by Python (like class, def, return, if)\n"
        "and cannot be used as variable names. Trying to do so will raise a\n"
        "SyntaxError.\n\n"
        "Python also supports multiple assignment in a single line. You can\n"
        "write a, b = 1, 2 to assign 1 to a and 2 to b simultaneously. This\n"
        "is not just syntactic sugar -- it is a genuine parallel assignment,\n"
        "which makes swapping two variables trivially easy: a, b = b, a."
    ),
    code_example=(
        "# Simple assignment\n"
        "x = 10\n"
        "name = \"Alice\"\n"
        "pi = 3.14159\n"
        "\n"
        "# Dynamic typing -- the same variable can change type\n"
        "value = 42\n"
        "print(type(value))  # <class 'int'>\n"
        "value = \"now I'm a string\"\n"
        "print(type(value))  # <class 'str'>\n"
        "\n"
        "# Multiple assignment\n"
        "a, b = 1, 2\n"
        "print(a, b)  # 1 2\n"
        "\n"
        "# Swapping variables\n"
        "a, b = b, a\n"
        "print(a, b)  # 2 1\n"
    ),
    key_points=[
        "A variable is a name that points to a value -- created with =.",
        "Python is dynamically typed: no type declarations needed.",
        "Use snake_case for variable names (e.g. my_var, total_count).",
        "Names cannot start with a digit or use reserved words.",
        "Multiple assignment: a, b = 1, 2 assigns in parallel.",
    ],
)

_lesson_input_output = Lesson(
    id="input_output",
    title="Input and Output",
    content=(
        "Programs become much more interesting when they can interact with\n"
        "the user. Python provides the built-in input() function for reading\n"
        "text from the keyboard. When Python reaches an input() call, it\n"
        "pauses execution, optionally displays a prompt string, and waits for\n"
        "the user to type something and press Enter.\n\n"
        "One crucial detail: input() always returns a string, even if the\n"
        "user types a number. If you need an integer, you must explicitly\n"
        "convert the result with int(). Likewise, use float() for decimal\n"
        "numbers. Forgetting this conversion is one of the most common\n"
        "beginner mistakes and will lead to surprising behavior when you try\n"
        "to do arithmetic.\n\n"
        "For output, you already know print(). But let's go deeper into\n"
        "formatted output. f-strings (formatted string literals) are the\n"
        "modern, readable way to build strings that include variable values.\n"
        "Prefix the string with f and put any expression inside curly braces.\n"
        "You can even include format specifiers: f\"{price:.2f}\" formats a\n"
        "float to two decimal places.\n\n"
        "The print() function also accepts keyword arguments. sep controls\n"
        "the separator between multiple arguments (default is a space), and\n"
        "end controls what is printed at the end (default is a newline '\\n').\n"
        "These small knobs give you fine-grained control over your output\n"
        "without resorting to complex string manipulation."
    ),
    code_example=(
        "# Reading input from the user\n"
        "name = input(\"What is your name? \")\n"
        "print(f\"Nice to meet you, {name}!\")\n"
        "\n"
        "# Converting input to a number\n"
        "age = int(input(\"How old are you? \"))\n"
        "print(f\"In 10 years you will be {age + 10}.\")\n"
        "\n"
        "# Formatted output with f-strings\n"
        "price = 19.995\n"
        "print(f\"Total: ${price:.2f}\")  # Total: $20.00\n"
        "\n"
        "# Using sep and end with print()\n"
        "print(\"A\", \"B\", \"C\", sep=\"-\")  # A-B-C\n"
        "print(\"Hello\", end=\" \")\n"
        "print(\"World\")  # Hello World (on one line)\n"
    ),
    key_points=[
        "input() pauses the program and reads a line of text from the user.",
        "input() ALWAYS returns a str -- use int() or float() to convert.",
        "f-strings (f\"...\") embed expressions with {curly braces}.",
        "print(sep=..., end=...) gives fine control over output formatting.",
    ],
)

_lesson_comments = Lesson(
    id="comments",
    title="Comments & Code Style",
    content=(
        "Comments are notes you leave in your source code for yourself and\n"
        "other developers. Python ignores them completely when running your\n"
        "program, but they are invaluable for explaining *why* the code does\n"
        "something, not merely *what* it does. Good comments answer questions\n"
        "like 'Why did we choose this approach?' or 'What edge case does this\n"
        "handle?'\n\n"
        "In Python, a single-line comment starts with the hash character (#).\n"
        "Everything after # on that line is ignored by the interpreter. Place\n"
        "a space after the # for readability: '# This is a comment'.\n\n"
        "For multi-line explanations you can use consecutive # lines, or you\n"
        "can use triple-quoted strings (\"\"\"...\"\"\"). When a triple-quoted\n"
        "string appears as the first statement inside a function, class, or\n"
        "module, it becomes a docstring -- a special comment that Python\n"
        "stores and makes accessible via the __doc__ attribute and the help()\n"
        "function. Docstrings are the standard way to document what a\n"
        "function does, what parameters it takes, and what it returns.\n\n"
        "Beyond comments, Python has an official style guide called PEP 8.\n"
        "The most important PEP 8 conventions are: indent with 4 spaces (not\n"
        "tabs), limit lines to 79 characters, use snake_case for variable and\n"
        "function names, use UPPER_CASE for constants, and surround top-level\n"
        "definitions with two blank lines. Following PEP 8 makes your code\n"
        "consistent and easier for others (and your future self) to read."
    ),
    code_example=(
        "# This is a single-line comment\n"
        "x = 42  # Inline comment after code\n"
        "\n"
        "# You can stack multiple single-line comments\n"
        "# to explain something that needs\n"
        "# more than one line.\n"
        "\n"
        "def greet(name):\n"
        "    \"\"\"Return a greeting string for the given name.\n"
        "\n"
        "    Args:\n"
        "        name: The name of the person to greet.\n"
        "\n"
        "    Returns:\n"
        "        A friendly greeting string.\n"
        "    \"\"\"\n"
        "    return f\"Hello, {name}!\"\n"
        "\n"
        "# Access the docstring\n"
        "print(greet.__doc__)\n"
    ),
    key_points=[
        "Single-line comments start with # -- Python ignores the rest of the line.",
        "Docstrings are triple-quoted strings on the first line of a function/class/module.",
        "Comments should explain WHY, not WHAT -- the code already shows what.",
        "Follow PEP 8: 4-space indents, snake_case names, 79-char line limit.",
    ],
)

# ---------------------------------------------------------------------------
# Exercises
# ---------------------------------------------------------------------------

_exercise_hello = Exercise(
    id="hello_exercise",
    title="Say Hello",
    description="Print the text \"Hello, World!\" exactly (including punctuation).",
    expected_output="Hello, World!",
    solution='print("Hello, World!")',
    hints=[
        "Use the print() function",
        "Don't forget the quotes around the text",
    ],
    difficulty="easy",
)

_exercise_variables = Exercise(
    id="variables_exercise",
    title="Variable Swap",
    description=(
        "Two variables are already defined: a = 5 and b = 10.\n"
        "Swap their values so that a becomes 10 and b becomes 5,\n"
        "then print them separated by a space."
    ),
    starter_code="a = 5\nb = 10\n# Swap the values of a and b\n# Then print them",
    expected_output="10 5",
    solution="a = 5\nb = 10\na, b = b, a\nprint(a, b)",
    hints=[
        "Python supports multiple assignment: a, b = b, a",
    ],
    difficulty="easy",
)

_exercise_io = Exercise(
    id="io_exercise",
    title="Greeting Machine",
    description=(
        "Write code that stores the name \"PyLearner\" in a variable called\n"
        "`name` and prints \"Hello, PyLearner! Welcome to Python.\" using an\n"
        "f-string."
    ),
    expected_output="Hello, PyLearner! Welcome to Python.",
    solution='name = "PyLearner"\nprint(f"Hello, {name}! Welcome to Python.")',
    hints=[
        'Use an f-string: f"Hello, {name}!"',
    ],
    difficulty="easy",
)


def _validate_comments(namespace, stdout):
    """Validator for the comments exercise."""
    if "add" not in namespace:
        return False, "Function 'add' not defined"
    if not callable(namespace["add"]):
        return False, "'add' is not callable"
    if namespace["add"].__doc__ is None:
        return False, "Function has no docstring"
    if namespace["add"](2, 3) != 5:
        return False, "add(2, 3) should return 5"
    return True, "Function 'add' works correctly and has a docstring!"


_exercise_comments = Exercise(
    id="comments_exercise",
    title="Document a Function",
    description=(
        "Write a function called `add` that takes two parameters and returns\n"
        "their sum. The function must include a docstring (a triple-quoted\n"
        "string on the first line of the function body) that describes what\n"
        "it does."
    ),
    starter_code=(
        "# Define a function called 'add' with a docstring\n"
        "# that takes two parameters and returns their sum.\n"
    ),
    validator=_validate_comments,
    solution=(
        'def add(a, b):\n'
        '    """Add two numbers and return the result."""\n'
        '    return a + b'
    ),
    hints=[
        "A docstring is a string on the first line of a function",
        "Use triple quotes for docstrings",
    ],
    difficulty="easy",
)

# ---------------------------------------------------------------------------
# Quiz
# ---------------------------------------------------------------------------

_quiz = [
    QuizQuestion(
        id="q1_print",
        question="What function is used to display output in Python?",
        options=[
            "A) echo()",
            "B) print()",
            "C) display()",
            "D) write()",
        ],
        correct="B",
    ),
    QuizQuestion(
        id="q2_variable_name",
        question="Which of the following variable names is valid in Python?",
        options=[
            "A) 2name",
            "B) my-var",
            "C) my_var",
            "D) class",
        ],
        correct="C",
        explanation=(
            "Variable names can't start with a number (2name), can't use "
            "hyphens (my-var), and 'class' is a reserved word. Only my_var "
            "follows all the rules."
        ),
    ),
    QuizQuestion(
        id="q3_input_type",
        question="What type does the input() function always return?",
        options=[
            "A) int",
            "B) float",
            "C) str",
            "D) It depends on what the user types",
        ],
        correct="C",
        explanation=(
            "input() always returns a string. Use int() or float() to "
            "convert the result to a numeric type."
        ),
    ),
    QuizQuestion(
        id="q4_comment_syntax",
        question="Which is the correct way to write a single-line comment in Python?",
        options=[
            "A) // comment",
            "B) /* comment */",
            "C) # comment",
            "D) -- comment",
        ],
        correct="C",
    ),
    QuizQuestion(
        id="q5_multiple_assignment",
        question="What does `x, y = 10, 20` do?",
        options=[
            "A) Creates a tuple",
            "B) Assigns 10 to x and 20 to y",
            "C) Causes a SyntaxError",
            "D) Assigns 20 to both x and y",
        ],
        correct="B",
        explanation=(
            "Python supports multiple assignment in a single line. The "
            "values on the right are assigned to the names on the left in "
            "order: x gets 10 and y gets 20."
        ),
    ),
]

# ---------------------------------------------------------------------------
# Module definition
# ---------------------------------------------------------------------------

module = Module(
    id="01_basics",
    title="Python Basics",
    description="Your first steps with Python: hello world, variables, I/O, and comments",
    lessons=[
        _lesson_hello_world,
        _lesson_variables,
        _lesson_input_output,
        _lesson_comments,
    ],
    exercises=[
        _exercise_hello,
        _exercise_variables,
        _exercise_io,
        _exercise_comments,
    ],
    quiz=_quiz,
)
