"""Module 03: Control Flow — conditionals, loops, and comprehensions."""

from pylearn.curriculum.base import Module, Lesson, Exercise, QuizQuestion

# ---------------------------------------------------------------------------
# Lessons
# ---------------------------------------------------------------------------

conditionals = Lesson(
    id="conditionals",
    title="If, Elif, Else",
    content="""\
Control flow is the backbone of every meaningful program.  Without it your
code would execute line by line from top to bottom with no ability to make
decisions.  Python's conditional statements — if, elif, and else — let you
branch execution based on Boolean expressions, so different code runs under
different circumstances.

**Boolean Expressions and Comparison Operators**

A Boolean expression evaluates to either True or False.  Python provides a
full set of comparison operators to build these expressions:

  ==   equal to              !=   not equal to
  <    less than             >    greater than
  <=   less than or equal    >=   greater than or equal

You can chain comparisons naturally, just as you would in mathematics.  The
expression `1 < x < 10` is perfectly valid Python and is equivalent to
`1 < x and x < 10`, but far more readable.

**Logical Operators**

Python uses the English words `and`, `or`, and `not` instead of symbolic
operators.  `and` returns True only when *both* operands are True.  `or`
returns True when *at least one* operand is True.  `not` inverts a Boolean.
These operators short-circuit: `and` stops evaluating as soon as it finds a
False value, and `or` stops as soon as it finds a True value.

**If / Elif / Else Syntax**

The basic structure is:

    if condition:
        # runs when condition is True
    elif other_condition:
        # runs when the first condition is False but this one is True
    else:
        # runs when none of the above conditions are True

You can have as many `elif` branches as you need, and the `else` is optional.
Python evaluates conditions from top to bottom and executes only the *first*
branch that matches.

**Truthiness and Falsyness**

Python considers certain values "falsy" — they behave like False in a Boolean
context.  The falsy values are: False, None, 0 (any numeric zero), empty
strings (""), and empty collections ([], {}, set(), ()).  Everything else is
"truthy".  This means you can write `if my_list:` instead of
`if len(my_list) > 0:`.

**Ternary (Conditional) Expression**

Python supports a compact one-liner for simple conditional assignments:

    value = x if condition else y

This evaluates to `x` when the condition is True, and `y` otherwise.  Use it
for concise assignments, but avoid nesting ternary expressions — readability
matters more than brevity.
""",
    code_example="""\
# Grading example using if/elif/else
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score {score} earns grade: {grade}")  # Score 85 earns grade: B

# Chained comparison
x = 5
if 1 < x < 10:
    print(f"{x} is between 1 and 10")  # 5 is between 1 and 10

# Ternary expression
age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # adult
""",
    key_points=[
        "Comparison operators: ==, !=, <, >, <=, >=",
        "Logical operators: and, or, not (short-circuit evaluation)",
        "Chained comparisons like 1 < x < 10 are valid and Pythonic",
        "Falsy values: False, None, 0, '', [], {}, set(), ()",
        "Ternary expression: value = x if condition else y",
    ],
)

for_loops = Lesson(
    id="for_loops",
    title="For Loops",
    content="""\
The `for` loop is Python's primary tool for iteration.  Unlike C-style for
loops that rely on an index variable and a stop condition, Python's for loop
iterates directly over the *items* of any iterable object — a list, string,
tuple, dictionary, file, or any object that implements the iterator protocol.

**Iterating Over Sequences**

The simplest form walks through each element:

    for item in sequence:
        # do something with item

This pattern works with lists, strings, tuples, sets, and dictionaries (which
iterate over keys by default).

**The range() Function**

When you need to iterate over a sequence of numbers, `range()` is your tool.
It takes up to three arguments: start (default 0), stop (exclusive), and step
(default 1).  `range(5)` produces 0, 1, 2, 3, 4.  `range(2, 10, 3)` produces
2, 5, 8.  The range object is lazy — it generates numbers on demand rather
than creating a full list in memory.

**enumerate() — When You Need the Index**

If you need both the index and the value, use `enumerate()` instead of
manually managing a counter.  It returns pairs of (index, value) and accepts
an optional `start` parameter.

**zip() — Parallel Iteration**

`zip()` lets you iterate over multiple sequences in parallel, yielding tuples
of corresponding elements.  It stops when the shortest input is exhausted.

**Nested Loops**

Placing one for loop inside another lets you iterate over combinations.  The
inner loop runs to completion for every single iteration of the outer loop.
This is common when working with 2-D data structures such as grids or
matrices.

**break, continue, and the else Clause**

`break` exits the loop immediately.  `continue` skips the rest of the current
iteration and jumps to the next one.  Python also supports an `else` clause on
for loops: the else block executes only if the loop completes normally
(i.e., without hitting a `break`).  This is particularly useful for search
patterns where you want to know if no match was found.
""",
    code_example="""\
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# Using enumerate to get index and value
print()
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

# zip: parallel iteration
names = ["Alice", "Bob", "Charlie"]
scores = [92, 85, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# range with step
print("\\nEven numbers from 0 to 8:")
for n in range(0, 10, 2):
    print(n, end=" ")  # 0 2 4 6 8

# for-else: search pattern
print("\\n")
numbers = [1, 3, 5, 7, 9]
for n in numbers:
    if n % 2 == 0:
        print(f"Found even number: {n}")
        break
else:
    print("No even numbers found")  # This runs because no break occurred
""",
    key_points=[
        "for loops iterate directly over items in any iterable",
        "range(start, stop, step) generates number sequences lazily",
        "enumerate() gives (index, value) pairs — avoid manual counters",
        "zip() iterates over multiple sequences in parallel",
        "break exits; continue skips to next iteration",
        "The else clause on a for loop runs only if no break occurred",
    ],
)

