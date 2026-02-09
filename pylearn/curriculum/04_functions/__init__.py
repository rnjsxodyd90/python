"""Module 04: Functions -- Define reusable code with functions."""

from pylearn.curriculum.base import Module, Lesson, Exercise, QuizQuestion

# ---------------------------------------------------------------------------
# Lessons
# ---------------------------------------------------------------------------

defining_functions = Lesson(
    id="defining_functions",
    title="Defining Functions",
    content="""\
Functions are the fundamental building blocks of reusable code in Python.
A function groups a set of statements so they can be executed whenever you
need them, as many times as you like.

**The `def` Keyword**

You create a function with the `def` keyword, followed by a name, parentheses
for parameters, and a colon.  The indented block underneath is the function
body:

    def say_hello():
        print("Hello!")

**Naming Conventions**

Python functions follow `snake_case` by convention -- all lowercase with
underscores separating words:

    def calculate_area(width, height):
        ...

Names should be descriptive verbs or verb-phrases that communicate what the
function does.

**Parameters vs Arguments**

*Parameters* are the names listed in the function definition.
*Arguments* are the actual values passed when calling the function.

    def greet(name):       # `name` is a parameter
        print(f"Hi, {name}!")

    greet("Alice")         # "Alice" is an argument

**The `return` Statement**

`return` sends a value back to the caller.  Once `return` executes, the
function exits immediately:

    def add(a, b):
        return a + b

    result = add(3, 4)     # result is 7

**Implicit `None`**

If a function has no `return` statement, or a bare `return` with no value,
it returns `None` implicitly:

    def do_nothing():
        pass

    x = do_nothing()       # x is None

**Returning Multiple Values**

Python can return several values at once as a tuple:

    def min_max(numbers):
        return min(numbers), max(numbers)

    lo, hi = min_max([3, 1, 4, 1, 5])   # lo=1, hi=5

**Docstrings**

The first string literal inside a function body is its *docstring*.  It
documents what the function does and is accessible via `help()` or the
`__doc__` attribute:

    def area(radius):
        \"\"\"Calculate the area of a circle with the given radius.\"\"\"
        import math
        return math.pi * radius ** 2

    print(area.__doc__)
    # Calculate the area of a circle with the given radius.

Writing clear docstrings is a professional best practice.
""",
    code_example="""\
def celsius_to_fahrenheit(celsius):
    \"\"\"Convert a temperature from Celsius to Fahrenheit.\"\"\"
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    \"\"\"Convert a temperature from Fahrenheit to Celsius.\"\"\"
    return (fahrenheit - 32) * 5 / 9


# Using the functions
boiling_c = 100
boiling_f = celsius_to_fahrenheit(boiling_c)
print(f"{boiling_c}C = {boiling_f}F")     # 100C = 212.0F

body_temp_f = 98.6
body_temp_c = fahrenheit_to_celsius(body_temp_f)
print(f"{body_temp_f}F = {body_temp_c:.1f}C")  # 98.6F = 37.0C

# Multiple return values
def convert_both(temp, unit):
    \"\"\"Return a temperature in both C and F.\"\"\"
    if unit == "C":
        return temp, celsius_to_fahrenheit(temp)
    else:
        return fahrenheit_to_celsius(temp), temp

c, f = convert_both(100, "C")
print(f"Celsius: {c}, Fahrenheit: {f}")    # Celsius: 100, Fahrenheit: 212.0
""",
    key_points=[
        "Use `def` to define a function, followed by its name and parentheses.",
        "Parameters are placeholders in the definition; arguments are the actual values passed.",
        "`return` sends a value back to the caller and exits the function.",
        "A function without `return` (or with a bare `return`) returns None.",
        "You can return multiple values as a tuple and unpack them on the caller side.",
        "Always write a docstring as the first line of the function body.",
    ],
)

