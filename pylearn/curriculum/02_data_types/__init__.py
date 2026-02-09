"""Module 02 -- Data Types: Master Python's built-in data types."""

from pylearn.curriculum.base import Module, Lesson, Exercise, QuizQuestion

# ---------------------------------------------------------------------------
# Lessons
# ---------------------------------------------------------------------------

strings_lesson = Lesson(
    id="strings",
    title="Strings",
    content="""\
Strings are one of the most commonly used data types in Python. A string is an \
ordered, immutable sequence of characters used to represent text. You can create \
strings using single quotes ('hello'), double quotes ("hello"), or triple quotes \
('''hello''' or \"\"\"hello\"\"\") for multi-line text. Single and double quotes \
are interchangeable, so choose whichever avoids the need for escaping -- for \
example, "it's easy" or 'He said "hi"'.

Escape sequences let you embed special characters inside a string. The most \
common ones are \\n (newline), \\t (tab), \\\\ (literal backslash), and \\' or \
\\" (literal quotes). If you prefix a string with r (a raw string), backslashes \
are treated literally: r"C:\\Users\\name" keeps the backslashes as-is.

Python strings support indexing and slicing. Indexing starts at 0, and negative \
indices count from the end (-1 is the last character). Slicing uses the syntax \
string[start:stop:step] and returns a new string. Because strings are immutable, \
you cannot change an individual character in place; any transformation produces \
a brand-new string object.

Python provides a rich set of string methods. Some of the most useful include \
.upper() and .lower() for case conversion, .strip() to remove leading and \
trailing whitespace, .split() to break a string into a list of substrings, \
.join() to combine a list of strings into one, .replace(old, new) to substitute \
substrings, and .find(sub) which returns the index of a substring or -1 if not \
found. These methods never modify the original string; they always return a new \
one.

Modern Python offers two main ways to format strings. F-strings (formatted \
string literals), introduced in Python 3.6, embed expressions directly inside \
curly braces: f"Hello, {name}!". The older .format() method uses positional or \
named placeholders: "Hello, {0}!".format(name). F-strings are generally \
preferred for their readability and speed.""",
    code_example="""\
# Creating strings
greeting = "Hello, World!"
multiline = \"\"\"This is
a multi-line string.\"\"\"

# Indexing and slicing
print(greeting[0])        # H
print(greeting[-1])       # !
print(greeting[0:5])      # Hello
print(greeting[::2])      # Hlo ol!

# Useful string methods
text = "  Python Programming  "
print(text.strip())       # "Python Programming"
print(text.strip().upper())  # "PYTHON PROGRAMMING"
print(text.strip().split())  # ['Python', 'Programming']

# F-strings
name = "Alice"
age = 30
print(f"{name} is {age} years old.")  # Alice is 30 years old.

# String immutability -- this would raise TypeError:
# greeting[0] = 'h'""",
    key_points=[
        "Strings are immutable sequences of characters",
        "Use single, double, or triple quotes to create strings",
        "Indexing starts at 0; negative indices count from the end",
        "Slicing syntax: string[start:stop:step]",
        "String methods (.upper(), .lower(), .strip(), .split(), .replace()) return new strings",
        "F-strings (f\"...\") are the preferred way to format strings in modern Python",
    ],
)

