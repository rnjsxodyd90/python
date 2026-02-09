"""Module 10: Interview Prep -- arrays, strings, linked lists, and common algorithms."""

from pylearn.curriculum.base import Module, Lesson, Exercise, QuizQuestion

# ---------------------------------------------------------------------------
# Lessons
# ---------------------------------------------------------------------------

_lesson_arrays_strings = Lesson(
    id="arrays_strings_overview",
    title="Arrays & Strings",
    content=(
        "Arrays (lists in Python) and strings are the most frequently tested\n"
        "data structures in coding interviews. Mastering a handful of core\n"
        "patterns will let you tackle the majority of problems you encounter.\n\n"
        "--- Two Pointers ---\n"
        "The two-pointer technique uses two indices that move toward each other\n"
        "(or in the same direction) through a sorted or structured sequence.\n"
        "Classic applications include finding pairs that sum to a target in a\n"
        "sorted array, removing duplicates in-place, and checking palindromes.\n"
        "The key insight is that by maintaining two pointers you can often\n"
        "reduce an O(n^2) brute-force search to O(n).\n\n"
        "--- Sliding Window ---\n"
        "The sliding window pattern maintains a contiguous subarray/substring\n"
        "bounded by two indices. You expand the window by advancing the right\n"
        "pointer and shrink it by advancing the left pointer. This is ideal\n"
        "for problems about subarrays of a fixed length, minimum-length\n"
        "subarrays with a given sum, or longest substrings without repeating\n"
        "characters. Sliding window typically runs in O(n) time.\n\n"
        "--- Hash Maps for O(1) Lookup ---\n"
        "Python dictionaries are hash maps under the hood, giving you average\n"
        "O(1) insertion and lookup. Whenever a problem asks you to 'find if\n"
        "something exists' or 'count occurrences', reach for a dict.\n"
        "collections.Counter is a specialized dict that counts hashable\n"
        "objects -- perfect for frequency-based problems like anagram\n"
        "detection or finding the most common element.\n\n"
        "--- Frequency Counting ---\n"
        "Many problems boil down to counting how often each element appears.\n"
        "Build a frequency map (dict or Counter), then scan it. Anagram\n"
        "checking, finding duplicates, and top-K-frequent-elements all use\n"
        "this pattern.\n\n"
        "--- Sort Then Scan ---\n"
        "Sometimes sorting the input first simplifies the problem dramatically.\n"
        "Finding duplicates, grouping anagrams, and merging intervals all\n"
        "become straightforward after a sort. Remember that sorting costs\n"
        "O(n log n), so this approach is only worthwhile when it removes a\n"
        "more expensive inner loop.\n\n"
        "--- Time and Space Complexity ---\n"
        "Interviewers almost always ask about complexity. Know the Big-O of\n"
        "your solution. Common targets:\n"
        "  - O(1) lookup: dict, set\n"
        "  - O(n) scan: single pass through a list\n"
        "  - O(n log n): sorting\n"
        "  - O(n^2): nested loops (usually the brute-force baseline)\n"
        "Space complexity matters too -- using a hash map trades O(n) space\n"
        "for faster time.\n\n"
        "--- Python Idioms for Interviews ---\n"
        "Interviewers expect you to write idiomatic Python:\n"
        "  - enumerate(iterable) gives (index, value) pairs.\n"
        "  - zip(a, b) iterates over two sequences in parallel.\n"
        "  - collections.Counter(iterable) builds a frequency dict.\n"
        "  - collections.defaultdict(list) avoids KeyError when grouping.\n"
        "  - Slicing (a[1:3], s[::-1]) is concise and fast.\n"
        "  - sorted() returns a new sorted list; list.sort() sorts in-place.\n"
        "  - set operations (union, intersection, difference) are O(n).\n"
        "Demonstrating fluency with these tools signals experience."
    ),
    code_example=(
        "# Two-pointer technique: find a pair in a SORTED list that sums to target\n"
        "def pair_sum_sorted(nums, target):\n"
        "    left, right = 0, len(nums) - 1\n"
        "    while left < right:\n"
        "        current = nums[left] + nums[right]\n"
        "        if current == target:\n"
        "            return [left, right]\n"
        "        elif current < target:\n"
        "            left += 1      # need a bigger sum\n"
        "        else:\n"
        "            right -= 1     # need a smaller sum\n"
        "    return []  # no pair found\n"
        "\n"
        "# Example usage\n"
        "numbers = [1, 3, 5, 7, 9, 11]\n"
        "print(pair_sum_sorted(numbers, 12))  # [2, 4] because 5 + 7 = 12\n"
        "\n"
        "# Frequency counting with Counter\n"
        "from collections import Counter\n"
        "words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']\n"
        "freq = Counter(words)\n"
        "print(freq.most_common(2))  # [('apple', 3), ('banana', 2)]\n"
    ),
    key_points=[
        "Two pointers reduce O(n^2) pair searches to O(n) on sorted data.",
        "Sliding window solves contiguous subarray/substring problems in O(n).",
        "Hash maps (dicts) give O(1) average lookup -- use them liberally.",
        "collections.Counter and defaultdict are interview power tools.",
        "Always state time and space complexity when presenting a solution.",
        "Sort-then-scan costs O(n log n) but often simplifies the logic.",
    ],
)

