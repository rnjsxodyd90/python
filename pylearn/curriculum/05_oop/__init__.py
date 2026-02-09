"""Module 05: Object-Oriented Programming -- classes, inheritance, polymorphism, and design patterns."""

from pylearn.curriculum.base import Module, Lesson, Exercise, QuizQuestion

# ---------------------------------------------------------------------------
# Lessons
# ---------------------------------------------------------------------------

_lesson_classes_objects = Lesson(
    id="classes_objects",
    title="Classes & Objects",
    content=(
        "Object-Oriented Programming (OOP) is a paradigm that organizes code around\n"
        "objects -- bundles of data (attributes) and behavior (methods) that model\n"
        "real-world or conceptual entities. In Python, everything is already an\n"
        "object: integers, strings, lists, and even functions. When you call\n"
        "type(42), Python tells you it is an instance of the class 'int'. OOP lets\n"
        "you define your own classes so you can create objects that are tailor-made\n"
        "for your problem domain.\n\n"
        "A class is defined with the `class` keyword followed by a name (using\n"
        "CamelCase by convention) and a colon. Think of a class as a blueprint or\n"
        "template. It describes what data an object will hold and what operations it\n"
        "can perform, but it is not an object itself -- just the instructions for\n"
        "making one. To actually create an object (an 'instance'), you call the\n"
        "class like a function: `my_dog = Dog('Rex', 'Labrador')`.\n\n"
        "The special method `__init__` is called automatically every time you create\n"
        "a new instance. It is the initializer (often loosely called the\n"
        "constructor). Its first parameter is always `self`, which is a reference to\n"
        "the instance being created. Inside `__init__` you attach attributes to\n"
        "`self` so that each instance carries its own data. For example,\n"
        "`self.name = name` stores the name argument as an instance attribute.\n\n"
        "Methods are functions defined inside a class body. Just like `__init__`,\n"
        "regular methods receive `self` as their first parameter so they can read\n"
        "and modify the instance's attributes. You call them with dot notation:\n"
        "`my_dog.bark()`. Python silently passes the object before the dot as\n"
        "`self`, so you never supply it explicitly when calling a method.\n\n"
        "Each instance has its own independent set of attributes. If you create two\n"
        "Dog objects with different names, each one remembers its own name. This is\n"
        "what makes objects so powerful: they encapsulate state and behavior into a\n"
        "single, self-contained unit that you can pass around your program."
    ),
    code_example=(
        "class Dog:\n"
        "    \"\"\"A simple Dog class to demonstrate OOP basics.\"\"\"\n"
        "\n"
        "    def __init__(self, name, breed):\n"
        "        self.name = name      # instance attribute\n"
        "        self.breed = breed    # instance attribute\n"
        "\n"
        "    def bark(self):\n"
        "        return f\"{self.name} says Woof!\"\n"
        "\n"
        "\n"
        "# Creating instances (objects)\n"
        "rex = Dog(\"Rex\", \"Labrador\")\n"
        "bella = Dog(\"Bella\", \"Poodle\")\n"
        "\n"
        "print(rex.bark())     # Rex says Woof!\n"
        "print(bella.bark())   # Bella says Woof!\n"
        "print(rex.breed)      # Labrador\n"
    ),
    key_points=[
        "A class is a blueprint; an object (instance) is a concrete realization.",
        "__init__ is called automatically when you create a new instance.",
        "'self' refers to the current instance -- always the first parameter of methods.",
        "Instance attributes are attached to 'self' and are unique to each object.",
        "Methods are called with dot notation: object.method().",
    ],
)

_lesson_class_static_methods = Lesson(
    id="class_static_methods",
    title="Class & Static Methods",
    content=(
        "Regular methods operate on an instance and receive `self` as their first\n"
        "parameter. But sometimes you need a method that works with the class\n"
        "itself, or a utility function that logically belongs to the class but\n"
        "does not need access to instance or class state at all. Python provides\n"
        "two decorators for these situations: @classmethod and @staticmethod.\n\n"
        "A class method is defined by placing the @classmethod decorator above the\n"
        "method definition. Instead of `self`, it receives `cls` -- a reference to\n"
        "the class itself -- as its first parameter. This makes class methods ideal\n"
        "for factory methods: alternative constructors that create instances in\n"
        "different ways. For example, a Date class might have a `from_string`\n"
        "classmethod that parses a date string like '2024-01-15' and returns a new\n"
        "Date instance. Because the method receives `cls`, it correctly creates\n"
        "instances of subclasses too, making it more flexible than calling the\n"
        "class name directly.\n\n"
        "A static method is defined with the @staticmethod decorator. It receives\n"
        "neither `self` nor `cls` -- it is essentially a plain function that lives\n"
        "inside the class namespace. Static methods are used for utility functions\n"
        "that have a logical connection to the class but do not need to read or\n"
        "modify any class or instance data. For example, a Math class might have a\n"
        "static method `is_even(n)` that simply returns whether a number is even.\n\n"
        "When should you use which? Use a regular method when you need to access or\n"
        "modify instance state. Use a @classmethod when you need to access or\n"
        "modify class-level state or when you are writing a factory method. Use a\n"
        "@staticmethod when the method is a utility that logically belongs to the\n"
        "class but does not need `self` or `cls`. If in doubt, start with a\n"
        "regular method; you can always refactor later.\n\n"
        "Class methods are also commonly used to track or manage class-level data.\n"
        "For instance, you might keep a count of all instances created, or maintain\n"
        "a registry of subclasses. Because `cls` points to whatever class the\n"
        "method is called on, class methods cooperate naturally with inheritance."
    ),
    code_example=(
        "class Date:\n"
        "    \"\"\"A simple Date class demonstrating class and static methods.\"\"\"\n"
        "\n"
        "    def __init__(self, year, month, day):\n"
        "        self.year = year\n"
        "        self.month = month\n"
        "        self.day = day\n"
        "\n"
        "    @classmethod\n"
        "    def from_string(cls, date_string):\n"
        "        \"\"\"Factory method: create a Date from 'YYYY-MM-DD' string.\"\"\"\n"
        "        year, month, day = map(int, date_string.split('-'))\n"
        "        return cls(year, month, day)\n"
        "\n"
        "    @staticmethod\n"
        "    def is_valid_date(date_string):\n"
        "        \"\"\"Utility: check if a string looks like a date.\"\"\"\n"
        "        parts = date_string.split('-')\n"
        "        return len(parts) == 3 and all(p.isdigit() for p in parts)\n"
        "\n"
        "    def __str__(self):\n"
        "        return f\"{self.year:04d}-{self.month:02d}-{self.day:02d}\"\n"
        "\n"
        "\n"
        "# Using the factory classmethod\n"
        "d = Date.from_string('2024-01-15')\n"
        "print(d)  # 2024-01-15\n"
        "\n"
        "# Using the static method\n"
        "print(Date.is_valid_date('2024-01-15'))  # True\n"
        "print(Date.is_valid_date('not-a-date'))  # False\n"
    ),
    key_points=[
        "@classmethod receives `cls` (the class) as its first parameter.",
        "@staticmethod receives neither `self` nor `cls` -- it is a plain function in the class namespace.",
        "Factory methods (alternative constructors) are the classic use case for @classmethod.",
        "Static methods are for utilities logically related to the class.",
        "Class methods work correctly with inheritance because `cls` refers to the actual subclass.",
    ],
)