numbers_lesson = Lesson(
    id="numbers",
    title="Numbers",
    content="""\
Python has three built-in numeric types: int, float, and complex. Integers \
(int) represent whole numbers of arbitrary precision -- Python will seamlessly \
handle numbers as large as your memory allows. Floats (float) represent \
floating-point numbers and follow IEEE 754 double-precision, giving you roughly \
15-17 significant decimal digits. Complex numbers (complex) have a real and \
imaginary part, written as 3+4j, and are useful in scientific computing.

Python supports the standard arithmetic operators: addition (+), subtraction \
(-), multiplication (*), and true division (/), which always returns a float. \
There are also three additional operators that come up constantly: floor \
division (//) returns the largest integer less than or equal to the result, the \
modulo operator (%) returns the remainder of division, and the exponentiation \
operator (**) raises a number to a power. Understanding the distinction between \
/ and // is especially important: 7 / 2 gives 3.5, while 7 // 2 gives 3.

Several built-in functions work with numbers. abs(x) returns the absolute value, \
round(x, n) rounds to n decimal places, and min() and max() return the smallest \
and largest of their arguments respectively. For more advanced mathematics, the \
math module in the standard library provides functions like math.sqrt(), \
math.ceil(), math.floor(), math.pi, and many more.

Type conversion between numeric types is straightforward. int() truncates a \
float toward zero (int(3.9) gives 3, int(-3.9) gives -3). float() converts an \
integer to a floating-point number. You can also convert numeric strings to \
numbers: int("42") and float("3.14") work as expected, but int("3.14") will \
raise a ValueError because the string is not a valid integer literal.""",
    code_example="""\
# Numeric types
x = 42          # int
y = 3.14        # float
z = 2 + 3j      # complex

# Arithmetic operators
print(10 + 3)    # 13   (addition)
print(10 - 3)    # 7    (subtraction)
print(10 * 3)    # 30   (multiplication)
print(10 / 3)    # 3.3333...  (true division)
print(10 // 3)   # 3    (floor division)
print(10 % 3)    # 1    (modulo / remainder)
print(2 ** 10)   # 1024 (exponentiation)

# Built-in functions
print(abs(-7))          # 7
print(round(3.14159, 2))  # 3.14
print(min(4, 2, 8, 1))   # 1
print(max(4, 2, 8, 1))   # 8

# Type conversion
print(int(3.9))     # 3
print(float(7))     # 7.0
print(int("42"))    # 42""",
    key_points=[
        "Python has three numeric types: int, float, and complex",
        "Integers have arbitrary precision -- no overflow",
        "/ always returns a float; // returns an integer (floor division)",
        "% gives the remainder; ** raises to a power",
        "abs(), round(), min(), max() are handy built-in functions",
        "int() truncates toward zero; float() adds a decimal point",
    ],
)

lists_lesson = Lesson(
    id="lists",
    title="Lists",
    content="""\
Lists are Python's most versatile and commonly used data structure. A list is an \
ordered, mutable collection that can hold items of any type, including other \
lists. You create a list with square brackets: [1, 2, 3] or with the list() \
constructor. Because lists are ordered, each element has a definite position, and \
you can access elements by index starting at 0. Negative indexing works just as \
it does with strings: -1 refers to the last element.

Slicing lets you extract sublists using the familiar [start:stop:step] syntax. \
Slicing always returns a new list, leaving the original unchanged. However, \
because lists are mutable, you can also assign to slices to replace, insert, or \
delete sections of a list in place: my_list[1:3] = [10, 20] replaces the second \
and third elements.

Lists come with a rich set of methods for modification. .append(x) adds a single \
item to the end. .extend(iterable) appends every element from another iterable. \
.insert(i, x) inserts an item at position i. For removal, .remove(x) deletes \
the first occurrence of x (raises ValueError if absent), and .pop(i) removes and \
returns the item at index i (defaults to the last item). .sort() sorts the list \
in place, while the built-in sorted() function returns a new sorted list. \
.reverse() reverses in place. .index(x) returns the first index of x, and \
.count(x) returns how many times x appears.

List comprehensions provide a concise, readable way to create new lists by \
transforming or filtering an existing iterable. The basic syntax is \
[expression for item in iterable] or [expression for item in iterable if \
condition]. For example, [x**2 for x in range(5)] produces [0, 1, 4, 9, 16]. \
Comprehensions are generally faster and more Pythonic than equivalent for-loops.

Lists can be nested to create matrices or other multi-dimensional structures. \
A 2D list is simply a list of lists: matrix = [[1, 2], [3, 4]]. You access \
elements with chained indexing: matrix[0][1] gives 2. Keep in mind that a \
shallow copy of a nested list still shares references to the inner lists; use \
copy.deepcopy() if you need fully independent copies.""",
    code_example="""\
# Creating and accessing lists
fruits = ["apple", "banana", "cherry", "date"]
print(fruits[0])       # apple
print(fruits[-1])      # date
print(fruits[1:3])     # ['banana', 'cherry']

# Mutability -- modifying in place
fruits[0] = "avocado"
print(fruits)          # ['avocado', 'banana', 'cherry', 'date']

# Common list methods
fruits.append("elderberry")
fruits.insert(1, "blueberry")
print(fruits)
# ['avocado', 'blueberry', 'banana', 'cherry', 'date', 'elderberry']

removed = fruits.pop()    # removes 'elderberry'
fruits.remove("banana")   # removes first occurrence
print(fruits)
# ['avocado', 'blueberry', 'cherry', 'date']

# Sorting
nums = [5, 2, 8, 1, 9]
nums.sort()
print(nums)            # [1, 2, 5, 8, 9]

# List comprehension
squares = [x ** 2 for x in range(6)]
print(squares)         # [0, 1, 4, 9, 16, 25]

evens = [x for x in range(10) if x % 2 == 0]
print(evens)           # [0, 2, 4, 6, 8]""",
    key_points=[
        "Lists are ordered, mutable collections created with [] or list()",
        "Indexing starts at 0; negative indices count from the end",
        "Key methods: append, extend, insert, remove, pop, sort, reverse",
        "List comprehensions: [expr for item in iterable if condition]",
        "Slicing returns a new list; assigning to a slice modifies in place",
        "Nested lists allow multi-dimensional structures",
    ],
)