parameters = Lesson(
    id="parameters",
    title="Parameters & Arguments",
    content="""\
Python provides a rich set of ways to pass data into functions.  Mastering
them lets you write flexible, self-documenting APIs.

**Positional Arguments**

The simplest form -- arguments are matched to parameters by position:

    def power(base, exponent):
        return base ** exponent

    power(2, 10)   # base=2, exponent=10 -> 1024

**Keyword Arguments**

You can name the parameters explicitly when calling.  This improves
readability and lets you pass them in any order:

    power(exponent=10, base=2)   # same result: 1024

**Default Values**

Parameters can have default values.  If the caller omits them, the default
is used:

    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"

    greet("Alice")            # "Hello, Alice!"
    greet("Bob", "Howdy")     # "Howdy, Bob!"

IMPORTANT: Never use a mutable object (like a list or dict) as a default
value!  It is shared across all calls.  Use `None` instead and create the
object inside the function:

    def append_to(item, target=None):
        if target is None:
            target = []
        target.append(item)
        return target

**`*args` -- Variable Positional Arguments**

Prefixing a parameter with `*` collects any extra positional arguments into
a tuple:

    def total(*args):
        return sum(args)

    total(1, 2, 3)       # 6
    total(10, 20)         # 30

**`**kwargs` -- Variable Keyword Arguments**

Prefixing with `**` collects extra keyword arguments into a dictionary:

    def print_info(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")

    print_info(name="Alice", age=30)

**Keyword-Only Arguments (after `*`)**

Parameters placed after `*` (or after `*args`) can only be supplied as
keyword arguments:

    def fetch(url, *, timeout=30, retries=3):
        ...

    fetch("https://example.com", timeout=10)   # OK
    fetch("https://example.com", 10)           # TypeError!

**Positional-Only Parameters (before `/`)**

Parameters before `/` can only be supplied positionally (Python 3.8+):

    def calculate(x, y, /, operation="add"):
        ...

    calculate(3, 4)                  # OK
    calculate(x=3, y=4)             # TypeError!
    calculate(3, 4, operation="mul") # OK

**Parameter Order Rule**

When combining all types, they must appear in this order:

    def func(pos_only, /, normal, *args, kw_only, **kwargs):
        ...
""",
    code_example="""\
def create_tag(tag, content, /, *, cls=None, id=None, **attrs):
    \"\"\"Build an HTML tag string demonstrating all parameter types.

    Parameters
    ----------
    tag      : str  (positional-only)  -- the HTML tag name
    content  : str  (positional-only)  -- text inside the tag
    cls      : str  (keyword-only)     -- CSS class
    id       : str  (keyword-only)     -- element id
    **attrs  : str  (extra keywords)   -- any other HTML attributes
    \"\"\"
    parts = [f"<{tag}"]

    if cls:
        parts.append(f' class="{cls}"')
    if id:
        parts.append(f' id="{id}"')
    for attr, value in attrs.items():
        parts.append(f' {attr}="{value}"')

    parts.append(f">{content}</{tag}>")
    return "".join(parts)


# Positional-only for tag and content
print(create_tag("h1", "Welcome"))
# <h1>Welcome</h1>

# Keyword-only for cls and id
print(create_tag("p", "Hello", cls="intro", id="greeting"))
# <p class="intro" id="greeting">Hello</p>

# Extra keyword arguments collected by **attrs
print(create_tag("a", "Click me", href="https://example.com", target="_blank"))
# <a href="https://example.com" target="_blank">Click me</a>


# Demonstrating *args
def summarize(*args, sep=" | "):
    \"\"\"Join all positional arguments with a separator.\"\"\"
    return sep.join(str(a) for a in args)

print(summarize("Alice", 30, "NYC"))           # Alice | 30 | NYC
print(summarize("x", "y", "z", sep=" -> "))    # x -> y -> z
""",
    key_points=[
        "Positional arguments are matched by position; keyword arguments by name.",
        "Default parameter values let callers omit arguments that have sensible defaults.",
        "Never use mutable objects (lists, dicts) as default values -- use None instead.",
        "`*args` collects extra positional arguments into a tuple.",
        "`**kwargs` collects extra keyword arguments into a dictionary.",
        "Parameters after `*` are keyword-only; parameters before `/` are positional-only.",
        "Parameter order: positional-only, /, normal, *args, keyword-only, **kwargs.",
    ],
)