_lesson_properties = Lesson(
    id="properties",
    title="Properties",
    content=(
        "In many languages, class attributes are accessed through explicit getter\n"
        "and setter methods: `obj.get_x()` and `obj.set_x(value)`. Python takes a\n"
        "different approach. The @property decorator lets you define methods that\n"
        "look like simple attribute access on the outside. You write `obj.x`\n"
        "instead of `obj.get_x()`, and behind the scenes Python calls your method.\n"
        "This gives you the clean syntax of attribute access with the power of\n"
        "method calls.\n\n"
        "To create a property, define a method with the @property decorator. This\n"
        "becomes the getter -- it is called whenever someone reads the attribute.\n"
        "To allow setting the attribute, define another method with the same name\n"
        "using the @name.setter decorator. This setter method receives the new\n"
        "value as a parameter and can validate or transform it before storing.\n\n"
        "Properties are especially useful for validation. For example, a\n"
        "Temperature class might store the value internally in Celsius but expose\n"
        "a `fahrenheit` property that converts on the fly. The setter can reject\n"
        "invalid values (like temperatures below absolute zero) by raising a\n"
        "ValueError, while the getter handles the conversion math transparently.\n\n"
        "Computed attributes are another excellent use case. Instead of storing\n"
        "redundant data, you compute it on demand. A Rectangle class might store\n"
        "only width and height, but provide an `area` property that returns\n"
        "`self.width * self.height`. The caller does not know or care whether the\n"
        "value is stored or computed -- it just works.\n\n"
        "A major benefit of properties is that you can start with simple public\n"
        "attributes and add validation or computation later without changing the\n"
        "external interface. Code that uses `obj.x = 5` continues to work even\n"
        "after you turn `x` into a property with a setter. This is why Pythonistas\n"
        "do not write getters and setters by default -- they add properties only\n"
        "when they actually need the extra logic."
    ),
    code_example=(
        "class Temperature:\n"
        "    \"\"\"Temperature class with property-based conversion.\"\"\"\n"
        "\n"
        "    def __init__(self, celsius=0):\n"
        "        self.celsius = celsius  # uses the setter below\n"
        "\n"
        "    @property\n"
        "    def celsius(self):\n"
        "        return self._celsius\n"
        "\n"
        "    @celsius.setter\n"
        "    def celsius(self, value):\n"
        "        if value < -273.15:\n"
        "            raise ValueError(\"Temperature below absolute zero!\")\n"
        "        self._celsius = value\n"
        "\n"
        "    @property\n"
        "    def fahrenheit(self):\n"
        "        return self._celsius * 9 / 5 + 32\n"
        "\n"
        "    @fahrenheit.setter\n"
        "    def fahrenheit(self, value):\n"
        "        self.celsius = (value - 32) * 5 / 9\n"
        "\n"
        "\n"
        "t = Temperature(100)\n"
        "print(t.fahrenheit)   # 212.0\n"
        "t.fahrenheit = 32\n"
        "print(t.celsius)      # 0.0\n"
    ),
    key_points=[
        "@property turns a method into a read-only attribute.",
        "@name.setter defines the setter for a property.",
        "Properties enable validation, conversion, and computed attributes.",
        "Start with plain attributes; add properties when you need extra logic.",
        "The external interface stays the same whether you use attributes or properties.",
    ],
)

_lesson_inheritance = Lesson(
    id="inheritance",
    title="Inheritance",
    content=(
        "Inheritance is a mechanism that lets one class (the child or subclass)\n"
        "acquire the attributes and methods of another class (the parent or\n"
        "superclass). The child class can then extend or override the inherited\n"
        "behavior. You specify the parent class in parentheses after the class\n"
        "name: `class Dog(Animal):`. The Dog class now has everything Animal has,\n"
        "plus whatever you add or change in its own body.\n\n"
        "The `super()` function is the bridge between parent and child. When a\n"
        "child class overrides `__init__`, it typically needs to call\n"
        "`super().__init__(...)` to ensure the parent's initialization runs as\n"
        "well. Without this call, the parent's attributes will not be set up,\n"
        "leading to AttributeError at runtime. `super()` also works with any\n"
        "method, not just `__init__` -- call `super().method_name()` to invoke\n"
        "the parent's version of a method.\n\n"
        "Method overriding happens when a child class defines a method with the\n"
        "same name as one in the parent. Python always uses the most specific\n"
        "version -- the one defined on the actual class of the object. If Dog\n"
        "defines `speak()` and Animal also defines `speak()`, calling `speak()`\n"
        "on a Dog instance runs Dog's version. This is fundamental to polymorphism,\n"
        "which we will explore in a later lesson.\n\n"
        "Python provides two built-in functions for checking class relationships:\n"
        "`isinstance(obj, ClassName)` returns True if obj is an instance of\n"
        "ClassName or any of its subclasses. `issubclass(ChildClass, ParentClass)`\n"
        "checks if one class is a subclass of another. These are useful for\n"
        "runtime type checking, though Pythonic code tends to rely on duck typing\n"
        "instead.\n\n"
        "Inheritance models an 'is-a' relationship: a Dog IS an Animal. If the\n"
        "relationship does not make semantic sense (a Car is NOT an Engine), then\n"
        "inheritance is the wrong tool and you should consider composition instead.\n"
        "Use inheritance when the child genuinely specializes the parent, and\n"
        "when you want substitutability -- the ability to use a child object\n"
        "anywhere a parent is expected."
    ),
    code_example=(
        "class Animal:\n"
        "    \"\"\"Base class for all animals.\"\"\"\n"
        "\n"
        "    def __init__(self, name):\n"
        "        self.name = name\n"
        "\n"
        "    def speak(self):\n"
        "        return f\"{self.name} makes a sound\"\n"
        "\n"
        "\n"
        "class Dog(Animal):\n"
        "    def __init__(self, name, breed):\n"
        "        super().__init__(name)   # call parent's __init__\n"
        "        self.breed = breed\n"
        "\n"
        "    def speak(self):             # override parent method\n"
        "        return f\"{self.name} says Woof!\"\n"
        "\n"
        "\n"
        "class Cat(Animal):\n"
        "    def speak(self):\n"
        "        return f\"{self.name} says Meow!\"\n"
        "\n"
        "\n"
        "animals = [Dog(\"Rex\", \"Labrador\"), Cat(\"Whiskers\")]\n"
        "for animal in animals:\n"
        "    print(animal.speak())\n"
        "# Rex says Woof!\n"
        "# Whiskers says Meow!\n"
        "\n"
        "print(isinstance(animals[0], Animal))  # True\n"
        "print(issubclass(Dog, Animal))          # True\n"
    ),
    key_points=[
        "Child classes inherit all attributes and methods from the parent.",
        "Use super().__init__(...) to call the parent's initializer.",
        "Method overriding lets a child provide its own version of a parent method.",
        "isinstance() and issubclass() check runtime type relationships.",
        "Inheritance models 'is-a' relationships -- use it when substitutability makes sense.",
    ],
)