while_loops = Lesson(
    id="while_loops",
    title="While Loops",
    content="""\
While loops repeat a block of code as long as a condition remains True.  They
are the right choice when you do not know in advance how many iterations you
need — for example, when waiting for user input, reading data until a
sentinel value appears, or running a game loop.

**Basic Syntax**

    while condition:
        # body — runs repeatedly while condition is True

The condition is checked *before* each iteration.  If it is False from the
start, the body never executes at all.

**Infinite Loops with break**

A common and perfectly acceptable pattern is to write an intentionally infinite
loop and use `break` to exit when a specific condition is met:

    while True:
        data = get_input()
        if data == "quit":
            break
        process(data)

This avoids awkward flag variables and keeps the exit logic close to the
action that triggers it.

**While-Else**

Just like for loops, while loops support an `else` clause.  The else block
runs only when the while condition becomes False naturally — *not* when the
loop is terminated by `break`.  This can be useful for "search and bail"
patterns, though it is less common than the for-else variant.

**Common Patterns**

*Sentinel value:* Keep reading input until a special value signals "stop."

*Input validation:* Repeatedly prompt the user until they provide valid data.

*Countdown / count-up:* Use a counter variable that you manually increment or
decrement inside the loop.

*Convergence:* Repeat a calculation until the result changes by less than some
threshold (common in numerical algorithms).

**Avoiding Infinite Loops**

Infinite loops that are *unintentional* are a common bug.  Always make sure
the loop body modifies something that will eventually make the condition
False, or that there is a guaranteed `break` path.
""",
    code_example="""\
# Countdown
print("Countdown:")
n = 5
while n > 0:
    print(n, end=" ")
    n -= 1
print("Liftoff!")

# Input validation pattern (simulated)
# In a real program you would use input(), here we simulate it:
valid_responses = ["yes", "no"]
simulated_inputs = ["maybe", "nah", "yes"]

print("\\nInput validation pattern:")
index = 0
while True:
    response = simulated_inputs[index]  # simulates input()
    index += 1
    print(f"  Got: {response!r}")
    if response in valid_responses:
        print(f"  Accepted: {response}")
        break
    print("  Invalid! Please enter 'yes' or 'no'.")

# While-else
print("\\nSearching for a negative number:")
values = [4, 7, 2, 9]
i = 0
while i < len(values):
    if values[i] < 0:
        print(f"Found negative: {values[i]}")
        break
    i += 1
else:
    print("No negative numbers found")  # Runs because no break occurred
""",
    key_points=[
        "while loops repeat as long as the condition is True",
        "The condition is evaluated before each iteration",
        "'while True' with break is a clean pattern for unknown iteration counts",
        "while-else runs the else block only if no break occurred",
        "Always ensure the loop can terminate to avoid infinite loops",
    ],
)