scope = Lesson(
    id="scope",
    title="Scope & Namespaces",
    content="""\
Understanding *scope* -- where a name is visible -- is essential for writing
correct Python.  Python uses the **LEGB rule** to resolve names.

**The LEGB Rule**

When Python encounters a name, it searches these scopes in order:

1. **L -- Local**: Names defined inside the current function.
2. **E -- Enclosing**: Names in the local scopes of any enclosing functions
   (relevant for nested functions).
3. **G -- Global**: Names defined at the top level of the module.
4. **B -- Built-in**: Names pre-defined in Python (`print`, `len`, `range`, etc.).

If the name is not found in any scope, Python raises a `NameError`.

**Local Scope**

Variables assigned inside a function are local to that function:

    def f():
        x = 10       # local to f
        print(x)

    f()              # 10
    print(x)         # NameError: name 'x' is not defined

**Global Scope**

Variables defined at the module level (outside any function) are global:

    count = 0        # global

    def show():
        print(count) # reads the global -- OK

**The `global` Keyword**

To *modify* a global variable inside a function, you must declare it with
`global`:

    count = 0

    def increment():
        global count
        count += 1

    increment()
    print(count)     # 1

Without `global`, the assignment `count += 1` would create a new local
variable and raise an `UnboundLocalError` because you are reading it
before the local assignment completes.

**The `nonlocal` Keyword**

`nonlocal` is the equivalent of `global` but for enclosing (not global)
scopes.  It is used inside nested functions:

    def outer():
        x = 0
        def inner():
            nonlocal x
            x += 1
        inner()
        print(x)      # 1

    outer()

**Variable Shadowing**

A local variable with the same name as a global one *shadows* it -- the
local takes priority within that function:

    x = "global"

    def f():
        x = "local"
        print(x)      # "local"

    f()
    print(x)           # "global"

Shadowing is legal but can cause confusion.  Avoid it unless intentional.

**Namespace Dictionaries**

Every scope is backed by a dictionary.  You can inspect them:

    - `locals()`   -- returns a dict of the current local namespace
    - `globals()`  -- returns a dict of the module-level namespace
    - `dir()`      -- lists names in the current scope (simplified view)

These are mainly useful for debugging and introspection.
""",
    code_example="""\
# --- Demonstrating LEGB scope levels ---

builtin_example = len  # 'len' comes from the Built-in scope

module_var = "I am global"   # Global scope


def outer_function():
    enclosing_var = "I am enclosing"   # Enclosing scope (for inner)

    def inner_function():
        local_var = "I am local"       # Local scope

        # Python searches: Local -> Enclosing -> Global -> Built-in
        print(local_var)         # Found in Local
        print(enclosing_var)     # Found in Enclosing
        print(module_var)        # Found in Global
        print(len([1, 2, 3]))   # 'len' found in Built-in

    inner_function()


outer_function()

# --- global vs nonlocal ---

counter = 0

def increment_global():
    global counter
    counter += 1

def make_local_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

increment_global()
increment_global()
print(f"Global counter: {counter}")  # Global counter: 2

local_counter = make_local_counter()
print(local_counter())  # 1
print(local_counter())  # 2
print(local_counter())  # 3

# --- Inspecting namespaces ---
def show_namespace():
    a = 1
    b = 2
    print("Local names:", list(locals().keys()))   # ['a', 'b']

show_namespace()
""",
    key_points=[
        "Python resolves names using the LEGB rule: Local, Enclosing, Global, Built-in.",
        "Variables assigned inside a function are local by default.",
        "Use `global` to modify a module-level variable inside a function.",
        "Use `nonlocal` to modify a variable from an enclosing (non-global) scope.",
        "Variable shadowing occurs when a local name hides a name from an outer scope.",
        "`locals()` and `globals()` return dictionaries of their respective namespaces.",
    ],
)