tuples_lesson = Lesson(
    id="tuples",
    title="Tuples",
    content="""\
Tuples are ordered, immutable sequences in Python. They look similar to lists \
but use parentheses instead of square brackets: (1, 2, 3). In practice, it is \
actually the commas that make a tuple, not the parentheses -- the parentheses \
are just for clarity and grouping. This distinction matters most when creating a \
single-element tuple: (1) is just the integer 1 in parentheses, whereas (1,) \
with a trailing comma is a tuple containing one element.

Because tuples are immutable, you cannot add, remove, or change elements once \
the tuple is created. This immutability gives tuples a few advantages over lists: \
they are hashable (so they can be used as dictionary keys or set members), they \
are slightly faster, and they signal to the reader that the data should not \
change. If you need to "modify" a tuple, you create a new one, often by \
concatenating or slicing existing tuples.

Tuple packing and unpacking are powerful features. Packing creates a tuple from \
a comma-separated sequence of values: point = 3, 7 (parentheses optional). \
Unpacking assigns each element to a separate variable: x, y = point. You can \
even use the * operator to capture remaining elements: first, *rest = (1, 2, 3, \
4) gives first = 1 and rest = [2, 3, 4]. Unpacking is extremely common in Python \
-- it is used in for-loops over enumerate(), in function return values, and in \
swap idioms like a, b = b, a.

For more descriptive tuples, Python's collections module provides namedtuple, \
which lets you access fields by name: Point = namedtuple('Point', ['x', 'y']). \
This gives you the immutability and efficiency of tuples with the readability of \
attribute access.

When should you use a tuple instead of a list? Use tuples for fixed collections \
of heterogeneous data (like a coordinate pair or a database row), for dictionary \
keys, or whenever you want to guarantee that the sequence will not be modified. \
Use lists when you need a growable, changeable collection of similar items.""",
    code_example="""\
# Creating tuples
point = (3, 7)
rgb = (255, 128, 0)
single = (42,)            # single-element tuple -- note the comma
empty = ()

# Indexing and slicing (just like lists, but read-only)
print(point[0])            # 3
print(rgb[1:])             # (128, 0)

# Tuple packing and unpacking
coordinates = 10, 20       # packing (parentheses optional)
x, y = coordinates         # unpacking
print(f"x={x}, y={y}")    # x=10, y=20

# Extended unpacking with *
first, *middle, last = (1, 2, 3, 4, 5)
print(first)               # 1
print(middle)              # [2, 3, 4]
print(last)                # 5

# Swapping variables
a, b = 1, 2
a, b = b, a
print(a, b)                # 2 1

# Tuples as dict keys (because they are hashable)
locations = {(40.7, -74.0): "New York", (51.5, -0.1): "London"}
print(locations[(40.7, -74.0)])  # New York""",
    key_points=[
        "Tuples are ordered, immutable sequences -- created with () or just commas",
        "A single-element tuple requires a trailing comma: (1,)",
        "Tuple unpacking assigns elements to variables: x, y = (3, 7)",
        "Tuples are hashable and can serve as dictionary keys",
        "Use tuples for fixed, heterogeneous data; lists for growable collections",
        "namedtuple from collections adds named field access to tuples",
    ],
)