comprehensions = Lesson(
    id="comprehensions",
    title="Comprehensions",
    content="""\
Comprehensions are one of Python's most beloved features.  They provide a
concise, readable syntax for creating lists, dictionaries, and sets from
existing iterables — often replacing multi-line loops with a single expressive
line.

**List Comprehensions**

The basic form is:

    [expression for item in iterable]

You can add a condition to filter elements:

    [expression for item in iterable if condition]

For example, `[x**2 for x in range(10) if x % 2 == 0]` produces the squares
of even numbers from 0 through 9.  This is equivalent to a for loop that
appends to a list, but it is more concise and often faster because the
iteration happens at C speed inside the interpreter.

**Dictionary Comprehensions**

    {key_expr: value_expr for item in iterable}

This creates a new dictionary.  You can also add an `if` filter.  A common
use case is inverting a dictionary:  `{v: k for k, v in original.items()}`.

**Set Comprehensions**

    {expression for item in iterable}

Identical syntax to a dict comprehension but without the colon.  The result
is a set, so duplicate values are automatically removed.

**Generator Expressions**

    (expression for item in iterable)

This looks like a list comprehension wrapped in parentheses, but it returns a
*generator* — a lazy iterator that produces values on demand rather than
building the entire collection in memory.  Generator expressions are ideal
when you only need to iterate once or when the data set is very large.  Note
that a generator expression is **not** a tuple comprehension.

**Nested Comprehensions**

You can nest multiple `for` clauses:

    [(x, y) for x in range(3) for y in range(3)]

The order of the for clauses matches the order of equivalent nested for loops
(outer loop first, inner loop second).

**When Not to Use Comprehensions**

Comprehensions should make your code *clearer*, not more cryptic.  If the
expression or conditions become complex, a regular loop with a descriptive
variable name is preferable.  A good rule of thumb: if the comprehension does
not fit comfortably on one or two lines, rewrite it as a loop.
""",
    code_example="""\
# List comprehension vs. traditional loop
# Traditional loop:
squares_loop = []
for x in range(1, 6):
    squares_loop.append(x ** 2)
print("Loop:         ", squares_loop)   # [1, 4, 9, 16, 25]

# Equivalent list comprehension:
squares_comp = [x ** 2 for x in range(1, 6)]
print("Comprehension:", squares_comp)   # [1, 4, 9, 16, 25]

# Filtered list comprehension — even squares only
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print("Even squares: ", even_squares)   # [4, 16, 36, 64, 100]

# Dict comprehension — word lengths
words = ["hello", "world", "python"]
word_lengths = {w: len(w) for w in words}
print("Word lengths: ", word_lengths)   # {'hello': 5, 'world': 5, 'python': 6}

# Set comprehension — unique first letters
first_letters = {w[0] for w in words}
print("First letters:", first_letters)  # {'h', 'w', 'p'}

# Generator expression — sum of squares without building a list
total = sum(x ** 2 for x in range(1, 101))
print("Sum of squares 1-100:", total)   # 338350
""",
    key_points=[
        "List comprehension: [expr for item in iterable if condition]",
        "Dict comprehension: {k: v for item in iterable}",
        "Set comprehension: {expr for item in iterable}",
        "Generator expression: (expr for item in iterable) — lazy evaluation",
        "Nested for clauses mirror the order of nested for loops",
        "Keep comprehensions readable; use regular loops for complex logic",
    ],
)