_lesson_multiple_inheritance = Lesson(
    id="multiple_inheritance",
    title="Multiple Inheritance & MRO",
    content=(
        "Python supports multiple inheritance, meaning a class can inherit from\n"
        "more than one parent: `class Child(Parent1, Parent2):`. This is more\n"
        "powerful than single inheritance but introduces complexity, particularly\n"
        "the 'diamond problem'. The diamond problem arises when two parent classes\n"
        "share a common ancestor and the child inherits from both. Which version\n"
        "of a method should the child use?\n\n"
        "Python solves this with the Method Resolution Order (MRO), which uses\n"
        "an algorithm called C3 linearization. The MRO defines a strict, linear\n"
        "ordering of classes that Python follows when searching for a method. You\n"
        "can inspect it with `ClassName.__mro__` or `ClassName.mro()`. The order\n"
        "is: the class itself first, then its parents left-to-right, then their\n"
        "parents, and so on, with the guarantee that a class always appears before\n"
        "its parents and the left-to-right order of bases is preserved.\n\n"
        "When `super()` is called inside a method, it does not simply go to the\n"
        "parent class -- it goes to the next class in the MRO chain. This is\n"
        "crucial for cooperative multiple inheritance to work. Each class in the\n"
        "chain calls `super()`, passing control up the MRO until the chain is\n"
        "complete. For this to work, all classes should use `super()` consistently\n"
        "and accept **kwargs so they can pass along unexpected arguments.\n\n"
        "In practice, the most common use of multiple inheritance in Python is\n"
        "the mixin pattern. A mixin is a small class that provides a specific\n"
        "piece of functionality meant to be 'mixed in' with other classes. For\n"
        "example, a LogMixin might add logging methods, or a SerializeMixin might\n"
        "add JSON serialization. Mixins typically do not have `__init__` methods\n"
        "or their own state -- they just provide behavior.\n\n"
        "While multiple inheritance is powerful, it can make code harder to\n"
        "understand if overused. Many experienced Python developers prefer\n"
        "composition or single inheritance with mixins. If you find yourself\n"
        "building deep, tangled hierarchies with multiple parents, step back and\n"
        "consider whether composition would be clearer."
    ),
    code_example=(
        "class LogMixin:\n"
        "    \"\"\"Mixin that adds logging capability.\"\"\"\n"
        "\n"
        "    def log(self, message):\n"
        "        print(f\"[{self.__class__.__name__}] {message}\")\n"
        "\n"
        "\n"
        "class Connection:\n"
        "    def __init__(self, host):\n"
        "        self.host = host\n"
        "\n"
        "    def connect(self):\n"
        "        return f\"Connected to {self.host}\"\n"
        "\n"
        "\n"
        "class LoggedConnection(LogMixin, Connection):\n"
        "    \"\"\"Connection with built-in logging.\"\"\"\n"
        "\n"
        "    def connect(self):\n"
        "        result = super().connect()\n"
        "        self.log(result)  # method from LogMixin\n"
        "        return result\n"
        "\n"
        "\n"
        "conn = LoggedConnection(\"example.com\")\n"
        "conn.connect()\n"
        "# [LoggedConnection] Connected to example.com\n"
        "\n"
        "# Inspect the MRO\n"
        "print(LoggedConnection.__mro__)\n"
        "# (LoggedConnection, LogMixin, Connection, object)\n"
    ),
    key_points=[
        "Python supports multiple inheritance: class Child(Parent1, Parent2).",
        "The MRO (Method Resolution Order) determines method lookup order.",
        "C3 linearization ensures a consistent, predictable MRO.",
        "Mixins are small, focused classes designed to be combined with others.",
        "Prefer composition or single inheritance with mixins over deep multi-inheritance trees.",
    ],
)

_lesson_composition = Lesson(
    id="composition",
    title="Composition vs Inheritance",
    content=(
        "Composition and inheritance are two fundamental ways to build complex\n"
        "objects from simpler ones. Inheritance models an 'is-a' relationship\n"
        "(a Dog IS an Animal), while composition models a 'has-a' relationship\n"
        "(a Car HAS an Engine). Both are useful, but composition is often the\n"
        "better choice, especially when the relationship between objects does not\n"
        "naturally fit an 'is-a' hierarchy.\n\n"
        "With composition, you create classes that contain instances of other\n"
        "classes as attributes. The outer class delegates work to the inner\n"
        "objects. For example, instead of making Car a subclass of Engine, you\n"
        "give Car an `engine` attribute that holds an Engine instance. If you\n"
        "need to start the car, you call `self.engine.start()`. This is called\n"
        "delegation.\n\n"
        "Composition provides several advantages over inheritance. First, it is\n"
        "more flexible: you can swap out components at runtime. Want a different\n"
        "engine? Just assign a new Engine object. With inheritance, you are locked\n"
        "into the parent's implementation at class definition time. Second,\n"
        "composition avoids the fragile base class problem, where changes to a\n"
        "parent class can break child classes in unexpected ways. Third, composition\n"
        "makes it easier to follow the Single Responsibility Principle -- each\n"
        "class does one thing well.\n\n"
        "Dependency injection is a pattern closely related to composition. Instead\n"
        "of a class creating its own dependencies internally, the dependencies are\n"
        "'injected' from outside -- usually through the constructor. This makes\n"
        "classes easier to test (you can inject mock objects) and more flexible\n"
        "(you can inject different implementations).\n\n"
        "A practical rule of thumb: use inheritance when the child truly IS a\n"
        "specialized version of the parent and you want polymorphic behavior. Use\n"
        "composition for everything else. 'Favor composition over inheritance' is\n"
        "one of the most widely repeated design principles in software engineering,\n"
        "and for good reason."
    ),
    code_example=(
        "class Engine:\n"
        "    \"\"\"An engine component.\"\"\"\n"
        "\n"
        "    def __init__(self, horsepower):\n"
        "        self.horsepower = horsepower\n"
        "        self.running = False\n"
        "\n"
        "    def start(self):\n"
        "        self.running = True\n"
        "        return f\"Engine ({self.horsepower}hp) started\"\n"
        "\n"
        "    def stop(self):\n"
        "        self.running = False\n"
        "        return \"Engine stopped\"\n"
        "\n"
        "\n"
        "class Car:\n"
        "    \"\"\"A car that HAS an engine (composition, not inheritance).\"\"\"\n"
        "\n"
        "    def __init__(self, model, engine):\n"
        "        self.model = model\n"
        "        self.engine = engine  # composition: Car HAS an Engine\n"
        "\n"
        "    def start(self):\n"
        "        return f\"{self.model}: {self.engine.start()}\"\n"
        "\n"
        "\n"
        "# Dependency injection: we pass the engine in from outside\n"
        "v8 = Engine(450)\n"
        "mustang = Car(\"Mustang\", v8)\n"
        "print(mustang.start())  # Mustang: Engine (450hp) started\n"
        "\n"
        "# Easy to swap components\n"
        "electric = Engine(300)\n"
        "tesla = Car(\"Model S\", electric)\n"
        "print(tesla.start())   # Model S: Engine (300hp) started\n"
    ),
    key_points=[
        "Inheritance = 'is-a'; Composition = 'has-a'.",
        "Composition stores other objects as attributes and delegates to them.",
        "Composition is more flexible: components can be swapped at runtime.",
        "Dependency injection passes dependencies in from outside (usually via __init__).",
        "'Favor composition over inheritance' -- use inheritance only for true specialization.",
    ],
)

_lesson_encapsulation = Lesson(
    id="encapsulation",
    title="Encapsulation",
    content=(
        "Encapsulation is the principle of bundling data and the methods that\n"
        "operate on that data into a single unit (a class) and restricting direct\n"
        "access to some of the object's internals. The goal is to protect the\n"
        "object's internal state from being modified in unexpected ways and to\n"
        "present a clean, stable interface to the outside world.\n\n"
        "Python does not have strict access modifiers like Java's private or\n"
        "protected keywords. Instead, it relies on naming conventions. A single\n"
        "leading underscore (_attribute) signals that the attribute is 'protected'\n"
        "-- it is an internal implementation detail, and external code should not\n"
        "access it directly. Python does not enforce this; it is a gentleman's\n"
        "agreement between developers. The underscore tells other programmers:\n"
        "'This is not part of the public API. Use at your own risk.'\n\n"
        "A double leading underscore (__attribute) triggers name mangling. Python\n"
        "renames the attribute to `_ClassName__attribute` to make accidental access\n"
        "from subclasses or external code harder. Note that this is not true\n"
        "privacy -- determined code can still access it via the mangled name. Name\n"
        "mangling exists primarily to prevent accidental name collisions in\n"
        "inheritance hierarchies, not to enforce security.\n\n"
        "The Pythonic approach to encapsulation is to start with public attributes\n"
        "and add properties when you need control. If you need to validate data\n"
        "on assignment, use a property setter. If you need to compute a value on\n"
        "access, use a property getter. The external interface (attribute access\n"
        "with dot notation) stays the same either way. This is a key advantage of\n"
        "Python's property mechanism.\n\n"
        "Information hiding does not mean hiding everything -- it means exposing a\n"
        "clear, intentional interface and keeping implementation details internal.\n"
        "If an attribute is part of your class's public contract, keep it public.\n"
        "If it is an internal detail that could change, prefix it with an\n"
        "underscore. Use double underscores sparingly and intentionally."
    ),
    code_example=(
        "class BankAccount:\n"
        "    \"\"\"Bank account demonstrating encapsulation conventions.\"\"\"\n"
        "\n"
        "    def __init__(self, owner, balance=0):\n"
        "        self.owner = owner         # public attribute\n"
        "        self.__balance = balance    # name-mangled (private by convention)\n"
        "\n"
        "    def deposit(self, amount):\n"
        "        if amount > 0:\n"
        "            self.__balance += amount\n"
        "            return True\n"
        "        return False\n"
        "\n"
        "    def withdraw(self, amount):\n"
        "        if 0 < amount <= self.__balance:\n"
        "            self.__balance -= amount\n"
        "            return True\n"
        "        return False\n"
        "\n"
        "    def get_balance(self):\n"
        "        return self.__balance\n"
        "\n"
        "\n"
        "acct = BankAccount(\"Alice\", 100)\n"
        "acct.deposit(50)\n"
        "print(acct.get_balance())  # 150\n"
        "\n"
        "# Name mangling in action:\n"
        "# acct.__balance          -> AttributeError\n"
        "# acct._BankAccount__balance -> 150 (accessible but discouraged)\n"
    ),
    key_points=[
        "Encapsulation bundles data and behavior and restricts internal access.",
        "Single underscore (_attr) = 'protected' by convention (not enforced).",
        "Double underscore (__attr) triggers name mangling to _ClassName__attr.",
        "Name mangling prevents accidental collisions, not true security.",
        "Start public; add properties when you need validation or computation.",
    ],
)