dictionaries_lesson = Lesson(
    id="dictionaries",
    title="Dictionaries",
    content="""\
Dictionaries are Python's built-in mapping type. They store data as key-value \
pairs and provide extremely fast lookup by key (average O(1)). You create a \
dictionary with curly braces: {"name": "Alice", "age": 30} or with the dict() \
constructor: dict(name="Alice", age=30). Keys must be hashable (strings, \
numbers, and tuples are common choices), and each key appears at most once. As \
of Python 3.7, dictionaries maintain insertion order.

There are two main ways to access a value. Using square brackets, d["key"], \
raises a KeyError if the key is missing. The safer alternative is the .get() \
method: d.get("key", default) returns the default value (None if unspecified) \
when the key does not exist. To add or update a key-value pair, simply assign \
to it: d["key"] = value. To remove a key, use del d["key"] or d.pop("key", \
default). The .pop() method also returns the removed value.

Dictionaries provide three view objects through their methods: .keys() returns \
a view of all keys, .values() returns a view of all values, and .items() returns \
a view of (key, value) tuples. These views are dynamic -- they reflect changes \
to the dictionary in real time. Iterating over a dictionary directly iterates \
over its keys: for k in d: is equivalent to for k in d.keys():.

Other useful methods include .update(other_dict) to merge another dictionary in, \
.setdefault(key, default) which returns the value if the key exists or inserts \
the default and returns it, and .clear() to remove all items. In Python 3.9+, \
you can also merge dictionaries with the | operator: merged = d1 | d2.

Dictionary comprehensions follow the same pattern as list comprehensions but \
produce dictionaries: {k: v for k, v in iterable}. For example, \
{x: x**2 for x in range(5)} creates {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}. \
Comprehensions are a concise way to transform, filter, or invert dictionaries.""",
    code_example="""\
# Creating dictionaries
person = {"name": "Alice", "age": 30, "city": "Paris"}
scores = dict(math=95, english=87, science=91)

# Accessing values
print(person["name"])          # Alice
print(person.get("email", "N/A"))  # N/A (key missing, returns default)

# Adding, updating, deleting
person["email"] = "alice@example.com"   # add
person["age"] = 31                       # update
del person["city"]                       # delete
print(person)
# {'name': 'Alice', 'age': 31, 'email': 'alice@example.com'}

# Iterating over keys, values, items
for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary comprehension
squares = {x: x ** 2 for x in range(6)}
print(squares)   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Counting pattern
sentence = "apple banana apple cherry banana apple"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)  # {'apple': 3, 'banana': 2, 'cherry': 1}""",
    key_points=[
        "Dictionaries map hashable keys to values with O(1) average lookup",
        "Use d.get(key, default) to avoid KeyError on missing keys",
        "d.keys(), d.values(), d.items() return dynamic view objects",
        "Assign to d[key] to add or update; use del or .pop() to remove",
        "Dict comprehensions: {k: v for k, v in iterable if condition}",
        "Since Python 3.7, dictionaries maintain insertion order",
    ],
)