_lesson_linked_lists = Lesson(
    id="linked_lists_overview",
    title="Linked Lists",
    content=(
        "Linked lists are a staple of coding interviews even though Python\n"
        "does not have a built-in linked list type. Interviewers use them to\n"
        "test your understanding of pointers (references), dynamic memory,\n"
        "and in-place manipulation.\n\n"
        "--- Why Python Has No Built-in Linked List ---\n"
        "Python lists are dynamic arrays backed by contiguous memory, giving\n"
        "O(1) random access and amortized O(1) append. A linked list would\n"
        "sacrifice random access (O(n)) for O(1) insert/delete at arbitrary\n"
        "positions -- a trade-off that is rarely worthwhile for general-purpose\n"
        "code. However, in interviews the linked list is used to test pointer\n"
        "manipulation skills, so you must know how to implement one.\n\n"
        "--- The Node Class ---\n"
        "A singly linked list is built from Node objects. Each node holds a\n"
        "value and a reference (next) to the following node. The last node's\n"
        "next is None, signaling the end of the list. A 'head' variable\n"
        "points to the first node.\n\n"
        "--- Traversal ---\n"
        "To visit every node, start at head and follow next pointers until\n"
        "you reach None. This is the foundation for searching, printing,\n"
        "and counting.\n\n"
        "--- Fast and Slow Pointers ---\n"
        "This technique uses two pointers moving at different speeds:\n"
        "  - Cycle detection (Floyd's algorithm): Move 'slow' one step and\n"
        "    'fast' two steps. If they meet, there is a cycle.\n"
        "  - Finding the middle: When fast reaches the end, slow is at the\n"
        "    middle.\n"
        "  - Finding the kth node from the end: Start fast k steps ahead,\n"
        "    then advance both. When fast reaches the end, slow is at the\n"
        "    target node.\n\n"
        "--- Reversing a Linked List ---\n"
        "One of the most common interview questions. Use three pointers:\n"
        "prev (starts at None), current (starts at head), and next_node\n"
        "(temporarily saves current.next). At each step, reverse the link\n"
        "by setting current.next = prev, then advance all three pointers.\n\n"
        "--- Merging Two Sorted Lists ---\n"
        "Use a dummy head node and a tail pointer. Compare the heads of\n"
        "both lists, attach the smaller node to tail, and advance that\n"
        "list's pointer. When one list is exhausted, attach the remainder\n"
        "of the other list."
    ),
    code_example=(
        "# Node class for a singly linked list\n"
        "class Node:\n"
        "    def __init__(self, val=0, next=None):\n"
        "        self.val = val\n"
        "        self.next = next\n"
        "\n"
        "# Build a list: 1 -> 2 -> 3 -> None\n"
        "head = Node(1, Node(2, Node(3)))\n"
        "\n"
        "# Traversal: print all values\n"
        "current = head\n"
        "while current:\n"
        "    print(current.val, end=' -> ')\n"
        "    current = current.next\n"
        "print('None')\n"
        "# Output: 1 -> 2 -> 3 -> None\n"
        "\n"
        "# Reverse a linked list\n"
        "def reverse_list(head):\n"
        "    prev = None\n"
        "    current = head\n"
        "    while current:\n"
        "        next_node = current.next\n"
        "        current.next = prev\n"
        "        prev = current\n"
        "        current = next_node\n"
        "    return prev  # new head\n"
        "\n"
        "# After reversing: 3 -> 2 -> 1 -> None\n"
        "new_head = reverse_list(head)\n"
        "current = new_head\n"
        "while current:\n"
        "    print(current.val, end=' -> ')\n"
        "    current = current.next\n"
        "print('None')\n"
    ),
    key_points=[
        "A linked list is made of Node objects; each has a value and a next reference.",
        "Traversal: follow next pointers from head until None.",
        "Fast/slow pointers detect cycles, find the middle, and find the kth-from-end node.",
        "Reversing a linked list is one of the most common interview questions.",
        "Merging two sorted lists uses a dummy node and two-pointer comparison.",
        "Python has no built-in linked list because its list (dynamic array) is better for most tasks.",
    ],
)