_lesson_polymorphism = Lesson(
    id="polymorphism",
    title="Polymorphism & Duck Typing",
    content=(
        "Polymorphism means 'many forms'. In OOP, it refers to the ability of\n"
        "different objects to respond to the same method call in their own way.\n"
        "If you call `shape.area()` on a Circle, you get the circle's area; on a\n"
        "Rectangle, you get the rectangle's area. The calling code does not need\n"
        "to know which specific type it is dealing with -- it just calls `area()`\n"
        "and trusts each object to do the right thing.\n\n"
        "Python embraces a philosophy called 'duck typing': 'If it walks like a\n"
        "duck and quacks like a duck, then it IS a duck.' This means Python does\n"
        "not check the type of an object before calling a method. It simply tries\n"
        "to call the method. If the object has it, great. If not, you get an\n"
        "AttributeError. This is fundamentally different from languages like Java\n"
        "that require objects to implement a formal interface before they can be\n"
        "used polymorphically.\n\n"
        "Duck typing is closely related to two Python philosophies. EAFP (Easier\n"
        "to Ask Forgiveness than Permission) says you should try an operation and\n"
        "handle the exception if it fails, rather than checking in advance whether\n"
        "it will work. LBYL (Look Before You Leap) is the opposite: check first,\n"
        "then act. Python generally favors EAFP. Instead of `if hasattr(obj,\n"
        "'area'):`, you call `obj.area()` inside a try/except block.\n\n"
        "Structural subtyping (formalized by PEP 544 with typing.Protocol) brings\n"
        "duck typing into the type-checking world. A Protocol defines a set of\n"
        "methods that a class must have, but the class does not need to explicitly\n"
        "inherit from the Protocol. If it has the right methods, it matches. This\n"
        "bridges the gap between static type checking and Python's dynamic nature.\n\n"
        "When should you use isinstance() versus duck typing? Use isinstance()\n"
        "when you truly need to branch on type (e.g., serialization code that\n"
        "handles different types differently). In most other cases, prefer duck\n"
        "typing -- it is more Pythonic, more flexible, and makes your code easier\n"
        "to extend with new types."
    ),
    code_example=(
        "import math\n"
        "\n"
        "\n"
        "class Circle:\n"
        "    def __init__(self, radius):\n"
        "        self.radius = radius\n"
        "\n"
        "    def area(self):\n"
        "        return math.pi * self.radius ** 2\n"
        "\n"
        "\n"
        "class Rectangle:\n"
        "    def __init__(self, width, height):\n"
        "        self.width = width\n"
        "        self.height = height\n"
        "\n"
        "    def area(self):\n"
        "        return self.width * self.height\n"
        "\n"
        "\n"
        "class Triangle:\n"
        "    def __init__(self, base, height):\n"
        "        self.base = base\n"
        "        self.height = height\n"
        "\n"
        "    def area(self):\n"
        "        return 0.5 * self.base * self.height\n"
        "\n"
        "\n"
        "# Polymorphism: same interface, different behavior\n"
        "shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]\n"
        "\n"
        "for shape in shapes:\n"
        "    # Duck typing: we don't check the type, we just call area()\n"
        "    print(f\"{type(shape).__name__}: {shape.area():.2f}\")\n"
        "# Circle: 78.54\n"
        "# Rectangle: 24.00\n"
        "# Triangle: 12.00\n"
    ),
    key_points=[
        "Polymorphism lets different objects respond to the same method in their own way.",
        "Duck typing: if it has the right methods, it qualifies -- no formal interface needed.",
        "EAFP (try/except) is preferred over LBYL (check first) in Python.",
        "typing.Protocol formalizes duck typing for static type checkers.",
        "Use isinstance() sparingly; prefer duck typing for flexibility.",
    ],
)

_lesson_abstract_classes = Lesson(
    id="abstract_classes",
    title="Abstract Base Classes",
    content=(
        "Sometimes you want to define a base class that establishes a contract:\n"
        "it declares methods that all subclasses MUST implement, but it does not\n"
        "provide implementations itself. This is an abstract base class (ABC). In\n"
        "Python, you create ABCs using the `abc` module, specifically by inheriting\n"
        "from `abc.ABC` and decorating methods with `@abc.abstractmethod`.\n\n"
        "The key rule is: you cannot instantiate an abstract class. If you try,\n"
        "Python raises a TypeError. You can only instantiate concrete subclasses\n"
        "that provide implementations for ALL abstract methods. If a subclass\n"
        "forgets to implement even one abstract method, it too becomes abstract\n"
        "and cannot be instantiated. This is Python's way of enforcing an\n"
        "interface contract at runtime.\n\n"
        "ABCs can contain both abstract and concrete methods. The abstract methods\n"
        "define the contract (what subclasses must implement), while concrete\n"
        "methods provide shared behavior that all subclasses inherit. You can also\n"
        "have abstract properties using @property combined with @abstractmethod.\n\n"
        "The Python standard library uses ABCs extensively. The `collections.abc`\n"
        "module defines ABCs like Iterable, Iterator, Sequence, Mapping, and\n"
        "MutableMapping. These formalize what it means to be 'iterable' or\n"
        "'sequence-like'. You can use them with isinstance() to check if an object\n"
        "supports certain operations, or inherit from them to get default method\n"
        "implementations for free.\n\n"
        "When should you use ABCs? They are ideal when you have a family of related\n"
        "classes that must all support a specific set of operations. A plugin system\n"
        "is a classic example: you define an abstract Plugin class with methods like\n"
        "`activate()` and `deactivate()`, and every plugin must implement them.\n"
        "ABCs give you the safety of enforced interfaces while still allowing the\n"
        "flexibility of Python's dynamic nature."
    ),
    code_example=(
        "from abc import ABC, abstractmethod\n"
        "import math\n"
        "\n"
        "\n"
        "class Shape(ABC):\n"
        "    \"\"\"Abstract base class for shapes.\"\"\"\n"
        "\n"
        "    @abstractmethod\n"
        "    def area(self):\n"
        "        \"\"\"Calculate and return the area.\"\"\"\n"
        "        pass\n"
        "\n"
        "    @abstractmethod\n"
        "    def perimeter(self):\n"
        "        \"\"\"Calculate and return the perimeter.\"\"\"\n"
        "        pass\n"
        "\n"
        "    def describe(self):\n"
        "        \"\"\"Concrete method shared by all shapes.\"\"\"\n"
        "        return f\"{type(self).__name__}: area={self.area():.2f}\"\n"
        "\n"
        "\n"
        "class Circle(Shape):\n"
        "    def __init__(self, radius):\n"
        "        self.radius = radius\n"
        "\n"
        "    def area(self):\n"
        "        return math.pi * self.radius ** 2\n"
        "\n"
        "    def perimeter(self):\n"
        "        return 2 * math.pi * self.radius\n"
        "\n"
        "\n"
        "class Rectangle(Shape):\n"
        "    def __init__(self, width, height):\n"
        "        self.width = width\n"
        "        self.height = height\n"
        "\n"
        "    def area(self):\n"
        "        return self.width * self.height\n"
        "\n"
        "    def perimeter(self):\n"
        "        return 2 * (self.width + self.height)\n"
        "\n"
        "\n"
        "# Shape() would raise TypeError -- cannot instantiate abstract class\n"
        "c = Circle(5)\n"
        "r = Rectangle(4, 6)\n"
        "print(c.describe())  # Circle: area=78.54\n"
        "print(r.describe())  # Rectangle: area=24.00\n"
    ),
    key_points=[
        "ABCs inherit from abc.ABC and use @abstractmethod to define contracts.",
        "You cannot instantiate a class that has unimplemented abstract methods.",
        "ABCs can mix abstract methods (must implement) with concrete methods (shared).",
        "collections.abc provides standard ABCs like Iterable, Sequence, Mapping.",
        "Use ABCs when you need to enforce a common interface across related classes.",
    ],
)