sets_lesson = Lesson(
    id="sets",
    title="Sets",
    content="""\
Sets are unordered collections of unique elements. They are Python's direct \
implementation of the mathematical concept of a set and are optimized for \
membership testing, deduplication, and set-theoretic operations. You create a \
set with curly braces: {1, 2, 3} or with the set() constructor. Note that {} \
creates an empty dictionary, not an empty set -- use set() for an empty set.

Because sets enforce uniqueness, adding a duplicate element has no effect. This \
makes sets ideal for removing duplicates from a sequence: list(set([1, 2, 2, 3])) \
produces [1, 2, 3] (though order is not guaranteed). Elements of a set must be \
hashable, which means you can have sets of numbers, strings, and tuples, but not \
sets of lists or dictionaries.

The real power of sets lies in their operations. Union (a | b or a.union(b)) \
returns all elements from both sets. Intersection (a & b or a.intersection(b)) \
returns only elements present in both. Difference (a - b or a.difference(b)) \
returns elements in a but not in b. Symmetric difference (a ^ b or \
a.symmetric_difference(b)) returns elements in either set but not both. Each of \
these operations returns a new set, leaving the originals unchanged. There are \
also in-place variants like .update(), .intersection_update(), etc.

Common set methods include .add(x) to insert an element, .remove(x) to delete \
an element (raises KeyError if missing), .discard(x) to delete without raising \
an error, .pop() to remove and return an arbitrary element, and .clear() to \
empty the set. You can also check subset and superset relationships with <= and \
>= or the .issubset() and .issuperset() methods.

A frozenset is an immutable version of a set. Once created, you cannot add or \
remove elements. Frozensets are hashable, which means they can be used as \
dictionary keys or as elements of other sets. Create one with frozenset([1, 2, 3]).

Use sets when you need fast membership testing (x in my_set is O(1) on average), \
when you need to eliminate duplicates, or when you need to perform mathematical \
set operations on your data.""",
    code_example="""\
# Creating sets
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
empty = set()               # NOT {} -- that's an empty dict

# Set operations
print(a | b)                # Union: {1, 2, 3, 4, 5, 6, 7, 8}
print(a & b)                # Intersection: {4, 5}
print(a - b)                # Difference: {1, 2, 3}
print(a ^ b)                # Symmetric difference: {1, 2, 3, 6, 7, 8}

# Removing duplicates from a list
nums = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(nums))
print(sorted(unique))       # [1, 2, 3, 4]

# Membership testing (very fast)
print(3 in a)               # True
print(9 in a)               # False

# Modifying sets
a.add(6)
a.discard(1)                # safe remove -- no error if missing
print(a)                    # {2, 3, 4, 5, 6}

# Frozenset -- immutable set
fs = frozenset([1, 2, 3])
# fs.add(4)  # AttributeError: frozenset has no 'add' method""",
    key_points=[
        "Sets are unordered collections of unique, hashable elements",
        "Use set() for an empty set -- {} creates an empty dict",
        "Union (|), intersection (&), difference (-), symmetric difference (^)",
        "Membership testing (in) is O(1) on average",
        "frozenset is an immutable, hashable version of set",
        "Sets are perfect for deduplication and set-theoretic operations",
    ],
)