match_case = Lesson(
    id="match_case",
    title="Match/Case (Python 3.10+)",
    content="""\
Python 3.10 introduced structural pattern matching with the `match` and
`case` statements.  At first glance it resembles a switch/case from languages
like C or Java, but it is far more powerful.  Pattern matching does not merely
compare values — it *destructures* data and binds variables to the parts that
match.

**Basic Syntax**

    match subject:
        case pattern1:
            # action for pattern1
        case pattern2:
            # action for pattern2

Python evaluates the subject once, then tries each case pattern from top to
bottom.  The first pattern that matches determines which block executes.

**Literal Patterns**

The simplest patterns match specific values:

    case 200:    # matches the integer 200
    case "quit": # matches the string "quit"

**Capture Patterns**

A bare name in a pattern captures the value into a variable:

    case (x, y):  # captures the two elements of a 2-tuple

Be careful: a bare name always matches, so `case x:` acts like a catch-all.

**Wildcard Pattern _**

The underscore `_` matches anything but does not bind a variable.  It is the
conventional "default" case:

    case _:
        print("No match found")

**OR Patterns with |**

Use the pipe operator to combine alternatives:

    case "quit" | "exit" | "q":
        sys.exit()

**Guard Clauses with if**

Add a condition to a case to further restrict when it matches:

    case x if x > 0:
        print(f"{x} is positive")

The pattern must match *and* the guard must be True for the block to execute.

**Class Patterns**

You can match against class instances and destructure their attributes:

    case Point(x=0, y=0):
        print("Origin")

This is particularly useful when processing command objects, AST nodes, or
event types.

**When to Use match/case**

Pattern matching shines when you have multiple distinct shapes of data to
handle — command parsing, protocol message handling, AST processing, or state
machines.  For simple value comparisons, if/elif/else is still perfectly fine.
""",
    code_example="""\
# Command parser using match/case
def handle_command(command: str) -> str:
    match command.split():
        case ["quit" | "exit"]:
            return "Goodbye!"
        case ["hello"]:
            return "Hello, World!"
        case ["hello", name]:
            return f"Hello, {name}!"
        case ["add", x, y]:
            return f"Result: {int(x) + int(y)}"
        case ["say", *words]:
            return " ".join(words)
        case _:
            return f"Unknown command: {command}"

# Test the command parser
commands = [
    "hello",
    "hello Alice",
    "add 3 5",
    "say Python is great",
    "quit",
    "unknown stuff",
]

for cmd in commands:
    result = handle_command(cmd)
    print(f"  {cmd!r:25s} -> {result}")

# Pattern matching with guard clauses
def classify_number(n):
    match n:
        case 0:
            return "zero"
        case x if x > 0:
            return "positive"
        case x if x < 0:
            return "negative"

print(f"\\nclassify_number(-3) = {classify_number(-3)}")
print(f"classify_number(0)  = {classify_number(0)}")
print(f"classify_number(7)  = {classify_number(7)}")
""",
    key_points=[
        "match/case is structural pattern matching, not just a switch",
        "Literal patterns match exact values; capture patterns bind variables",
        "_ is the wildcard that matches anything without binding",
        "Use | for OR patterns: case 'quit' | 'exit'",
        "Guard clauses (if) add extra conditions to a case",
        "Requires Python 3.10 or later",
    ],
)

# ---------------------------------------------------------------------------
# Exercises
# ---------------------------------------------------------------------------

fizzbuzz = Exercise(
    id="fizzbuzz",
    title="FizzBuzz",
    difficulty="easy",
    description="""\
Print the numbers from 1 to 20, one per line — but with the following twists:
- If the number is divisible by 3, print "Fizz" instead of the number.
- If the number is divisible by 5, print "Buzz" instead of the number.
- If the number is divisible by *both* 3 and 5, print "FizzBuzz".
Otherwise, print the number itself.
""",
    starter_code="""\
# FizzBuzz: Print numbers 1-20 with Fizz/Buzz/FizzBuzz substitutions
for i in range(1, 21):
    # Your code here
    pass
""",
    expected_output=(
        "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n"
        "11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz"
    ),
    hints=[
        "Use % (modulo) to check divisibility",
        "Check FizzBuzz (divisible by both) first",
    ],
    solution="""\
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
""",
)

sum_evens = Exercise(
    id="sum_evens",
    title="Sum of Evens",
    difficulty="easy",
    description="""\
Calculate the sum of all even numbers from 1 to 50 (inclusive) using a for
loop, then print the result.
""",
    starter_code="""\
# Calculate the sum of even numbers from 1 to 50
total = 0
# Your code here

print(total)
""",
    expected_output="650",
    hints=[
        "Use range(2, 51, 2) or check n % 2 == 0",
    ],
    solution="""\
total = 0
for n in range(2, 51, 2):
    total += n
print(total)
""",
)

guess_number = Exercise(
    id="guess_number",
    title="Number Guesser Logic",
    difficulty="medium",
    description="""\
Write a function called `check_guess(guess, target)` that compares a guess to
a target number and returns:
- "Too low"  if the guess is less than the target,
- "Too high" if the guess is greater than the target,
- "Correct!" if the guess equals the target.
""",
    starter_code="""\
def check_guess(guess, target):
    # Your code here
    pass
""",
    test_cases=[
        {
            "name": "Too low",
            "input_code": "print(check_guess(5, 10))",
            "expected": "Too low",
        },
        {
            "name": "Too high",
            "input_code": "print(check_guess(15, 10))",
            "expected": "Too high",
        },
        {
            "name": "Correct",
            "input_code": "print(check_guess(10, 10))",
            "expected": "Correct!",
        },
    ],
    hints=[
        "Use if/elif/else to compare guess to target",
        "Return a string from the function, don't print inside it",
    ],
    solution="""\
def check_guess(guess, target):
    if guess < target:
        return "Too low"
    elif guess > target:
        return "Too high"
    else:
        return "Correct!"
""",
)