_lesson_dunder_methods = Lesson(
    id="dunder_methods",
    title="Dunder Methods",
    content=(
        "Dunder methods (short for 'double underscore' methods, also called magic\n"
        "methods or special methods) are methods with names surrounded by double\n"
        "underscores, like __init__, __str__, and __add__. They let your objects\n"
        "integrate with Python's built-in syntax and protocols. When you write\n"
        "`a + b`, Python actually calls `a.__add__(b)`. When you write `str(obj)`,\n"
        "Python calls `obj.__str__()`. By defining these methods, you make your\n"
        "custom objects behave like built-in types.\n\n"
        "Two of the most commonly overridden dunder methods are __str__ and\n"
        "__repr__. __str__ defines the 'informal', human-readable string\n"
        "representation, used by print() and str(). __repr__ defines the\n"
        "'official' representation, ideally one that could recreate the object.\n"
        "If you only implement one, implement __repr__ -- Python falls back to it\n"
        "when __str__ is not defined.\n\n"
        "Comparison methods let you use ==, <, >, etc. with your objects. __eq__\n"
        "handles ==, __lt__ handles <, __le__ handles <=, and so on. A useful\n"
        "shortcut is the @functools.total_ordering decorator: define __eq__ and\n"
        "one ordering method (__lt__), and it auto-generates the rest.\n\n"
        "Arithmetic operators are handled by __add__ (+), __sub__ (-), __mul__ (*),\n"
        "__truediv__ (/), and others. Container behavior is controlled by __len__\n"
        "(for len()), __getitem__ (for indexing with []), __setitem__ (for\n"
        "assignment with []=), and __contains__ (for the 'in' operator).\n\n"
        "There are also __iter__ and __next__ (making an object iterable),\n"
        "__call__ (making an object callable like a function), __enter__ and\n"
        "__exit__ (context managers for 'with' statements), and __hash__ (making\n"
        "objects usable as dictionary keys). The Python data model is rich and\n"
        "consistent -- mastering dunder methods is key to writing truly Pythonic\n"
        "classes."
    ),
    code_example=(
        "class Vector:\n"
        "    \"\"\"A 2D vector with operator overloading.\"\"\"\n"
        "\n"
        "    def __init__(self, x, y):\n"
        "        self.x = x\n"
        "        self.y = y\n"
        "\n"
        "    def __repr__(self):\n"
        "        return f\"Vector({self.x}, {self.y})\"\n"
        "\n"
        "    def __str__(self):\n"
        "        return f\"Vector({self.x}, {self.y})\"\n"
        "\n"
        "    def __eq__(self, other):\n"
        "        return self.x == other.x and self.y == other.y\n"
        "\n"
        "    def __add__(self, other):\n"
        "        return Vector(self.x + other.x, self.y + other.y)\n"
        "\n"
        "    def __abs__(self):\n"
        "        return (self.x ** 2 + self.y ** 2) ** 0.5\n"
        "\n"
        "    def __len__(self):\n"
        "        return 2  # A 2D vector always has 2 components\n"
        "\n"
        "\n"
        "v1 = Vector(3, 4)\n"
        "v2 = Vector(1, 2)\n"
        "print(v1 + v2)           # Vector(4, 6)\n"
        "print(v1 == Vector(3, 4))  # True\n"
        "print(abs(v1))           # 5.0\n"
    ),
    key_points=[
        "__str__ = human-readable string; __repr__ = official/debug representation.",
        "__eq__, __lt__, etc. enable comparison operators (==, <, <=, ...).",
        "__add__, __sub__, __mul__ enable arithmetic operators (+, -, *).",
        "__len__, __getitem__, __contains__ make objects behave like containers.",
        "Dunder methods let custom objects integrate seamlessly with Python syntax.",
    ],
)

_lesson_dataclasses = Lesson(
    id="dataclasses_lesson",
    title="Dataclasses",
    content=(
        "Many classes exist primarily to hold data. They have an __init__ that\n"
        "stores parameters as attributes, a __repr__ for debugging, and maybe\n"
        "__eq__ for comparison. Writing all this boilerplate gets tedious fast.\n"
        "The @dataclass decorator (from the dataclasses module, available since\n"
        "Python 3.7) auto-generates these methods for you based on class-level\n"
        "type annotations.\n\n"
        "To use it, decorate a class with @dataclass and annotate each field with\n"
        "a type hint. Python generates __init__, __repr__, and __eq__ for you\n"
        "automatically. You can provide default values for fields using simple\n"
        "assignment or the field() function for more advanced defaults. For mutable\n"
        "defaults (like lists or dicts), you MUST use `field(default_factory=list)`\n"
        "instead of `field(default=[])` -- the latter would share a single list\n"
        "between all instances (a classic Python gotcha).\n\n"
        "The __post_init__ method is called after the auto-generated __init__\n"
        "completes. It is useful for validation, computing derived attributes, or\n"
        "any initialization logic that goes beyond simple assignment. For example,\n"
        "you might validate that an age field is non-negative.\n\n"
        "Frozen dataclasses are created with @dataclass(frozen=True). They are\n"
        "immutable: any attempt to set an attribute after creation raises a\n"
        "FrozenInstanceError. Frozen dataclasses are also hashable by default,\n"
        "making them usable as dictionary keys or set elements. This is ideal for\n"
        "value objects like coordinates or configuration records.\n\n"
        "The @dataclass decorator accepts several options: `order=True` generates\n"
        "comparison methods (__lt__, __le__, __gt__, __ge__) based on field order.\n"
        "`frozen=True` makes instances immutable. `slots=True` (Python 3.10+) uses\n"
        "__slots__ for memory efficiency. Dataclasses strike an excellent balance\n"
        "between the simplicity of tuples/dicts and the structure of full classes."
    ),
    code_example=(
        "from dataclasses import dataclass, field\n"
        "\n"
        "\n"
        "@dataclass\n"
        "class Point:\n"
        "    \"\"\"A 2D point.\"\"\"\n"
        "    x: float\n"
        "    y: float\n"
        "\n"
        "    def distance_to(self, other):\n"
        "        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5\n"
        "\n"
        "\n"
        "@dataclass\n"
        "class Student:\n"
        "    \"\"\"A student record with default grade.\"\"\"\n"
        "    name: str\n"
        "    age: int\n"
        "    grade: float = 0.0\n"
        "    courses: list = field(default_factory=list)\n"
        "\n"
        "    def __post_init__(self):\n"
        "        if self.age < 0:\n"
        "            raise ValueError(\"Age cannot be negative\")\n"
        "\n"
        "\n"
        "@dataclass(frozen=True)\n"
        "class Color:\n"
        "    \"\"\"An immutable color -- usable as a dict key.\"\"\"\n"
        "    r: int\n"
        "    g: int\n"
        "    b: int\n"
        "\n"
        "\n"
        "p1 = Point(0, 0)\n"
        "p2 = Point(3, 4)\n"
        "print(p1.distance_to(p2))  # 5.0\n"
        "print(p1)                  # Point(x=0, y=0)\n"
        "\n"
        "s = Student(\"Alice\", 20, 85.5)\n"
        "print(s)  # Student(name='Alice', age=20, grade=85.5, courses=[])\n"
        "\n"
        "red = Color(255, 0, 0)\n"
        "# red.r = 128  -> FrozenInstanceError!\n"
    ),
    key_points=[
        "@dataclass auto-generates __init__, __repr__, and __eq__ from type annotations.",
        "Use field(default_factory=list) for mutable defaults, never field(default=[]).",
        "__post_init__ runs after __init__ for validation or derived attributes.",
        "frozen=True makes instances immutable and hashable.",
        "order=True auto-generates comparison methods; slots=True saves memory.",
    ],
)