closures = Lesson(
    id="closures",
    title="Closures",
    content="""\
A **closure** is a nested function that remembers and has access to variables
from its enclosing scope, even after the outer function has finished
executing.  Closures are one of Python's most powerful features for creating
flexible, stateful functions without using classes.

**Nested Functions**

You can define a function inside another function:

    def outer():
        def inner():
            print("I'm inner!")
        inner()

    outer()   # "I'm inner!"

The inner function is only accessible inside `outer`.

**What Makes a Closure?**

A closure is created when three conditions are met:

1. There is a nested function.
2. The nested function references a variable from the enclosing function.
3. The enclosing function returns the nested function.

    def outer(message):
        def inner():
            print(message)   # `message` is "captured"
        return inner         # return the function object

    say_hi = outer("Hi!")
    say_hi()                 # "Hi!" -- `message` is remembered

After `outer("Hi!")` finishes, its local variable `message` would normally
be garbage-collected.  But because `inner` still references it, Python keeps
it alive.  That is the closure.

**Factory Functions**

Closures are ideal for creating families of related functions:

    def make_multiplier(factor):
        def multiply(x):
            return x * factor
        return multiply

    double = make_multiplier(2)
    triple = make_multiplier(3)

    print(double(5))   # 10
    print(triple(5))   # 15

Each returned function "remembers" its own `factor`.

**Practical Uses**

1. **Counters**: Maintain state without a class.
2. **Memoization / Caching**: Cache results of expensive computations.
3. **Callback factories**: Generate event handlers with pre-configured data.
4. **Decorators**: Nearly all decorators are closures (covered later).

**Inspecting Closures**

You can see what a closure captured via the `__closure__` attribute:

    double = make_multiplier(2)
    print(double.__closure__[0].cell_contents)   # 2

**Late Binding Gotcha**

Closures capture *variables*, not *values*.  A common pitfall with loops:

    funcs = []
    for i in range(3):
        funcs.append(lambda: i)

    print([f() for f in funcs])   # [2, 2, 2]  -- all see the final i!

Fix with a default argument to capture the current value:

    funcs = []
    for i in range(3):
        funcs.append(lambda i=i: i)

    print([f() for f in funcs])   # [0, 1, 2]
""",
    code_example="""\
# --- Factory function: make_multiplier ---

def make_multiplier(factor):
    \"\"\"Return a function that multiplies its argument by `factor`.\"\"\"
    def multiply(x):
        return x * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(f"double(5) = {double(5)}")   # double(5) = 10
print(f"triple(5) = {triple(5)}")   # triple(5) = 15

# Inspect the closure
print(f"double captures: {double.__closure__[0].cell_contents}")  # 2


# --- Counter maker using closure + nonlocal ---

def make_counter(start=0):
    \"\"\"Return a counter function that increments from `start`.\"\"\"
    count = start
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counter_a = make_counter()
counter_b = make_counter(100)

print(counter_a(), counter_a(), counter_a())  # 1 2 3
print(counter_b(), counter_b())               # 101 102


# --- Simple memoization closure ---

def make_memoized(func):
    \"\"\"Return a memoized version of `func`.\"\"\"
    cache = {}
    def memoized(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return memoized

def slow_square(n):
    \"\"\"Pretend this is expensive.\"\"\"
    return n * n

fast_square = make_memoized(slow_square)
print(fast_square(4))    # 16 (computed)
print(fast_square(4))    # 16 (cached)
""",
    key_points=[
        "A closure is a nested function that captures variables from its enclosing scope.",
        "Closures remember enclosing variables even after the outer function returns.",
        "Factory functions use closures to generate specialized functions.",
        "Closures capture variables (references), not values -- beware late binding in loops.",
        "Fix the loop-closure gotcha by using a default argument to snapshot the value.",
        "Closures are the mechanism behind decorators, memoization, and callback factories.",
    ],
)

lambdas = Lesson(
    id="lambdas",
    title="Lambda Functions",
    content="""\
A **lambda** is a small, anonymous function defined in a single expression.
It is useful when you need a short throwaway function, typically as an
argument to higher-order functions like `sorted()`, `map()`, or `filter()`.

**Basic Syntax**

    lambda parameters: expression

The expression is evaluated and returned automatically (no `return` keyword).

    square = lambda x: x ** 2
    print(square(5))   # 25

This is equivalent to:

    def square(x):
        return x ** 2

**When to Use Lambdas**

Lambdas shine when:
- You need a simple function for a one-time use.
- Passing a short key or transformation to another function.
- The logic fits in a single expression.

**When NOT to Use Lambdas**

Avoid lambdas when:
- The logic is complex or needs multiple statements.
- You need a docstring (lambdas cannot have one).
- You would assign it to a variable -- just use `def` instead. PEP 8
  explicitly advises against `square = lambda x: x ** 2`.

**With `sorted()` -- Key Functions**

One of the most common uses is providing a `key` argument:

    names = ["Charlie", "alice", "Bob"]
    print(sorted(names, key=lambda s: s.lower()))
    # ['alice', 'Bob', 'Charlie']

    pairs = [(1, "b"), (3, "a"), (2, "c")]
    print(sorted(pairs, key=lambda p: p[1]))
    # [(3, 'a'), (1, 'b'), (2, 'c')]

**With `map()` and `filter()`**

    nums = [1, 2, 3, 4, 5]

    squared = list(map(lambda x: x ** 2, nums))
    print(squared)   # [1, 4, 9, 16, 25]

    evens = list(filter(lambda x: x % 2 == 0, nums))
    print(evens)     # [2, 4]

Note: List comprehensions are often more readable than `map`/`filter` with
lambdas:

    squared = [x ** 2 for x in nums]
    evens   = [x for x in nums if x % 2 == 0]

**Lambdas With `max()` and `min()`**

    people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    oldest = max(people, key=lambda p: p[1])
    print(oldest)   # ('Charlie', 35)

**Multiple Arguments**

    add = lambda x, y: x + y
    print(add(3, 4))   # 7

**Limitations**

- Only a single expression (no statements like `if`/`for`/`while`).
- Conditional expressions are allowed: `lambda x: "even" if x % 2 == 0 else "odd"`.
- No annotations or decorators.
""",
    code_example="""\
# --- Sorting with lambda keys ---

students = [
    {"name": "Alice",   "grade": 88, "age": 20},
    {"name": "Bob",     "grade": 95, "age": 22},
    {"name": "Charlie", "grade": 72, "age": 19},
    {"name": "Diana",   "grade": 91, "age": 21},
]

# Sort by grade, highest first
by_grade = sorted(students, key=lambda s: s["grade"], reverse=True)
for s in by_grade:
    print(f'{s["name"]}: {s["grade"]}')
# Bob: 95
# Diana: 91
# Alice: 88
# Charlie: 72

print()

# Sort by age, youngest first
by_age = sorted(students, key=lambda s: s["age"])
for s in by_age:
    print(f'{s["name"]}: {s["age"]}')
# Charlie: 19
# Alice: 20
# Diana: 21
# Bob: 22

print()

# Multi-key sort: by grade descending, then name ascending
by_grade_name = sorted(students, key=lambda s: (-s["grade"], s["name"]))
for s in by_grade_name:
    print(f'{s["name"]}: {s["grade"]}')
# Bob: 95
# Diana: 91
# Alice: 88
# Charlie: 72

print()

# Using map and filter with lambdas
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares_of_evens = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(f"Squares of evens: {squares_of_evens}")
# Squares of evens: [4, 16, 36, 64, 100]

# Equivalent (and often preferred) list comprehension:
squares_of_evens_lc = [x ** 2 for x in numbers if x % 2 == 0]
print(f"Same with comprehension: {squares_of_evens_lc}")
""",
    key_points=[
        "A lambda is a small anonymous function: `lambda params: expression`.",
        "Lambdas can only contain a single expression -- no statements.",
        "Use lambdas as throwaway functions for `sorted()`, `map()`, `filter()`, `max()`, etc.",
        "Do NOT assign a lambda to a variable as a substitute for `def` (PEP 8).",
        "List comprehensions are often more readable than `map`/`filter` with lambdas.",
        "Lambdas support multiple arguments and conditional expressions.",
    ],
)