comprehension_exercise = Exercise(
    id="comprehension_exercise",
    title="Comprehension Power",
    difficulty="medium",
    description="""\
Using a single list comprehension, create a list of the squares of all even
numbers from 1 to 20 (inclusive), then print the list.
""",
    starter_code="""\
# Create a list of squares of even numbers from 1 to 20 using a comprehension
result = []  # Replace with a list comprehension
print(result)
""",
    expected_output="[4, 16, 36, 64, 100, 144, 196, 256, 324, 400]",
    hints=[
        "Filter for even numbers with an if clause in the comprehension",
    ],
    solution="""\
result = [x ** 2 for x in range(1, 21) if x % 2 == 0]
print(result)
""",
)

pyramid = Exercise(
    id="pyramid",
    title="Star Pyramid",
    difficulty="medium",
    description="""\
Print a right-aligned pyramid of stars (*) with 5 rows.  Row 1 has 1 star,
row 2 has 2 stars, and so on up to row 5 with 5 stars.  Each row should be
right-aligned to a width of 5 characters.
""",
    starter_code="""\
# Print a right-aligned pyramid of 5 rows
for i in range(1, 6):
    # Your code here
    pass
""",
    expected_output="    *\n   **\n  ***\n ****\n*****",
    hints=[
        "Use string multiplication and rjust() or format specifiers",
    ],
    solution="""\
for i in range(1, 6):
    print(("*" * i).rjust(5))
""",
)

# ---------------------------------------------------------------------------
# Quiz Questions
# ---------------------------------------------------------------------------

q1 = QuizQuestion(
    id="q1_boolean_logic",
    question="What is the output of: print(5 > 3 and 2 > 4)?",
    options=[
        "A) True",
        "B) False",
        "C) None",
        "D) Error",
    ],
    correct="B",
    explanation=(
        "5 > 3 is True, but 2 > 4 is False.  True and False evaluates to "
        "False because 'and' requires both operands to be True."
    ),
)

q2 = QuizQuestion(
    id="q2_range",
    question="What does range(2, 10, 3) produce?",
    options=[
        "A) [2, 5, 8]",
        "B) [2, 3, 4, 5, 6, 7, 8, 9]",
        "C) [2, 4, 6, 8]",
        "D) [3, 6, 9]",
    ],
    correct="A",
    explanation=(
        "range(start, stop, step) begins at 2 and increments by 3 each time: "
        "2, 5, 8.  The next value (11) would exceed the stop value of 10, so "
        "iteration stops."
    ),
)

q3 = QuizQuestion(
    id="q3_continue",
    question="What keyword skips to the next iteration of a loop?",
    options=[
        "A) break",
        "B) pass",
        "C) continue",
        "D) skip",
    ],
    correct="C",
    explanation=(
        "'continue' skips the rest of the current iteration and jumps to the "
        "next one.  'break' exits the loop entirely.  'pass' does nothing.  "
        "'skip' is not a Python keyword."
    ),
)

q4 = QuizQuestion(
    id="q4_comprehension",
    question="Which is a valid list comprehension?",
    options=[
        "A) [x**2 for x in range(5)]",
        "B) [for x in range(5): x**2]",
        "C) (x**2 for x in range(5))",
        "D) Both A and C",
    ],
    correct="A",
    explanation=(
        "Option A is a list comprehension.  Option C uses parentheses, which "
        "creates a generator expression, not a list comprehension.  Option B "
        "uses invalid syntax.  Only A is a valid list comprehension."
    ),
)

q5 = QuizQuestion(
    id="q5_for_else",
    question="What does the `else` clause on a for loop execute?",
    options=[
        "A) When the loop body raises an error",
        "B) When the loop completes without break",
        "C) After every iteration",
        "D) Never",
    ],
    correct="B",
    explanation=(
        "The else clause on a for (or while) loop runs only when the loop "
        "completes normally — that is, without encountering a 'break' "
        "statement.  If 'break' is executed, the else block is skipped."
    ),
)

# ---------------------------------------------------------------------------
# Module assembly
# ---------------------------------------------------------------------------

module = Module(
    id="03_control_flow",
    title="Control Flow",
    description="Control program execution with conditionals, loops, and comprehensions",
    lessons=[
        conditionals,
        for_loops,
        while_loops,
        comprehensions,
        match_case,
    ],
    exercises=[
        fizzbuzz,
        sum_evens,
        guess_number,
        comprehension_exercise,
        pyramid,
    ],
    quiz=[
        q1,
        q2,
        q3,
        q4,
        q5,
    ],
)