_lesson_sorting_searching = Lesson(
    id="sorting_searching",
    title="Sorting & Searching",
    content=(
        "Sorting and searching are fundamental building blocks in algorithm\n"
        "design. Many interview problems become dramatically simpler once\n"
        "the data is sorted, and binary search is one of the most powerful\n"
        "tools in your toolkit.\n\n"
        "--- Python's Built-in Sort: Timsort ---\n"
        "Python's list.sort() (in-place) and sorted() (returns new list)\n"
        "both use Timsort, a hybrid of merge sort and insertion sort.\n"
        "Timsort runs in O(n log n) worst case and O(n) best case (when the\n"
        "data is already nearly sorted). It is stable, meaning equal elements\n"
        "retain their original relative order.\n\n"
        "You can customize sorting with the key parameter:\n"
        "  - sorted(words, key=len) sorts by string length.\n"
        "  - sorted(pairs, key=lambda x: x[1]) sorts by second element.\n"
        "  - sorted(words, key=str.lower) sorts case-insensitively.\n\n"
        "--- Binary Search ---\n"
        "Binary search finds a target in a SORTED sequence in O(log n) time\n"
        "by repeatedly halving the search space. The algorithm maintains two\n"
        "pointers (left, right) and compares the middle element to the\n"
        "target. If the middle is too small, search the right half; if too\n"
        "large, search the left half.\n\n"
        "Python's bisect module provides bisect_left() and bisect_right()\n"
        "for finding insertion points, and insort() for inserting while\n"
        "maintaining sort order. In interviews, you may be asked to\n"
        "implement binary search from scratch.\n\n"
        "--- When to Sort First ---\n"
        "Consider sorting when:\n"
        "  - You need to find duplicates (sort then check adjacent elements).\n"
        "  - You need to group items (sort by key, then scan).\n"
        "  - You need to merge intervals (sort by start time).\n"
        "  - You need to use two pointers on unsorted data.\n"
        "The O(n log n) sorting cost is worthwhile when it eliminates an\n"
        "O(n) inner loop, reducing O(n^2) to O(n log n).\n\n"
        "--- Common Patterns ---\n"
        "  - Merge sort for linked lists: linked lists lack random access,\n"
        "    so merge sort (which only needs sequential access) is preferred\n"
        "    over quicksort.\n"
        "  - Quick select for kth element: finds the kth smallest element in\n"
        "    O(n) average time without fully sorting. It partitions the array\n"
        "    like quicksort but only recurses into the partition containing\n"
        "    the kth element.\n"
        "  - Counting sort / bucket sort: when values are in a known small\n"
        "    range, you can sort in O(n) time.\n\n"
        "--- Complexity Cheat Sheet ---\n"
        "  Algorithm        | Time (avg)  | Time (worst) | Space  | Stable?\n"
        "  Timsort (Python) | O(n log n)  | O(n log n)   | O(n)   | Yes\n"
        "  Merge sort       | O(n log n)  | O(n log n)   | O(n)   | Yes\n"
        "  Quick sort       | O(n log n)  | O(n^2)       | O(log n)| No\n"
        "  Heap sort        | O(n log n)  | O(n log n)   | O(1)   | No\n"
        "  Binary search    | O(log n)    | O(log n)     | O(1)   | N/A"
    ),
    code_example=(
        "# Binary search implementation\n"
        "def binary_search(nums, target):\n"
        "    left, right = 0, len(nums) - 1\n"
        "    while left <= right:\n"
        "        mid = (left + right) // 2\n"
        "        if nums[mid] == target:\n"
        "            return mid\n"
        "        elif nums[mid] < target:\n"
        "            left = mid + 1\n"
        "        else:\n"
        "            right = mid - 1\n"
        "    return -1  # not found\n"
        "\n"
        "# Example usage\n"
        "data = [1, 3, 5, 7, 9, 11, 13]\n"
        "print(binary_search(data, 7))   # 3 (index of 7)\n"
        "print(binary_search(data, 4))   # -1 (not found)\n"
        "\n"
        "# Using Python's bisect module\n"
        "import bisect\n"
        "print(bisect.bisect_left(data, 7))   # 3\n"
        "print(bisect.bisect_left(data, 4))   # 2 (insertion point)\n"
        "\n"
        "# Sorting with a custom key\n"
        "words = ['banana', 'apple', 'cherry', 'date']\n"
        "print(sorted(words, key=len))  # ['date', 'apple', 'banana', 'cherry']\n"
    ),
    key_points=[
        "Python's built-in sort (Timsort) is O(n log n) and stable.",
        "Binary search runs in O(log n) but requires sorted data.",
        "The bisect module provides efficient binary search utilities.",
        "Sort first when it simplifies the remaining logic (duplicates, intervals, pairing).",
        "Quick select finds the kth element in O(n) average without full sorting.",
        "Always be ready to state the time and space complexity of your approach.",
    ],
)