type_conversion_lesson = Lesson(
    id="type_conversion",
    title="Type Conversion",
    content="""\
Type conversion (also called type casting) is the process of converting a value \
from one data type to another. Python distinguishes between implicit conversion, \
which happens automatically, and explicit conversion, which you perform manually \
with built-in functions.

Implicit conversion occurs when Python automatically promotes a value to a \
compatible type during an operation. For example, when you add an integer and a \
float (3 + 2.5), Python converts the integer to a float before performing the \
addition, producing 5.5. This is also called type coercion. Implicit conversion \
is safe because it always moves to a wider type without losing information. \
However, Python does not implicitly convert between unrelated types: "3" + 5 \
raises a TypeError rather than silently guessing your intent.

Explicit conversion uses built-in constructor functions. int(x) converts to \
integer -- it truncates floats (int(3.9) gives 3) and parses numeric strings \
(int("42") gives 42). float(x) converts to float. str(x) converts any object \
to its string representation. bool(x) converts to boolean. list(), tuple(), \
set(), and dict() convert between collection types. For instance, \
list("hello") produces ['h', 'e', 'l', 'l', 'o'], and dict([(1, 'a'), (2, 'b')]) \
produces {1: 'a', 2: 'b'}.

Understanding truthy and falsy values is essential for effective Python \
programming. When Python evaluates a value in a boolean context (such as an if \
statement or bool() call), the following are considered falsy: None, False, zero \
of any numeric type (0, 0.0, 0j), and empty sequences or collections ('', [], \
(), {}, set(), frozenset()). Everything else is truthy. This is why you can \
write idiomatic checks like if my_list: to test whether a list is non-empty.

The type() function returns the type of an object: type(42) returns <class 'int'>. \
The isinstance() function checks whether an object is an instance of a particular \
type or tuple of types: isinstance(42, int) returns True, and isinstance(42, \
(int, float)) also returns True. Prefer isinstance() over type() comparisons \
because it respects inheritance.""",
    code_example="""\
# Implicit conversion
result = 3 + 2.5          # int + float -> float
print(result)              # 5.5
print(type(result))        # <class 'float'>

# Explicit conversion
x = int("42")             # str -> int
y = float(7)              # int -> float
z = str(3.14)             # float -> str
print(x, y, z)            # 42 7.0 3.14

# Collection conversions
print(list("hello"))       # ['h', 'e', 'l', 'l', 'o']
print(tuple([1, 2, 3]))   # (1, 2, 3)
print(set([1, 2, 2, 3]))  # {1, 2, 3}

# Truthy and falsy values
print(bool(0))             # False
print(bool(""))            # False
print(bool([]))            # False
print(bool(None))          # False
print(bool(42))            # True
print(bool("hello"))       # True
print(bool([1, 2]))        # True

# type() and isinstance()
print(type(42))               # <class 'int'>
print(isinstance(42, int))    # True
print(isinstance(42, (int, float)))  # True""",
    key_points=[
        "Implicit conversion: Python auto-promotes int to float in mixed arithmetic",
        "Explicit conversion: int(), float(), str(), bool(), list(), tuple(), set()",
        "int() truncates floats toward zero; int('3.14') raises ValueError",
        "Falsy values: None, False, 0, 0.0, '', [], (), {}, set()",
        "type(x) returns the type; isinstance(x, T) checks type with inheritance",
        "Prefer isinstance() over type() == for type checking",
    ],
)

# ---------------------------------------------------------------------------
# Exercises
# ---------------------------------------------------------------------------

string_exercise = Exercise(
    id="string_exercise",
    title="String Manipulation",
    description="""\
Given the following string:

    text = "  Hello, Python World!  "

Strip the leading and trailing whitespace, convert the result to uppercase, \
and print it.""",
    starter_code='text = "  Hello, Python World!  "\n# Strip whitespace and convert to uppercase, then print\n',
    expected_output="HELLO, PYTHON WORLD!",
    hints=["Use .strip() then .upper()"],
    solution='text = "  Hello, Python World!  "\nprint(text.strip().upper())',
    difficulty="easy",
)

numbers_exercise = Exercise(
    id="numbers_exercise",
    title="Calculator",
    description="""\
Calculate and print the results of the following three operations, each on \
its own line:

1. 17 // 3  (integer division)
2. 17 % 3   (remainder)
3. 2 ** 10  (power)""",
    starter_code="# Print the result of each operation on a separate line\n",
    expected_output="5\n2\n1024",
    hints=[
        "// is the floor (integer) division operator",
        "% gives the remainder",
        "** is the exponentiation operator",
    ],
    solution="print(17 // 3)\nprint(17 % 3)\nprint(2 ** 10)",
    difficulty="easy",
)

list_exercise = Exercise(
    id="list_exercise",
    title="List Operations",
    description="""\
Start with the following list:

    nums = [3, 1, 4, 1, 5, 9, 2, 6]

Remove duplicates (by converting to a set and back to a list), sort the \
result, and print the sorted unique list.""",
    starter_code="nums = [3, 1, 4, 1, 5, 9, 2, 6]\n# Remove duplicates, sort, and print\n",
    expected_output="[1, 2, 3, 4, 5, 6, 9]",
    hints=[
        "Convert to set to remove duplicates, then back to list",
        "Use sorted() to sort",
    ],
    solution="nums = [3, 1, 4, 1, 5, 9, 2, 6]\nresult = sorted(set(nums))\nprint(result)",
    difficulty="medium",
)