recursion = Lesson(
    id="recursion",
    title="Recursion",
    content="""\
**Recursion** is a technique where a function calls itself to solve a
problem by breaking it into smaller sub-problems of the same kind.  It is
a natural fit for problems that have a self-similar structure (trees, nested
data, mathematical sequences).

**Two Essential Parts**

Every recursive function MUST have:

1. **Base case**: A condition that stops the recursion.  Without it, the
   function calls itself forever and crashes with a `RecursionError`.
2. **Recursive case**: The function calls itself with a "smaller" or
   "simpler" input that moves toward the base case.

**Classic Example: Factorial**

    n! = n * (n-1) * ... * 1
    0! = 1  (base case)

    def factorial(n):
        if n == 0:          # base case
            return 1
        return n * factorial(n - 1)  # recursive case

    factorial(5)
    # 5 * factorial(4)
    # 5 * 4 * factorial(3)
    # 5 * 4 * 3 * factorial(2)
    # 5 * 4 * 3 * 2 * factorial(1)
    # 5 * 4 * 3 * 2 * 1 * factorial(0)
    # 5 * 4 * 3 * 2 * 1 * 1  = 120

**Classic Example: Fibonacci**

    fib(0) = 0
    fib(1) = 1
    fib(n) = fib(n-1) + fib(n-2)

    def fib(n):
        if n <= 1:
            return n
        return fib(n - 1) + fib(n - 2)

The naive Fibonacci implementation is *very* slow for large n because it
recalculates the same values many times.  This can be fixed with
memoization (caching).

**The Call Stack**

Each recursive call adds a new *frame* to the call stack.  Python has a
default recursion limit of 1000 frames.  You can check and change it:

    import sys
    print(sys.getrecursionlimit())    # 1000
    sys.setrecursionlimit(2000)       # increase (use with caution!)

Exceeding the limit raises `RecursionError: maximum recursion depth exceeded`.

**Recursive vs Iterative**

Many recursive solutions can be rewritten iteratively with a loop.  The
iterative version is usually more memory-efficient because it does not
build up stack frames:

    # Iterative factorial
    def factorial_iter(n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

Choose recursion when:
- The problem naturally maps to recursive sub-problems (trees, graphs).
- Code clarity is more important than raw performance.

Choose iteration when:
- Performance or stack depth is a concern.
- The problem is naturally sequential.

**Tail Recursion (and Python's Stance)**

A tail-recursive function is one where the recursive call is the very last
operation.  Some languages optimize tail recursion to avoid growing the
stack.  Python does NOT perform tail-call optimization by design (Guido van
Rossum's choice).  So even tail-recursive functions in Python will still
consume stack frames.

**Tree Traversal -- A Natural Fit**

Recursion excels with hierarchical data:

    def print_tree(node, indent=0):
        print(" " * indent + node["name"])
        for child in node.get("children", []):
            print_tree(child, indent + 2)
""",
    code_example="""\
# --- Factorial: recursive and iterative ---

def factorial(n):
    \"\"\"Recursive factorial.\"\"\"
    if n == 0:
        return 1
    return n * factorial(n - 1)

def factorial_iter(n):
    \"\"\"Iterative factorial.\"\"\"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(f"factorial(5)      = {factorial(5)}")       # 120
print(f"factorial_iter(5) = {factorial_iter(5)}")   # 120


# --- Fibonacci: naive vs memoized ---

def fib(n):
    \"\"\"Naive recursive Fibonacci (slow for large n).\"\"\"
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def fib_memo(n, cache=None):
    \"\"\"Memoized Fibonacci (fast).\"\"\"
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]

print(f"fib(10)      = {fib(10)}")        # 55
print(f"fib_memo(50) = {fib_memo(50)}")   # 12586269025


# --- Tree traversal ---

file_system = {
    "name": "root",
    "children": [
        {"name": "documents", "children": [
            {"name": "resume.pdf"},
            {"name": "cover_letter.docx"},
        ]},
        {"name": "photos", "children": [
            {"name": "vacation.jpg"},
        ]},
        {"name": "readme.txt"},
    ],
}

def print_tree(node, indent=0):
    \"\"\"Recursively print a tree structure.\"\"\"
    print(" " * indent + node["name"])
    for child in node.get("children", []):
        print_tree(child, indent + 2)

print_tree(file_system)
# root
#   documents
#     resume.pdf
#     cover_letter.docx
#   photos
#     vacation.jpg
#   readme.txt
""",
    key_points=[
        "Recursion is a function calling itself to solve smaller sub-problems.",
        "Every recursive function needs a base case to stop and a recursive case to progress.",
        "Python's default recursion limit is 1000 -- exceeding it raises RecursionError.",
        "Naive recursion can be very slow; memoization (caching) dramatically improves performance.",
        "Python does NOT optimize tail recursion, so deep recursion always uses stack frames.",
        "Use recursion for naturally hierarchical problems; prefer iteration when performance matters.",
    ],
)