# ---------------------------------------------------------------------------
# Exercises
# ---------------------------------------------------------------------------

_exercise_two_sum = Exercise(
    id="two_sum",
    title="Two Sum",
    description=(
        "Given a list of integers `nums` and an integer `target`, return the\n"
        "indices of the two numbers that add up to `target`.\n\n"
        "You may assume that each input has exactly one solution, and you may\n"
        "not use the same element twice. Return the indices as a list of two\n"
        "integers in ascending order.\n\n"
        "Write a function: def two_sum(nums, target) -> list"
    ),
    starter_code=(
        "def two_sum(nums, target):\n"
        "    # Your code here\n"
        "    pass\n"
    ),
    test_cases=[
        {"name": "Basic", "input_code": "print(two_sum([2, 7, 11, 15], 9))", "expected": "[0, 1]"},
        {"name": "Middle elements", "input_code": "print(two_sum([3, 2, 4], 6))", "expected": "[1, 2]"},
        {"name": "Same numbers", "input_code": "print(two_sum([3, 3], 6))", "expected": "[0, 1]"},
    ],
    hints=[
        "Use a dictionary to store seen values and their indices",
        "For each number, check if target - number exists in the dict",
    ],
    solution=(
        "def two_sum(nums, target):\n"
        "    seen = {}\n"
        "    for i, num in enumerate(nums):\n"
        "        complement = target - num\n"
        "        if complement in seen:\n"
        "            return [seen[complement], i]\n"
        "        seen[num] = i\n"
        "    return []"
    ),
    difficulty="easy",
)

_exercise_reverse_string = Exercise(
    id="reverse_string",
    title="Reverse String",
    description=(
        "Write a function `reverse_string(s)` that reverses a string without\n"
        "using Python's slice shortcut `[::-1]`.\n\n"
        "You should build the reversed string manually -- for example by\n"
        "iterating through characters and constructing a new string.\n\n"
        "Write a function: def reverse_string(s) -> str"
    ),
    starter_code=(
        "def reverse_string(s):\n"
        "    # Your code here (do NOT use s[::-1])\n"
        "    pass\n"
    ),
    test_cases=[
        {"name": "Basic", "input_code": "print(reverse_string('hello'))", "expected": "olleh"},
        {"name": "Empty", "input_code": "print(reverse_string(''))", "expected": ""},
        {"name": "Palindrome", "input_code": "print(reverse_string('racecar'))", "expected": "racecar"},
    ],
    hints=[
        "Try building the string character by character from the end",
        "Or use a list and join",
    ],
    solution=(
        "def reverse_string(s):\n"
        "    result = []\n"
        "    for char in s:\n"
        "        result.insert(0, char)\n"
        "    return ''.join(result)"
    ),
    difficulty="easy",
)