tuple_exercise = Exercise(
    id="tuple_exercise",
    title="Tuple Unpacking",
    description="""\
Create a tuple named `point` with the values (3, 7). Unpack it into two \
variables `x` and `y`, then print them using an f-string in the format:

    x=3, y=7""",
    starter_code="# Create tuple, unpack, and print\n",
    expected_output="x=3, y=7",
    hints=[
        "Create the tuple: point = (3, 7)",
        "Unpack with: x, y = point",
        'Use an f-string: f"x={x}, y={y}"',
    ],
    solution='point = (3, 7)\nx, y = point\nprint(f"x={x}, y={y}")',
    difficulty="easy",
)


def _validate_dict(namespace, stdout):
    """Validator for the word-counter exercise."""
    expected = {'cat': 2, 'mat': 1, 'on': 1, 'sat': 1, 'the': 3}
    output = stdout.strip()
    try:
        result = eval(output)
        if result == expected:
            return True, "Word count is correct!"
        return False, f"Expected {expected}, got {result}"
    except Exception:
        return False, f"Could not parse output. Expected dict like {expected}"


dict_exercise = Exercise(
    id="dict_exercise",
    title="Word Counter",
    description="""\
Count the occurrences of each word in the following sentence:

    "the cat sat on the mat the cat"

Build a dictionary mapping each word to its count, then print the dictionary \
sorted by keys. The expected output is a dict like:

    {'cat': 2, 'mat': 1, 'on': 1, 'sat': 1, 'the': 3}""",
    starter_code='sentence = "the cat sat on the mat the cat"\n# Count words and print sorted dict\n',
    validator=_validate_dict,
    hints=[
        "Split the string into words first",
        "Use a dict to count, or try collections.Counter",
        "dict(sorted(d.items())) sorts a dict by keys",
    ],
    solution=(
        'sentence = "the cat sat on the mat the cat"\n'
        "words = sentence.split()\n"
        "counts = {}\n"
        "for word in words:\n"
        "    counts[word] = counts.get(word, 0) + 1\n"
        "print(dict(sorted(counts.items())))"
    ),
    difficulty="medium",
)


def _validate_sets(namespace, stdout):
    """Validator for the set-operations exercise."""
    lines = stdout.strip().split('\n')
    if len(lines) != 3:
        return False, f"Expected 3 lines of output, got {len(lines)}"
    try:
        union = eval(lines[0])
        inter = eval(lines[1])
        diff = eval(lines[2])
        if union == {1, 2, 3, 4, 5, 6, 7, 8} and inter == {4, 5} and diff == {1, 2, 3}:
            return True, "All set operations correct!"
        return False, "One or more set operations incorrect"
    except Exception:
        return False, "Could not parse output as sets"


set_exercise = Exercise(
    id="set_exercise",
    title="Set Operations",
    description="""\
Given the following two sets:

    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}

Print three results, each on its own line:
1. The union of a and b
2. The intersection of a and b
3. The difference a - b""",
    starter_code="a = {1, 2, 3, 4, 5}\nb = {4, 5, 6, 7, 8}\n# Print union, intersection, difference\n",
    expected_output="{1, 2, 3, 4, 5, 6, 7, 8}\n{4, 5}\n{1, 2, 3}",
    validator=_validate_sets,
    hints=[
        "Union: a | b or a.union(b)",
        "Intersection: a & b or a.intersection(b)",
        "Difference: a - b or a.difference(b)",
    ],
    solution="a = {1, 2, 3, 4, 5}\nb = {4, 5, 6, 7, 8}\nprint(a | b)\nprint(a & b)\nprint(a - b)",
    difficulty="easy",
)

conversion_exercise = Exercise(
    id="conversion_exercise",
    title="Type Juggling",
    description="""\
Convert the string "42" to an integer, add 8 to it, and print the result.""",
    starter_code='text = "42"\n# Convert to int, add 8, and print\n',
    expected_output="50",
    hints=["Use int() to convert strings to integers"],
    solution='text = "42"\nresult = int(text) + 8\nprint(result)',
    difficulty="easy",
)