# ---------------------------------------------------------------------------
# Exercises
# ---------------------------------------------------------------------------

greet_exercise = Exercise(
    id="greet_exercise",
    title="Greeting Function",
    difficulty="easy",
    description="""\
Write a function `greet(name, greeting="Hello")` that returns a formatted
greeting string.

The returned string should be: "{greeting}, {name}!"

For example:
    greet("Alice")           -> "Hello, Alice!"
    greet("Bob", "Hi")       -> "Hi, Bob!"
""",
    starter_code="""\
def greet(name, greeting="Hello"):
    # Your code here
    pass

# Test it
print(greet("Alice"))
print(greet("Bob", "Hi"))
print(greet(greeting="Hey", name="Charlie"))
""",
    solution="""\
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
""",
    test_cases=[
        {
            "name": "Default greeting",
            "input_code": "print(greet('Alice'))",
            "expected": "Hello, Alice!",
        },
        {
            "name": "Custom greeting",
            "input_code": "print(greet('Bob', 'Hi'))",
            "expected": "Hi, Bob!",
        },
        {
            "name": "Keyword arg",
            "input_code": "print(greet(greeting='Hey', name='Charlie'))",
            "expected": "Hey, Charlie!",
        },
    ],
    hints=[
        "Use an f-string to format the return value.",
        "Remember to use `return`, not `print`, inside the function.",
    ],
)

args_kwargs = Exercise(
    id="args_kwargs",
    title="Flexible Function",
    difficulty="medium",
    description="""\
Write a function `make_profile(**kwargs)` that accepts any number of keyword
arguments and returns a formatted string with each key-value pair on a
separate line in the format "key: value", sorted alphabetically by key.

For example:
    make_profile(name="Alice", age=30)
    # Returns:
    # "age: 30
    # name: Alice"
""",
    starter_code="""\
def make_profile(**kwargs):
    # Your code here
    pass

# Test it
print(make_profile(name="Alice", age=30))
print(make_profile(city="NYC"))
""",
    solution="""\
def make_profile(**kwargs):
    lines = [f"{key}: {value}" for key, value in sorted(kwargs.items())]
    return "\\n".join(lines)
""",
    test_cases=[
        {
            "name": "Basic profile",
            "input_code": "print(make_profile(name='Alice', age=30))",
            "expected": "age: 30\nname: Alice",
        },
        {
            "name": "Single field",
            "input_code": "print(make_profile(city='NYC'))",
            "expected": "city: NYC",
        },
    ],
    hints=[
        "Use sorted(kwargs.items()) to iterate in alphabetical order by key.",
        "Use an f-string and '\\n'.join() to build the result.",
    ],
)