_exercise_valid_palindrome = Exercise(
    id="valid_palindrome",
    title="Valid Palindrome",
    description=(
        "Write a function `is_palindrome(s)` that checks whether a string is\n"
        "a palindrome, considering only alphanumeric characters and ignoring\n"
        "case.\n\n"
        "For example, 'A man, a plan, a canal: Panama' is a valid palindrome\n"
        "because after removing non-alphanumeric characters and lowering case\n"
        "it reads 'amanaplanacanalpanama', which is the same forwards and\n"
        "backwards.\n\n"
        "Write a function: def is_palindrome(s) -> bool"
    ),
    starter_code=(
        "def is_palindrome(s):\n"
        "    # Your code here\n"
        "    pass\n"
    ),
    test_cases=[
        {"name": "Basic palindrome", "input_code": "print(is_palindrome('A man, a plan, a canal: Panama'))", "expected": "True"},
        {"name": "Not palindrome", "input_code": "print(is_palindrome('race a car'))", "expected": "False"},
        {"name": "Empty string", "input_code": "print(is_palindrome(''))", "expected": "True"},
    ],
    hints=[
        "Filter out non-alphanumeric characters first",
        "Use .isalnum() and .lower()",
    ],
    solution=(
        "def is_palindrome(s):\n"
        "    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())\n"
        "    return cleaned == cleaned[::-1]"
    ),
    difficulty="easy",
)

_exercise_max_subarray = Exercise(
    id="max_subarray",
    title="Maximum Subarray",
    description=(
        "Write a function `max_subarray(nums)` that finds the contiguous\n"
        "subarray within a list of integers which has the largest sum, and\n"
        "returns that sum.\n\n"
        "Use Kadane's algorithm for an efficient O(n) solution:\n"
        "  - Track a running current_sum and a global max_sum.\n"
        "  - At each element, decide: is it better to extend the current\n"
        "    subarray or start fresh from this element?\n\n"
        "Write a function: def max_subarray(nums) -> int"
    ),
    starter_code=(
        "def max_subarray(nums):\n"
        "    # Your code here\n"
        "    pass\n"
    ),
    test_cases=[
        {"name": "Mixed", "input_code": "print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))", "expected": "6"},
        {"name": "All negative", "input_code": "print(max_subarray([-1, -2, -3]))", "expected": "-1"},
        {"name": "Single", "input_code": "print(max_subarray([5]))", "expected": "5"},
    ],
    hints=[
        "Track current_sum and max_sum",
        "Reset current_sum to current element if it drops below it",
    ],
    solution=(
        "def max_subarray(nums):\n"
        "    current_sum = max_sum = nums[0]\n"
        "    for num in nums[1:]:\n"
        "        current_sum = max(num, current_sum + num)\n"
        "        max_sum = max(max_sum, current_sum)\n"
        "    return max_sum"
    ),
    difficulty="medium",
)

_exercise_anagram_check = Exercise(
    id="anagram_check",
    title="Valid Anagram",
    description=(
        "Write a function `is_anagram(s, t)` that returns True if string `t`\n"
        "is an anagram of string `s`, and False otherwise.\n\n"
        "An anagram is a word formed by rearranging the letters of another\n"
        "word, using every letter exactly once. For example, 'anagram' and\n"
        "'nagaram' are anagrams.\n\n"
        "Write a function: def is_anagram(s, t) -> bool"
    ),
    starter_code=(
        "def is_anagram(s, t):\n"
        "    # Your code here\n"
        "    pass\n"
    ),
    test_cases=[
        {"name": "Anagram", "input_code": "print(is_anagram('anagram', 'nagaram'))", "expected": "True"},
        {"name": "Not anagram", "input_code": "print(is_anagram('rat', 'car'))", "expected": "False"},
        {"name": "Different lengths", "input_code": "print(is_anagram('ab', 'abc'))", "expected": "False"},
    ],
    hints=[
        "Compare character frequencies using a dict or Counter",
    ],
    solution=(
        "def is_anagram(s, t):\n"
        "    if len(s) != len(t):\n"
        "        return False\n"
        "    from collections import Counter\n"
        "    return Counter(s) == Counter(t)"
    ),
    difficulty="easy",
)