_lesson_design_patterns = Lesson(
    id="design_patterns",
    title="Design Patterns in Python",
    content=(
        "Design patterns are reusable solutions to common software design problems.\n"
        "The famous 'Gang of Four' (GoF) book catalogued 23 patterns in the\n"
        "context of C++ and Smalltalk. In Python, many of these patterns are either\n"
        "built into the language, dramatically simplified, or unnecessary. Let's\n"
        "look at a few of the most useful patterns and their Pythonic\n"
        "implementations.\n\n"
        "The Singleton pattern ensures a class has only one instance. In Python,\n"
        "the simplest singleton is just a module -- module-level variables are\n"
        "shared across all imports. If you need a class-based singleton, override\n"
        "`__new__` to return the same instance every time: store the instance as a\n"
        "class attribute and check if it already exists before creating a new one.\n"
        "However, in Python, singletons are rarely needed -- modules and global\n"
        "variables usually suffice.\n\n"
        "The Observer pattern (also called Publish-Subscribe) lets objects\n"
        "subscribe to events and get notified when they occur. In Python, this\n"
        "is elegantly implemented with callback lists. An EventEmitter stores a\n"
        "dictionary mapping event names to lists of callback functions. The `on()`\n"
        "method registers a callback, and `emit()` calls all registered callbacks\n"
        "for a given event. Python's first-class functions make this pattern\n"
        "trivial to implement.\n\n"
        "The Strategy pattern lets you swap algorithms at runtime. In traditional\n"
        "OOP, you define a Strategy interface with concrete strategy classes. In\n"
        "Python, you can simply pass a function. Need a different sorting strategy?\n"
        "Pass a different key function to sorted(). Python's first-class functions\n"
        "often eliminate the need for the full class-based pattern.\n\n"
        "The Factory pattern creates objects without specifying the exact class.\n"
        "In Python, @classmethod factory methods (like `datetime.fromtimestamp()`)\n"
        "are the idiomatic approach. You can also use simple factory functions.\n"
        "The important insight is that many GoF patterns exist to work around\n"
        "limitations of static languages. Python's dynamic nature, first-class\n"
        "functions, and powerful built-ins mean you should always look for the\n"
        "simplest Pythonic solution first."
    ),
    code_example=(
        "# Strategy Pattern: swap algorithms via functions\n"
        "def price_with_discount(price, discount_strategy):\n"
        "    \"\"\"Apply a discount strategy to a price.\"\"\"\n"
        "    return discount_strategy(price)\n"
        "\n"
        "\n"
        "def no_discount(price):\n"
        "    return price\n"
        "\n"
        "\n"
        "def ten_percent_off(price):\n"
        "    return price * 0.9\n"
        "\n"
        "\n"
        "def buy_one_get_half(price):\n"
        "    return price * 0.75\n"
        "\n"
        "\n"
        "# Swap strategies at runtime\n"
        "print(price_with_discount(100, no_discount))       # 100\n"
        "print(price_with_discount(100, ten_percent_off))    # 90.0\n"
        "print(price_with_discount(100, buy_one_get_half))   # 75.0\n"
        "\n"
        "\n"
        "# Singleton using __new__\n"
        "class Config:\n"
        "    _instance = None\n"
        "\n"
        "    def __new__(cls):\n"
        "        if cls._instance is None:\n"
        "            cls._instance = super().__new__(cls)\n"
        "        return cls._instance\n"
        "\n"
        "\n"
        "c1 = Config()\n"
        "c2 = Config()\n"
        "print(c1 is c2)  # True -- same instance\n"
    ),
    key_points=[
        "Singleton: use a module or override __new__; often unnecessary in Python.",
        "Observer: store callbacks in a dict; Python's first-class functions make it easy.",
        "Strategy: just pass a function; no need for interface classes in Python.",
        "Factory: use @classmethod factory methods or simple factory functions.",
        "Many GoF patterns simplify dramatically in Python thanks to dynamic typing and first-class functions.",
    ],
)

# ---------------------------------------------------------------------------
# Exercises
# ---------------------------------------------------------------------------

_exercise_create_class = Exercise(
    id="create_class",
    title="Create a Class",
    description=(
        "Create a `Rectangle` class with `width` and `height` attributes\n"
        "(set in __init__) and an `area()` method that returns the area\n"
        "(width * height)."
    ),
    starter_code=(
        "# Define a Rectangle class with width, height, and an area() method\n"
    ),
    test_cases=[
        {
            "name": "Create rectangle",
            "input_code": "r = Rectangle(5, 3)\nprint(r.area())",
            "expected": "15",
        },
        {
            "name": "Different size",
            "input_code": "r = Rectangle(10, 4)\nprint(r.area())",
            "expected": "40",
        },
    ],
    solution=(
        "class Rectangle:\n"
        "    def __init__(self, width, height):\n"
        "        self.width = width\n"
        "        self.height = height\n"
        "\n"
        "    def area(self):\n"
        "        return self.width * self.height\n"
    ),
    hints=[
        "Define the class with 'class Rectangle:'",
        "The __init__ method should accept self, width, and height.",
        "Store them as self.width and self.height.",
        "The area() method returns self.width * self.height.",
    ],
    difficulty="easy",
)

_exercise_class_methods = Exercise(
    id="class_methods_ex",
    title="Factory Method",
    description=(
        "Create a `Circle` class with a `radius` attribute, an `area()` method\n"
        "that returns the area (pi * radius**2), and a @classmethod\n"
        "`from_diameter(cls, diameter)` that creates a Circle from a diameter\n"
        "(radius = diameter / 2). Use `import math` for pi."
    ),
    starter_code=(
        "import math\n"
        "\n"
        "# Define a Circle class with radius, area(), and from_diameter()\n"
    ),
    test_cases=[
        {
            "name": "From radius",
            "input_code": "import math\nc = Circle(5)\nprint(round(c.area(), 2))",
            "expected": "78.54",
        },
        {
            "name": "From diameter",
            "input_code": "import math\nc = Circle.from_diameter(10)\nprint(c.radius)",
            "expected": "5.0",
        },
    ],
    solution=(
        "import math\n"
        "\n"
        "class Circle:\n"
        "    def __init__(self, radius):\n"
        "        self.radius = radius\n"
        "\n"
        "    def area(self):\n"
        "        return math.pi * self.radius ** 2\n"
        "\n"
        "    @classmethod\n"
        "    def from_diameter(cls, diameter):\n"
        "        return cls(diameter / 2)\n"
    ),
    hints=[
        "Use math.pi for the value of pi.",
        "A @classmethod receives `cls` as its first parameter.",
        "from_diameter should return cls(diameter / 2).",
        "The radius from from_diameter(10) should be 5.0 (a float).",
    ],
    difficulty="medium",
)