def _validate_counter(namespace, stdout):
    """Validate the make_counter exercise."""
    if "make_counter" not in namespace:
        return False, "Function 'make_counter' not defined"
    counter = namespace["make_counter"]()
    results = [counter() for _ in range(5)]
    if results == [1, 2, 3, 4, 5]:
        return True, "Counter works correctly!"
    return False, f"Expected [1, 2, 3, 4, 5], got {results}"


scope_exercise = Exercise(
    id="scope_exercise",
    title="Counter with Closure",
    difficulty="medium",
    description="""\
Write a function `make_counter()` that returns a counter function.

Each time you call the returned counter function, it should increment an
internal count by 1 and return the new count.  The first call returns 1,
the second returns 2, and so on.

Example:
    counter = make_counter()
    print(counter())  # 1
    print(counter())  # 2
    print(counter())  # 3
""",
    starter_code="""\
def make_counter():
    # Your code here
    pass

# Test it
counter = make_counter()
print(counter())  # Should print 1
print(counter())  # Should print 2
print(counter())  # Should print 3
""",
    solution="""\
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter
""",
    validator=_validate_counter,
    hints=[
        "Use a nested function",
        "Use nonlocal to modify the enclosing variable",
    ],
)

lambda_sort = Exercise(
    id="lambda_sort",
    title="Lambda Sorting",
    difficulty="easy",
    description="""\
Given a list of student tuples (name, grade):

    students = [('Alice', 88), ('Bob', 95), ('Charlie', 72), ('Diana', 91)]

Sort them by grade (the second element) in **descending** order and print
the resulting list.

Expected output:
    [('Bob', 95), ('Diana', 91), ('Alice', 88), ('Charlie', 72)]
""",
    starter_code="""\
students = [('Alice', 88), ('Bob', 95), ('Charlie', 72), ('Diana', 91)]

# Sort by grade descending and print the result
""",
    solution="""\
students = [('Alice', 88), ('Bob', 95), ('Charlie', 72), ('Diana', 91)]
print(sorted(students, key=lambda s: s[1], reverse=True))
""",
    expected_output="[('Bob', 95), ('Diana', 91), ('Alice', 88), ('Charlie', 72)]",
    hints=[
        "Use sorted() with key parameter",
        "Use lambda to access the second element",
    ],
)

factorial_exercise = Exercise(
    id="factorial",
    title="Recursive Factorial",
    difficulty="easy",
    description="""\
Write a recursive function `factorial(n)` that returns n! (n factorial).

Remember:
    - 0! = 1  (base case)
    - n! = n * (n-1)!  (recursive case)

Example:
    factorial(5)  -> 120   (5 * 4 * 3 * 2 * 1)
""",
    starter_code="""\
def factorial(n):
    # Your code here
    pass

# Test it
print(factorial(0))   # 1
print(factorial(1))   # 1
print(factorial(5))   # 120
print(factorial(10))  # 3628800
""",
    solution="""\
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
""",
    test_cases=[
        {
            "name": "factorial(0)",
            "input_code": "print(factorial(0))",
            "expected": "1",
        },
        {
            "name": "factorial(1)",
            "input_code": "print(factorial(1))",
            "expected": "1",
        },
        {
            "name": "factorial(5)",
            "input_code": "print(factorial(5))",
            "expected": "120",
        },
        {
            "name": "factorial(10)",
            "input_code": "print(factorial(10))",
            "expected": "3628800",
        },
    ],
    hints=[
        "The base case is when n == 0: return 1.",
        "The recursive case is: return n * factorial(n - 1).",
    ],
)


def _validate_decorator(namespace, stdout):
    """Validate the shout decorator exercise."""
    if "shout" not in namespace:
        return False, "Decorator 'shout' not defined"

    @namespace["shout"]
    def hello():
        return "hello world"

    result = hello()
    if result == "HELLO WORLD":
        return True, "Decorator works correctly!"
    return False, f"Expected 'HELLO WORLD', got {result!r}"