_exercise_merge_sorted = Exercise(
    id="merge_sorted",
    title="Merge Sorted Arrays",
    description=(
        "Write a function `merge_sorted(a, b)` that takes two sorted lists\n"
        "and merges them into a single sorted list.\n\n"
        "Do not simply concatenate and sort -- use the fact that both input\n"
        "lists are already sorted. Use two pointers, one for each list,\n"
        "and compare elements to build the result in O(n + m) time.\n\n"
        "Write a function: def merge_sorted(a, b) -> list"
    ),
    starter_code=(
        "def merge_sorted(a, b):\n"
        "    # Your code here\n"
        "    pass\n"
    ),
    test_cases=[
        {"name": "Basic", "input_code": "print(merge_sorted([1, 3, 5], [2, 4, 6]))", "expected": "[1, 2, 3, 4, 5, 6]"},
        {"name": "Empty", "input_code": "print(merge_sorted([], [1, 2]))", "expected": "[1, 2]"},
        {"name": "Overlapping", "input_code": "print(merge_sorted([1, 2, 3], [2, 3, 4]))", "expected": "[1, 2, 2, 3, 3, 4]"},
    ],
    hints=[
        "Use two pointers, one for each list",
        "Compare elements and append the smaller one",
    ],
    solution=(
        "def merge_sorted(a, b):\n"
        "    result = []\n"
        "    i = j = 0\n"
        "    while i < len(a) and j < len(b):\n"
        "        if a[i] <= b[j]:\n"
        "            result.append(a[i])\n"
        "            i += 1\n"
        "        else:\n"
        "            result.append(b[j])\n"
        "            j += 1\n"
        "    result.extend(a[i:])\n"
        "    result.extend(b[j:])\n"
        "    return result"
    ),
    difficulty="medium",
)

_exercise_fibonacci = Exercise(
    id="fibonacci",
    title="Fibonacci Sequence",
    description=(
        "Write a function `fib(n)` that returns the nth Fibonacci number\n"
        "using 0-based indexing: fib(0) = 0, fib(1) = 1, and for n >= 2,\n"
        "fib(n) = fib(n-1) + fib(n-2).\n\n"
        "Use an iterative approach for O(n) time and O(1) space. Avoid\n"
        "naive recursion, which would be O(2^n) without memoization.\n\n"
        "Write a function: def fib(n) -> int"
    ),
    starter_code=(
        "def fib(n):\n"
        "    # Your code here\n"
        "    pass\n"
    ),
    test_cases=[
        {"name": "fib(0)", "input_code": "print(fib(0))", "expected": "0"},
        {"name": "fib(1)", "input_code": "print(fib(1))", "expected": "1"},
        {"name": "fib(10)", "input_code": "print(fib(10))", "expected": "55"},
        {"name": "fib(20)", "input_code": "print(fib(20))", "expected": "6765"},
    ],
    hints=[
        "Iterative approach is O(n) time and O(1) space",
        "Use two variables to track previous two values",
    ],
    solution=(
        "def fib(n):\n"
        "    if n <= 1:\n"
        "        return n\n"
        "    a, b = 0, 1\n"
        "    for _ in range(2, n + 1):\n"
        "        a, b = b, a + b\n"
        "    return b"
    ),
    difficulty="easy",
)