_exercise_property = Exercise(
    id="property_ex",
    title="Temperature Property",
    description=(
        "Create a `Temperature` class that stores the temperature in Celsius\n"
        "(set via __init__). Add a `fahrenheit` property with both a getter\n"
        "and a setter. Formula: F = C * 9/5 + 32. The setter should convert\n"
        "back: C = (F - 32) * 5/9."
    ),
    starter_code=(
        "# Define a Temperature class with a celsius attribute\n"
        "# and a fahrenheit property (getter and setter)\n"
    ),
    test_cases=[
        {
            "name": "C to F",
            "input_code": "t = Temperature(100)\nprint(t.fahrenheit)",
            "expected": "212.0",
        },
        {
            "name": "F to C",
            "input_code": "t = Temperature(0)\nt.fahrenheit = 212\nprint(t.celsius)",
            "expected": "100.0",
        },
    ],
    solution=(
        "class Temperature:\n"
        "    def __init__(self, celsius):\n"
        "        self.celsius = celsius\n"
        "\n"
        "    @property\n"
        "    def fahrenheit(self):\n"
        "        return self.celsius * 9 / 5 + 32\n"
        "\n"
        "    @fahrenheit.setter\n"
        "    def fahrenheit(self, value):\n"
        "        self.celsius = (value - 32) * 5 / 9\n"
    ),
    hints=[
        "Use @property to create the getter for fahrenheit.",
        "Use @fahrenheit.setter to create the setter.",
        "The getter returns self.celsius * 9 / 5 + 32.",
        "The setter sets self.celsius = (value - 32) * 5 / 9.",
    ],
    difficulty="medium",
)


def _validate_shapes(namespace, stdout):
    """Validator for the shape hierarchy exercise."""
    import math
    if 'Square' not in namespace or 'Circle' not in namespace:
        return False, "Both Square and Circle classes must be defined"
    s = namespace['Square'](4)
    c = namespace['Circle'](5)
    if abs(s.area() - 16) > 0.01:
        return False, f"Square(4).area() should be 16, got {s.area()}"
    if abs(c.area() - math.pi * 25) > 0.01:
        return False, f"Circle(5).area() should be ~78.54, got {c.area()}"
    if not isinstance(s, namespace['Shape']):
        return False, "Square should inherit from Shape"
    return True, "Shape hierarchy is correct!"


_exercise_inheritance = Exercise(
    id="inheritance_ex",
    title="Shape Hierarchy",
    description=(
        "Create a base `Shape` class with a `name` attribute (set in __init__)\n"
        "and an `area()` method that returns 0. Then create `Square(Shape)` with\n"
        "a `side` attribute that overrides area() to return side**2, and\n"
        "`Circle(Shape)` with a `radius` attribute that overrides area() to\n"
        "return math.pi * radius**2. Use `import math`."
    ),
    starter_code=(
        "import math\n"
        "\n"
        "# Define Shape, Square(Shape), and Circle(Shape)\n"
    ),
    validator=_validate_shapes,
    solution=(
        "import math\n"
        "\n"
        "class Shape:\n"
        "    def __init__(self, name):\n"
        "        self.name = name\n"
        "\n"
        "    def area(self):\n"
        "        return 0\n"
        "\n"
        "\n"
        "class Square(Shape):\n"
        "    def __init__(self, side):\n"
        "        super().__init__('Square')\n"
        "        self.side = side\n"
        "\n"
        "    def area(self):\n"
        "        return self.side ** 2\n"
        "\n"
        "\n"
        "class Circle(Shape):\n"
        "    def __init__(self, radius):\n"
        "        super().__init__('Circle')\n"
        "        self.radius = radius\n"
        "\n"
        "    def area(self):\n"
        "        return math.pi * self.radius ** 2\n"
    ),
    hints=[
        "Square and Circle should inherit from Shape: class Square(Shape):",
        "Call super().__init__(name) in each subclass __init__.",
        "Override area() in each subclass to return the correct formula.",
        "Use math.pi for the circle area calculation.",
    ],
    difficulty="medium",
)

_exercise_dunder = Exercise(
    id="dunder_ex",
    title="Vector Class",
    description=(
        "Create a `Vector` class with `x` and `y` attributes. Implement:\n"
        "- __add__: vector addition, returning a new Vector\n"
        "- __str__: returns 'Vector(x, y)'\n"
        "- __eq__: returns True if x and y match"
    ),
    starter_code=(
        "# Define a Vector class with x, y, __add__, __str__, and __eq__\n"
    ),
    test_cases=[
        {
            "name": "String repr",
            "input_code": "print(Vector(3, 4))",
            "expected": "Vector(3, 4)",
        },
        {
            "name": "Addition",
            "input_code": "print(Vector(1, 2) + Vector(3, 4))",
            "expected": "Vector(4, 6)",
        },
        {
            "name": "Equality",
            "input_code": "print(Vector(1, 2) == Vector(1, 2))",
            "expected": "True",
        },
    ],
    solution=(
        "class Vector:\n"
        "    def __init__(self, x, y):\n"
        "        self.x = x\n"
        "        self.y = y\n"
        "\n"
        "    def __add__(self, other):\n"
        "        return Vector(self.x + other.x, self.y + other.y)\n"
        "\n"
        "    def __str__(self):\n"
        "        return f'Vector({self.x}, {self.y})'\n"
        "\n"
        "    def __eq__(self, other):\n"
        "        return self.x == other.x and self.y == other.y\n"
    ),
    hints=[
        "__add__ should return a NEW Vector with summed components.",
        "__str__ should return the exact format: 'Vector(x, y)'.",
        "__eq__ should compare both x and y values.",
    ],
    difficulty="medium",
)


def _validate_bank(namespace, stdout):
    """Validator for the bank account exercise."""
    if 'BankAccount' not in namespace:
        return False, "BankAccount class not defined"
    acct = namespace['BankAccount'](100)
    acct.deposit(50)
    if acct.get_balance() != 150:
        return False, f"After deposit(50), balance should be 150, got {acct.get_balance()}"
    result = acct.withdraw(200)
    if acct.get_balance() != 150:
        return False, "Withdraw exceeding balance should be rejected"
    acct.withdraw(30)
    if acct.get_balance() != 120:
        return False, f"After withdraw(30), balance should be 120, got {acct.get_balance()}"
    return True, "BankAccount works correctly!"


_exercise_encapsulation = Exercise(
    id="encapsulation_ex",
    title="Bank Account",
    description=(
        "Create a `BankAccount` class with:\n"
        "- A private `__balance` attribute (set via __init__ with initial balance)\n"
        "- `deposit(amount)`: adds amount to balance\n"
        "- `withdraw(amount)`: subtracts amount ONLY if sufficient funds exist\n"
        "- `get_balance()`: returns the current balance\n"
        "Withdraw should not allow the balance to go below 0."
    ),
    starter_code=(
        "# Define a BankAccount class with private __balance,\n"
        "# deposit(), withdraw(), and get_balance() methods\n"
    ),
    validator=_validate_bank,
    solution=(
        "class BankAccount:\n"
        "    def __init__(self, balance=0):\n"
        "        self.__balance = balance\n"
        "\n"
        "    def deposit(self, amount):\n"
        "        if amount > 0:\n"
        "            self.__balance += amount\n"
        "\n"
        "    def withdraw(self, amount):\n"
        "        if 0 < amount <= self.__balance:\n"
        "            self.__balance -= amount\n"
        "            return True\n"
        "        return False\n"
        "\n"
        "    def get_balance(self):\n"
        "        return self.__balance\n"
    ),
    hints=[
        "Use self.__balance for the private attribute (name mangling).",
        "In withdraw(), check that amount <= self.__balance before subtracting.",
        "get_balance() simply returns self.__balance.",
    ],
    difficulty="medium",
)