# ---------------------------------------------------------------------------
# Quiz Questions
# ---------------------------------------------------------------------------

quiz = [
    QuizQuestion(
        id="q1_strip",
        question="Which method removes whitespace from both ends of a string?",
        options=[
            "A) trim()",
            "B) strip()",
            "C) clean()",
            "D) remove()",
        ],
        correct="B",
        explanation=(
            "The .strip() method returns a copy of the string with leading and "
            "trailing whitespace removed. Python does not have a .trim() method "
            "(that name is used in other languages like JavaScript)."
        ),
    ),
    QuizQuestion(
        id="q2_floor_div",
        question="What is the result of 7 // 2?",
        options=[
            "A) 3.5",
            "B) 3",
            "C) 4",
            "D) 3.0",
        ],
        correct="B",
        explanation=(
            "// is the floor (integer) division operator. It divides and then "
            "rounds down to the nearest integer. 7 // 2 equals 3, not 3.5."
        ),
    ),
    QuizQuestion(
        id="q3_mutable",
        question="Which of the following data types is mutable?",
        options=[
            "A) str",
            "B) tuple",
            "C) list",
            "D) frozenset",
        ],
        correct="C",
        explanation=(
            "Lists are mutable -- you can add, remove, and change elements in "
            "place. Strings, tuples, and frozensets are all immutable."
        ),
    ),
    QuizQuestion(
        id="q4_single_tuple",
        question="How do you create a single-element tuple?",
        options=[
            "A) (1)",
            "B) (1,)",
            "C) tuple(1)",
            "D) [1]",
        ],
        correct="B",
        explanation=(
            "(1) is just the integer 1 wrapped in parentheses for grouping. "
            "The trailing comma in (1,) is what actually makes it a tuple. "
            "tuple(1) raises a TypeError because int is not iterable."
        ),
    ),
    QuizQuestion(
        id="q5_dict_get",
        question="What does dict.get(key, default) return when the key is missing?",
        options=[
            "A) Raises KeyError",
            "B) Returns None",
            "C) Returns default",
            "D) Adds the key with default value",
        ],
        correct="C",
        explanation=(
            "The .get() method returns the specified default value when the key "
            "is not found. If no default is provided, it returns None. Unlike "
            "bracket access (d[key]), it never raises a KeyError."
        ),
    ),
    QuizQuestion(
        id="q6_set_diff",
        question="Which set operation returns elements in A but not in B?",
        options=[
            "A) A | B",
            "B) A & B",
            "C) A - B",
            "D) A ^ B",
        ],
        correct="C",
        explanation=(
            "A - B (set difference) returns a new set with elements that are in "
            "A but not in B. | is union, & is intersection, and ^ is symmetric "
            "difference (elements in either but not both)."
        ),
    ),
    QuizQuestion(
        id="q7_bool_empty",
        question="What is bool([])?",
        options=[
            "A) True",
            "B) False",
            "C) None",
            "D) Error",
        ],
        correct="B",
        explanation=(
            "Empty sequences and collections are falsy in Python. An empty list "
            "[], empty string '', empty tuple (), empty dict {}, and empty set() "
            "all evaluate to False in a boolean context."
        ),
    ),
]

# ---------------------------------------------------------------------------
# Module assembly
# ---------------------------------------------------------------------------

module = Module(
    id="02_data_types",
    title="Data Types",
    description=(
        "Master Python's built-in data types: strings, numbers, lists, "
        "tuples, dictionaries, and sets"
    ),
    lessons=[
        strings_lesson,
        numbers_lesson,
        lists_lesson,
        tuples_lesson,
        dictionaries_lesson,
        sets_lesson,
        type_conversion_lesson,
    ],
    exercises=[
        string_exercise,
        numbers_exercise,
        list_exercise,
        tuple_exercise,
        dict_exercise,
        set_exercise,
        conversion_exercise,
    ],
    quiz=quiz,
)