_exercise_remove_duplicates = Exercise(
    id="remove_duplicates",
    title="Remove Duplicates",
    description=(
        "Write a function `remove_duplicates(nums)` that returns a new list\n"
        "with duplicate values removed, while preserving the original order\n"
        "of first appearances.\n\n"
        "For example, [1, 2, 2, 3, 4, 4, 5] becomes [1, 2, 3, 4, 5].\n\n"
        "Write a function: def remove_duplicates(nums) -> list"
    ),
    starter_code=(
        "def remove_duplicates(nums):\n"
        "    # Your code here\n"
        "    pass\n"
    ),
    test_cases=[
        {"name": "Basic", "input_code": "print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))", "expected": "[1, 2, 3, 4, 5]"},
        {"name": "All same", "input_code": "print(remove_duplicates([1, 1, 1]))", "expected": "[1]"},
        {"name": "No dupes", "input_code": "print(remove_duplicates([1, 2, 3]))", "expected": "[1, 2, 3]"},
    ],
    hints=[
        "Use a set to track seen values",
        "Iterate and add to result only if not seen",
    ],
    solution=(
        "def remove_duplicates(nums):\n"
        "    seen = set()\n"
        "    result = []\n"
        "    for num in nums:\n"
        "        if num not in seen:\n"
        "            seen.add(num)\n"
        "            result.append(num)\n"
        "    return result"
    ),
    difficulty="easy",
)

_exercise_binary_search = Exercise(
    id="binary_search_ex",
    title="Binary Search",
    description=(
        "Write a function `binary_search(nums, target)` that returns the\n"
        "index of `target` in the sorted list `nums`, or -1 if the target\n"
        "is not found.\n\n"
        "Implement the classic binary search algorithm:\n"
        "  1. Set left = 0, right = len(nums) - 1.\n"
        "  2. While left <= right, compute mid = (left + right) // 2.\n"
        "  3. If nums[mid] == target, return mid.\n"
        "  4. If nums[mid] < target, search the right half.\n"
        "  5. Otherwise, search the left half.\n\n"
        "Write a function: def binary_search(nums, target) -> int"
    ),
    starter_code=(
        "def binary_search(nums, target):\n"
        "    # Your code here\n"
        "    pass\n"
    ),
    test_cases=[
        {"name": "Found middle", "input_code": "print(binary_search([1, 3, 5, 7, 9], 5))", "expected": "2"},
        {"name": "Found first", "input_code": "print(binary_search([1, 3, 5, 7, 9], 1))", "expected": "0"},
        {"name": "Not found", "input_code": "print(binary_search([1, 3, 5, 7, 9], 4))", "expected": "-1"},
    ],
    hints=[
        "Use two pointers: left and right",
        "Calculate mid = (left + right) // 2",
    ],
    solution=(
        "def binary_search(nums, target):\n"
        "    left, right = 0, len(nums) - 1\n"
        "    while left <= right:\n"
        "        mid = (left + right) // 2\n"
        "        if nums[mid] == target:\n"
        "            return mid\n"
        "        elif nums[mid] < target:\n"
        "            left = mid + 1\n"
        "        else:\n"
        "            right = mid - 1\n"
        "    return -1"
    ),
    difficulty="medium",
)

_exercise_group_anagrams = Exercise(
    id="group_anagrams",
    title="Group Anagrams",
    description=(
        "Write a function `group_anagrams(strs)` that takes a list of strings\n"
        "and groups anagrams together.\n\n"
        "Two strings are anagrams if they contain the same characters in the\n"
        "same frequencies. For example, 'eat', 'tea', and 'ate' are all\n"
        "anagrams of each other.\n\n"
        "Return the groups as a list of lists. Each inner group should be\n"
        "sorted alphabetically, and the groups themselves should be sorted\n"
        "by their first element.\n\n"
        "Write a function: def group_anagrams(strs) -> list"
    ),
    starter_code=(
        "def group_anagrams(strs):\n"
        "    # Your code here\n"
        "    pass\n"
    ),
    test_cases=[
        {
            "name": "Basic",
            "input_code": (
                "result = group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])\n"
                "for g in result:\n"
                "    print(sorted(g))"
            ),
            "expected": "['ate', 'eat', 'tea']\n['bat']\n['nat', 'tan']",
        },
    ],
    hints=[
        "Use sorted(word) as a key to group anagrams",
        "A defaultdict(list) works well here",
    ],
    solution=(
        "def group_anagrams(strs):\n"
        "    from collections import defaultdict\n"
        "    groups = defaultdict(list)\n"
        "    for s in strs:\n"
        "        key = tuple(sorted(s))\n"
        "        groups[key].append(s)\n"
        "    result = [sorted(g) for g in groups.values()]\n"
        "    result.sort(key=lambda g: g[0])\n"
        "    return result"
    ),
    difficulty="hard",
)