decorator_intro = Exercise(
    id="decorator_intro",
    title="Simple Decorator",
    difficulty="hard",
    description="""\
Write a decorator `@shout` that converts the return value of a function
to UPPERCASE.

When applied to a function that returns a string, the decorated function
should return that string in all caps.

Example:
    @shout
    def greet():
        return "hello world"

    print(greet())   # "HELLO WORLD"

A decorator is a function that takes a function as an argument, defines a
wrapper function inside, and returns the wrapper.
""",
    starter_code="""\
def shout(func):
    # Your code here -- define and return a wrapper function
    pass

@shout
def greet():
    return "hello world"

@shout
def farewell():
    return "goodbye"

print(greet())      # Should print: HELLO WORLD
print(farewell())   # Should print: GOODBYE
""",
    solution="""\
def shout(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper
""",
    validator=_validate_decorator,
    hints=[
        "A decorator is a function that takes a function and returns a new function",
        "Use functools.wraps for best practice, but it's not required here",
    ],
)

# ---------------------------------------------------------------------------
# Quiz Questions
# ---------------------------------------------------------------------------

quiz_return_none = QuizQuestion(
    id="return_none",
    question="What does a function return if there is no return statement?",
    options=[
        "A) 0",
        "B) \"\"",
        "C) None",
        "D) Error",
    ],
    correct="C",
    explanation=(
        "If a function has no `return` statement, or uses a bare `return` with "
        "no value, Python implicitly returns `None`."
    ),
)

quiz_args = QuizQuestion(
    id="args_collect",
    question="What does *args collect?",
    options=[
        "A) Keyword arguments",
        "B) Positional arguments as a tuple",
        "C) A list",
        "D) A dictionary",
    ],
    correct="B",
    explanation=(
        "`*args` collects any extra positional arguments passed to the function "
        "and packs them into a tuple.  Keyword arguments are collected by `**kwargs` "
        "into a dictionary."
    ),
)

quiz_legb = QuizQuestion(
    id="legb_e",
    question="In the LEGB rule, what does 'E' stand for?",
    options=[
        "A) External",
        "B) Enclosing",
        "C) Environment",
        "D) Evaluated",
    ],
    correct="B",
    explanation=(
        "LEGB stands for Local, Enclosing, Global, Built-in.  The 'E' refers to "
        "the Enclosing function scope, which is relevant when you have nested functions."
    ),
)

quiz_closure = QuizQuestion(
    id="closure_def",
    question="What is a closure?",
    options=[
        "A) A function that closes files",
        "B) A nested function that captures variables from its enclosing scope",
        "C) A way to end a loop",
        "D) A class method",
    ],
    correct="B",
    explanation=(
        "A closure is a nested function that remembers and has access to variables "
        "from the enclosing function's scope, even after that outer function has "
        "finished executing."
    ),
)

quiz_lambda = QuizQuestion(
    id="lambda_syntax",
    question="Which is valid lambda syntax?",
    options=[
        "A) lambda: x + y",
        "B) lambda x, y: x + y",
        "C) def lambda(x): x",
        "D) lambda x, y -> x + y",
    ],
    correct="B",
    explanation=(
        "The correct syntax is `lambda parameters: expression`.  Option A has no "
        "parameters before the colon (it would create a no-argument lambda returning "
        "the name `x + y` from the enclosing scope).  Option C uses `def` with the "
        "reserved word `lambda`.  Option D uses `->` instead of `:`."
    ),
)

quiz_recursion = QuizQuestion(
    id="recursion_base",
    question="Every recursive function must have a ___.",
    options=[
        "A) Loop",
        "B) Global variable",
        "C) Base case",
        "D) Class",
    ],
    correct="C",
    explanation=(
        "A base case is the condition that stops the recursion.  Without it, the "
        "function would call itself infinitely, eventually causing a RecursionError "
        "when Python's maximum recursion depth is exceeded."
    ),
)

# ---------------------------------------------------------------------------
# Module Assembly
# ---------------------------------------------------------------------------

module = Module(
    id="04_functions",
    title="Functions",
    description=(
        "Define reusable code with functions: parameters, scope, "
        "closures, lambdas, and recursion"
    ),
    lessons=[
        defining_functions,
        parameters,
        scope,
        closures,
        lambdas,
        recursion,
    ],
    exercises=[
        greet_exercise,
        args_kwargs,
        scope_exercise,
        lambda_sort,
        factorial_exercise,
        decorator_intro,
    ],
    quiz=[
        quiz_return_none,
        quiz_args,
        quiz_legb,
        quiz_closure,
        quiz_lambda,
        quiz_recursion,
    ],
)