_exercise_dataclass = Exercise(
    id="dataclass_ex",
    title="Student Dataclass",
    description=(
        "Create a `Student` dataclass with:\n"
        "- name: str\n"
        "- age: int\n"
        "- grade: float (default 0.0)\n"
        "- A method `is_passing()` that returns True if grade >= 60.\n"
        "Don't forget to import dataclass from dataclasses."
    ),
    starter_code=(
        "from dataclasses import dataclass, field\n"
        "\n"
        "# Define a Student dataclass\n"
    ),
    test_cases=[
        {
            "name": "Create student",
            "input_code": "s = Student('Alice', 20, 85.5)\nprint(f'{s.name}, {s.age}')",
            "expected": "Alice, 20",
        },
        {
            "name": "Default grade",
            "input_code": "s = Student('Bob', 18)\nprint(s.grade)",
            "expected": "0.0",
        },
        {
            "name": "Passing",
            "input_code": "print(Student('A', 20, 75).is_passing())",
            "expected": "True",
        },
        {
            "name": "Failing",
            "input_code": "print(Student('B', 20, 50).is_passing())",
            "expected": "False",
        },
    ],
    solution=(
        "from dataclasses import dataclass, field\n"
        "\n"
        "@dataclass\n"
        "class Student:\n"
        "    name: str\n"
        "    age: int\n"
        "    grade: float = 0.0\n"
        "\n"
        "    def is_passing(self):\n"
        "        return self.grade >= 60\n"
    ),
    hints=[
        "from dataclasses import dataclass, field",
        "Decorate the class with @dataclass.",
        "Fields with defaults must come after fields without defaults.",
        "is_passing() just returns self.grade >= 60.",
    ],
    difficulty="easy",
)


def _validate_observer(namespace, stdout):
    """Validator for the observer pattern exercise."""
    if 'EventEmitter' not in namespace:
        return False, "EventEmitter class not defined"
    emitter = namespace['EventEmitter']()
    results = []
    emitter.on('data', lambda x: results.append(x))
    emitter.on('data', lambda x: results.append(x * 2))
    emitter.emit('data', 5)
    if results == [5, 10]:
        return True, "EventEmitter works correctly!"
    return False, f"Expected [5, 10], got {results}"


_exercise_design_pattern = Exercise(
    id="design_pattern_ex",
    title="Observer Pattern",
    description=(
        "Implement an `EventEmitter` class with:\n"
        "- `on(event, callback)`: registers a callback for the given event name\n"
        "- `emit(event, *args)`: calls all registered callbacks for that event,\n"
        "  passing *args to each callback\n"
        "Hint: use a dictionary mapping event names to lists of callbacks."
    ),
    starter_code=(
        "# Define an EventEmitter class with on() and emit() methods\n"
    ),
    validator=_validate_observer,
    solution=(
        "class EventEmitter:\n"
        "    def __init__(self):\n"
        "        self._events = {}\n"
        "\n"
        "    def on(self, event, callback):\n"
        "        if event not in self._events:\n"
        "            self._events[event] = []\n"
        "        self._events[event].append(callback)\n"
        "\n"
        "    def emit(self, event, *args):\n"
        "        for callback in self._events.get(event, []):\n"
        "            callback(*args)\n"
    ),
    hints=[
        "Store events in a dict: self._events = {}",
        "on() appends the callback to self._events[event].",
        "emit() iterates over self._events.get(event, []) and calls each callback.",
        "Use *args in emit() to pass arguments to callbacks.",
    ],
    difficulty="hard",
)

# ---------------------------------------------------------------------------
# Quiz
# ---------------------------------------------------------------------------

_quiz = [
    QuizQuestion(
        id="q1_self",
        question="What is the first parameter of a regular instance method?",
        options=[
            "A) cls",
            "B) this",
            "C) self",
            "D) instance",
        ],
        correct="C",
        explanation=(
            "By convention, the first parameter of an instance method is named "
            "'self'. It refers to the instance the method is called on. While "
            "the name 'self' is a convention (not enforced by Python), it is "
            "universally followed."
        ),
    ),
    QuizQuestion(
        id="q2_classmethod",
        question="What decorator creates a method that receives the class as its first argument?",
        options=[
            "A) @staticmethod",
            "B) @classmethod",
            "C) @property",
            "D) @abstract",
        ],
        correct="B",
        explanation=(
            "@classmethod makes the method receive `cls` (the class) as its "
            "first argument instead of `self` (an instance). This is ideal for "
            "factory methods and class-level operations."
        ),
    ),
    QuizQuestion(
        id="q3_name_mangling",
        question="What does name mangling do to `__attr`?",
        options=[
            "A) Makes it truly private",
            "B) Renames it to `_ClassName__attr`",
            "C) Deletes it",
            "D) Makes it read-only",
        ],
        correct="B",
        explanation=(
            "Python's name mangling renames double-underscore attributes to "
            "_ClassName__attr. This prevents accidental name collisions in "
            "subclasses but does not provide true privacy -- the mangled name "
            "is still accessible."
        ),
    ),
    QuizQuestion(
        id="q4_mro",
        question="What does MRO stand for?",
        options=[
            "A) Method Return Object",
            "B) Multiple Runtime Override",
            "C) Method Resolution Order",
            "D) Module Resource Organizer",
        ],
        correct="C",
        explanation=(
            "MRO stands for Method Resolution Order. It defines the order in "
            "which Python searches classes when looking up a method, which is "
            "especially important with multiple inheritance."
        ),
    ),
    QuizQuestion(
        id="q5_abc_module",
        question="Which module provides abstract base classes?",
        options=[
            "A) abstract",
            "B) abc",
            "C) interface",
            "D) base",
        ],
        correct="B",
        explanation=(
            "The `abc` module (Abstract Base Classes) provides the ABC class "
            "and the @abstractmethod decorator for defining abstract interfaces "
            "in Python."
        ),
    ),
    QuizQuestion(
        id="q6_str",
        question="What does the __str__ dunder method define?",
        options=[
            "A) String parsing",
            "B) Human-readable string representation",
            "C) String validation",
            "D) Serialization",
        ],
        correct="B",
        explanation=(
            "__str__ defines the human-readable, 'informal' string "
            "representation of an object. It is called by print() and str(). "
            "For a more detailed, debug-oriented representation, use __repr__."
        ),
    ),
    QuizQuestion(
        id="q7_composition",
        question="Which is NOT a benefit of composition over inheritance?",
        options=[
            "A) More flexible",
            "B) Loose coupling",
            "C) Automatic method inheritance",
            "D) Easier testing",
        ],
        correct="C",
        explanation=(
            "Automatic method inheritance is a feature of inheritance, not "
            "composition. With composition, you must explicitly delegate method "
            "calls. The trade-off is greater flexibility, looser coupling, and "
            "easier testing."
        ),
    ),
    QuizQuestion(
        id="q8_frozen_dataclass",
        question="What decorator makes a dataclass immutable?",
        options=[
            "A) @dataclass(frozen=True)",
            "B) @dataclass(immutable=True)",
            "C) @dataclass(const=True)",
            "D) @dataclass(readonly=True)",
        ],
        correct="A",
        explanation=(
            "@dataclass(frozen=True) makes instances immutable. Any attempt to "
            "set an attribute after creation raises FrozenInstanceError. Frozen "
            "dataclasses are also automatically hashable."
        ),
    ),
]

# ---------------------------------------------------------------------------
# Module definition
# ---------------------------------------------------------------------------

module = Module(
    id="05_oop",
    title="Object-Oriented Programming",
    description="Master OOP in Python: classes, inheritance, polymorphism, and design patterns",
    lessons=[
        _lesson_classes_objects,
        _lesson_class_static_methods,
        _lesson_properties,
        _lesson_inheritance,
        _lesson_multiple_inheritance,
        _lesson_composition,
        _lesson_encapsulation,
        _lesson_polymorphism,
        _lesson_abstract_classes,
        _lesson_dunder_methods,
        _lesson_dataclasses,
        _lesson_design_patterns,
    ],
    exercises=[
        _exercise_create_class,
        _exercise_class_methods,
        _exercise_property,
        _exercise_inheritance,
        _exercise_dunder,
        _exercise_encapsulation,
        _exercise_dataclass,
        _exercise_design_pattern,
    ],
    quiz=_quiz,
)