# ---------------------------------------------------------------------------
# Quiz
# ---------------------------------------------------------------------------

_quiz = [
    QuizQuestion(
        id="q1_hash_lookup",
        question="What is the time complexity of hash table lookup?",
        options=[
            "A) O(n)",
            "B) O(log n)",
            "C) O(1) average",
            "D) O(n log n)",
        ],
        correct="C",
        explanation=(
            "Hash tables (Python dicts and sets) provide O(1) average-case "
            "lookup by computing a hash of the key to find its bucket directly. "
            "Worst case is O(n) due to hash collisions, but this is rare with "
            "a good hash function."
        ),
    ),
    QuizQuestion(
        id="q2_kadane",
        question="What algorithm finds the maximum subarray sum in O(n)?",
        options=[
            "A) Brute force",
            "B) Kadane's algorithm",
            "C) Binary search",
            "D) Merge sort",
        ],
        correct="B",
        explanation=(
            "Kadane's algorithm scans the array once, maintaining a running "
            "current_sum and a global max_sum. At each element it decides "
            "whether to extend the current subarray or start a new one. "
            "This runs in O(n) time and O(1) space."
        ),
    ),
    QuizQuestion(
        id="q3_two_pointers",
        question="The two pointers technique is most useful when:",
        options=[
            "A) Data is unsorted",
            "B) Data is sorted or searching for pairs",
            "C) Data is in a tree",
            "D) Data is random",
        ],
        correct="B",
        explanation=(
            "Two pointers work best on sorted sequences or when searching for "
            "pairs/triplets. With sorted data, you can intelligently move the "
            "pointers inward based on whether the current sum is too large or "
            "too small, achieving O(n) time."
        ),
    ),
    QuizQuestion(
        id="q4_python_sort",
        question="What is the time complexity of Python's built-in sort?",
        options=[
            "A) O(n)",
            "B) O(n log n)",
            "C) O(n^2)",
            "D) O(log n)",
        ],
        correct="B",
        explanation=(
            "Python uses Timsort, which is O(n log n) in the average and "
            "worst case. It is a hybrid of merge sort and insertion sort, "
            "optimized for real-world data that often contains partially "
            "sorted runs."
        ),
    ),
    QuizQuestion(
        id="q5_anagram_check",
        question=(
            "To check if two strings are anagrams, the most efficient "
            "approach is:"
        ),
        options=[
            "A) Sort both and compare",
            "B) Use character frequency counting",
            "C) Try all permutations",
            "D) Both A and B are efficient",
        ],
        correct="D",
        explanation=(
            "Sorting is O(n log n) and counting is O(n). Both are efficient "
            "compared to brute force (trying all permutations, which is O(n!)). "
            "In practice, frequency counting with a dict or Counter is slightly "
            "faster, but sorting is simpler to code and perfectly acceptable "
            "in an interview."
        ),
    ),
]

# ---------------------------------------------------------------------------
# Module definition
# ---------------------------------------------------------------------------

module = Module(
    id="10_interview_prep",
    title="Interview Prep",
    description=(
        "Practice coding interview problems: arrays, strings, linked lists, "
        "and common algorithms"
    ),
    lessons=[
        _lesson_arrays_strings,
        _lesson_linked_lists,
        _lesson_sorting_searching,
    ],
    exercises=[
        _exercise_two_sum,
        _exercise_reverse_string,
        _exercise_valid_palindrome,
        _exercise_max_subarray,
        _exercise_anagram_check,
        _exercise_merge_sorted,
        _exercise_fibonacci,
        _exercise_remove_duplicates,
        _exercise_binary_search,
        _exercise_group_anagrams,
    ],
    quiz=_quiz,
)
